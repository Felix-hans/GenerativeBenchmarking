import pandas as pd
import subprocess
import os

df = pd.read_excel('/Users/fhans/Documents/GenerativeBenchmarking/data/Leetcode_question_bank_V01.xlsx')


#prepare the folder location of the file and result generation
def prepare_file(item):
    folderpath = f"data/problems/{item['ID']}"
    os.makedirs(folderpath, exist_ok=True)

    resultpath = f"{folderpath}/result"
    os.makedirs(resultpath, exist_ok=True)

    return folderpath

#We get the problem statement and the predefined function
def send_request(item,folderpath):
    # the following command allows to generate the py template
    # command = f"leetcode show {item['ID']} -g -l python3"

    if item['Type']=="Database":
        command = f"leetcode show {item['ID']} -g -x -o {folderpath} -l mysql"

    else:
        command = f"leetcode show {item['ID']} -g -x -o {folderpath} -l python3"
    # command = f"leetcode show 157 -g -x -o {folderpath} -l python3"

    # # run the command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    # # get the output and errors, if any
    output, error = process.communicate()

    if output.decode().startswith("[ERROR]"):
        raise ValueError("Premium Question {item['ID']}")

    # print the error
    if error:
        print(error.decode())

#We generate a .py file that contains the problem description and the pre-defined python function
#We need to convert it
def process_file(folderpath):

    file = [f for f in os.listdir(folderpath) if os.path.isfile(os.path.join(folderpath, f))]
    filepath = folderpath + "/" + file[0]
    with open(filepath, 'r') as file:
        content = file.read()

    # Split the content into part A and part B
    #exception has to be made for SQL comments
    if '# @lc code=start' in content:
        part_a, part_b = content.split('# @lc code=start')
    elif '-- @lc code=start' in content:
        part_a, part_b = content.split('-- @lc code=start')

    # Process part A
    part_a = part_a.split("Testcase Example:")[1] # keep only content after "Testcase Example:"
    part_a = '\n'.join(line[2:] for line in part_a.split('\n')) # remove '#' at the beginning of each line
    part_a = '\n'.join(part_a.split('\n')[2:])

    with open(f'{folderpath}/README.md', 'w') as file:  # save it as a readMe file
        file.write(part_a)
    
    # Process part B
    part_b = part_b.replace('# @lc code=end', '')  # remove the line with '# @lc code=end'
    part_b = part_b.replace('-- @lc code=end', '')
    part_b = part_b.strip()  # remove leading/trailing white space
    with open(filepath, 'w') as file:  # overwrite the original .py file
        file.write(part_b)

def iterateFrame(df):
    
    #Many IDs are used multiple times in different groups, lets drop them
    df = df.drop_duplicates(subset='ID')

    #for testing use this (one example per category)
    # filtered_df = df.drop_duplicates(subset='Type')
    for index, item in df.iterrows():

        try:
            folderpath = prepare_file(item)
            send_request(item, folderpath)
            process_file(folderpath)
        except Exception as e:
            print(e)

iterateFrame(df)




reduction([0.1,0.1,0.2,0.1])
reduction([0.1,0.1,0.2,0.1,0.3])
reduction([1,'kebap',1,1])
reduction(None)