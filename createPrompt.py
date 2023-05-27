import re



def evaluateOutput(tryAgain,output):

    # status = re.search(r"b'  \xe2\x9c\x94 s+(\w+)", output)

    # cases_passed = re.search(r'(\d+)(?=\/\d+ cases)', output)
    # cases_passed = int(cases_passed.group()) if cases_passed else None

    # total_cases = re.search(r'(?<=\d\/)(\d+)(?= cases)', output)
    # total_cases = int(total_cases.group()) if total_cases else None
    
    #if checkmark in output, all good
    if "\\xe2\\x9c\\x94" in output:
        tryAgain = False
        print('all good')


    #if crossmark in output, try again
    elif "\\xe2\\x9c\\x98" in output:
        tryAgain = True
        print('and another one')

    else:
        print('nothing in')

    output = re.sub(r'\\xe2\\x9c\\x98', '', output)
    output = re.sub(r'\\xe2\\x9c\\x94', '', output)
    print(output)
    output = 'There seems to be an issue in the code: ' + output + 'Correct the error.'

    return tryAgain, output