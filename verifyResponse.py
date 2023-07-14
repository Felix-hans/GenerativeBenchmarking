import generateGPTResponse
import pandas as pd

def getViewShotsPython(messages):
    """
    - Does all declared variables get used?
    - Is the template used
    - is main function in seperate calling
    - Is the '''go used or just '''
    """

    template1= """
    ```
    class Solution:
        def func(self, nums: List[int], target: int) int64:

    ```
    """
    
    response_1 = """
    ```
    class Solution:
        def func(self, nums: List[int], target: int) int:
            total = nums[0] + target
            return total
    ```
    """

    subject_1 = "Here is the provided template:" + template1 + "Here is the provided response:" + response_1

    messages.append({"role": "user", "content": subject_1})
    messages.append({"role": "assistant", "content": "No, the data type of the template is different from the data type in the solution."})

    template2= """
    ```
    class Solution:
        def func(self, nums: List[int], target: int) int64:

    ```
    """
    
    response_2 = """
    ```
    class Solution:
        def func(self, nums: List[int], target: int) int:
            total = nums[0] + target
            return total

    if __name__ == "__main__":
        solution = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        print(solution.twoSum(nums, target))
    ```
    """

    subject_2 = "Here is the provided template:" + template2 + "Here is the provided response:" + response_2

    messages.append({"role": "user", "content": subject_2})
    messages.append({"role": "assistant", "content": "No, main function is called in the first code snippet. It needs to be in the second."})

    return messages


def getViewShots(messages):
    """
    - Does all declared variables get used?
    - Is the template used
    - is main function in seperate calling
    - Is the '''go used or just '''
    """
    code_control_df = pd.read_excel('/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data/EXP01/few_shots_code_control.xlsx')

    
    for index, row in code_control_df.iterrows():
        subject = "Here is the provided template:" + row['Template'] + "Here is the provided response:" + row['Code']
        messages.append({"role": "user", "content": subject})
        messages.append({"role": "assistant", "content": row['Comment']})

    return messages

def verifyResponse(org_messages, response,language,template):
    messages = []

    introduction = """
    Your are a control instance. You will receive code and have to verify whether the code fulfills the rules.
    You have to answer to the question: Does the code fulfill all guidelines? with:
    "Yes" or "No, [explanation]\n"
    """

    system_instructions = org_messages[0]['content']
    

    instructions = introduction + system_instructions
    messages.append({"role": "system", "content": instructions})

    messages = getViewShots(messages)


    subject = "Here is the provided template:\n" + template + " \nHere is the provided response:" + response

    
    messages.append({"role": "system", "content": subject})

    verdict = generateGPTResponse.generate_chatgpt_api(messages)
    print("--------------------------------------------------------")
    print(verdict)


    return 0