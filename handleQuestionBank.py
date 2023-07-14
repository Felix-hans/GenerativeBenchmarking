import os
import re
import pandas as pd
from config import Config

def filter_and_sample():
    config = Config()

    df = pd.read_excel(config.questionBank)

    # Remove duplicate rows based on the column ID

    # df = df.drop_duplicates(subset='ID')

    # Filter the DataFrame according to the specified conditions
    df = df[df['Period'] == config.period]

    df = df[df['premium'] == config.premium]

    df = df[df['Type'].isin(config.type_list)]

    sampled_dataframes = []

    # For each difficulty level and type specified, sample the specified number of rows
    for type_ in config.type_list:
        for difficulty, n_samples in config.difficulty_dict.items():
            temp_df = df[(df['Difficulty'] == difficulty) & (df['Type'] == type_)]
            
            # If the number of rows is less than n_samples, take all rows
            if temp_df.shape[0] <= n_samples:
                sampled_dataframes.append(temp_df)
            else:
                sampled_dataframes.append(temp_df.sample(n=n_samples))

    # Concatenate all sampled dataframes
    sampled_df = pd.concat(sampled_dataframes)

    sampled_df.to_excel(config.sampled_df_path, index = False)
    return sampled_df

# def createFolderPathList(df,root_path):
    
#     folder_path_list = []
#     for id_ in df['ID']:

#         problem_folder_path = os.path.join(root_path, str(id_))
#         folder_path_list.append(problem_folder_path)
#     return folder_path_list

def logQuestionGeneration(logFile,folder_name):

    config = Config()
    df = pd.read_excel(logFile)

    df.loc[df['ID'] == int(folder_name), config.generated_name] = 1

    df.to_excel(logFile, index=False)


'''
def logQuestionVerification(logFile,folder_name):
    
    df = pd.read_excel('logFile')

    df = df.loc[df['ID'] == folder_name, 'validated'] = 1

    df.to_excel(logFile, index=False)
'''
def removeGeneratedQuestions(sampled_df, log_df):

    config = Config()

    generated_ids = list(log_df[log_df[config.generated_name]==1]['ID'])
    print("generated-ids")
    print(generated_ids) 

    df = sampled_df[~sampled_df.ID.isin(generated_ids)]
    print(df)
    print(len(df))

    return df

def getResultFiles(dir_path,rep):
    result_files = []
    for root, dirs, files in os.walk(dir_path):
        for file in files: 

            if file.endswith(f'output_{rep}_result.txt'):
                result_files.append(os.path.join(root, file))
    return result_files


def parse_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

        status = re.search(r"b'  \\xe2\\x9c\\x9\d s+(\w+)", content)

        cases_passed = re.search(r'(\d+)(?=\/\d+ cases)', content)
        cases_passed = int(cases_passed.group()) if cases_passed else None

        total_cases = re.search(r'(?<=\d\/)(\d+)(?= cases)', content)
        total_cases = int(total_cases.group()) if total_cases else None

        try:
            ratio_cases = cases_passed/total_cases
        except:
            ratio_cases = "ERROR"
            print("####################################################")
            print()
            print("ERROR IN SUBMISSION")
            print()
            print("####################################################")

        runtime_performance = re.search(r'(?<=Your runtime beats )([\d\.]+)', content)
        runtime_performance = float(runtime_performance.group()) if runtime_performance else None

        memory_performance = re.search(r'(?<=Your memory usage beats )([\d\.]+)', content)
        memory_performance = float(memory_performance.group()) if memory_performance else None

        return status, cases_passed, total_cases, ratio_cases, runtime_performance, memory_performance

def createStatistictsColumns(sampled_df, rep,iteration):

    col = f'case_{rep}_attempt_{iteration}_ratio_cases'
    if col not in sampled_df.columns:
        sampled_df[f'case_{rep}_attempt_{iteration}_ratio_cases'] = None
        sampled_df[f'case_{rep}_attempt_{iteration}_runtime_performance'] = None
        sampled_df[f'case_{rep}_attempt_{iteration}_memory_performance'] = None

    return sampled_df


def getAndInsertValidationStatistics(folder_name,problem_result_folder_path,sampled_df,rep,iteration):

    result_files_path = getResultFiles(problem_result_folder_path,rep)


    for i,file_path in enumerate(result_files_path):

        status, cases_passed, total_cases, ratio_cases, runtime_performance, memory_performance = parse_file(file_path)
        
        sampled_df = createStatistictsColumns(sampled_df, rep,iteration)

        sampled_df.loc[sampled_df['ID'] == int(folder_name), f'case_{rep}_attempt_{iteration}_ratio_cases'] = ratio_cases
        sampled_df.loc[sampled_df['ID'] == int(folder_name), f'case_{rep}_attempt_{iteration}_runtime_performance'] = runtime_performance
        sampled_df.loc[sampled_df['ID'] == int(folder_name), f'case_{rep}_attempt_{iteration}_memory_performance'] = memory_performance

    
    return sampled_df



def logQuestionValidation(folder_name,rep,problem_result_folder_path,sampled_df_path, logFile, iteration,tryAgain):
    
    config = Config()
    log_df = pd.read_excel(logFile)
    sampled_df = pd.read_excel(sampled_df_path)

    sampled_df = getAndInsertValidationStatistics(folder_name,problem_result_folder_path,sampled_df,rep,iteration)

    if tryAgain == False:
        log_df.loc[log_df['ID'] == int(folder_name), config.validated_name] = 1

    log_df.to_excel(logFile, index=False)
    sampled_df.to_excel(sampled_df_path, index=False)


def validateQuestions(sampled_df_path, logFile):

    config = Config()
    sampled_df = pd.read_excel(sampled_df_path)
    log_df = pd.read_excel(logFile)
    generated_ids = list(log_df[log_df[config.validated_name]==1]['ID'])


    df = sampled_df[~sampled_df.ID.isin(generated_ids)]


    folder_path_list = df['ID']
    #remove already validated questions
    return folder_path_list

def createNewColumns(log_df):
    
    config = Config()
    changed = False

    if config.generated_name not in log_df.columns:
        log_df[config.generated_name] = None
        changed = True
    
    if config.validated_name not in log_df.columns:
        log_df[config.validated_name] = None
        changed = True

    if changed:
        log_df.to_excel(config.logFile, index=False)
    
    return log_df

#This is the initial call of this part. If changes should be done at the beginning 
#(like creating new columns, it should be done hre)
def main(sampled_df_path, logFile):

    sampled_df = pd.read_excel(sampled_df_path)
    log_df = pd.read_excel(logFile)

    #We need to create the missing columns in case they were not created yet
    log_df = createNewColumns(log_df)
    
    #could be that we are re-starting because the chatgpt client stopped working
    #We want to make sure we quickly skip the questions we already answered
    df = removeGeneratedQuestions(sampled_df, log_df)

    folder_path_list = df['ID']

    return folder_path_list

    
# filter_and_sample()