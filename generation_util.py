import glob
import os, sys, time, torch, openai
from chatgpt_wrapper import ChatGPT
from transformers import AutoModelForCausalLM, AutoTokenizer
from config import Config
from leetcode_util import LeetCodeUtil
import handleQuestionBank
import generateGPTResponse
import leetcode_util
import createPrompt

class GenerationUtil:
    def __init__(self):
        self.model_name = "ChatGPT"
        self.chatbot = ChatGPT()
        self.config = Config()

  
    def generate(self, prompt, max_length=1024):

        if self.model_name == "ChatGPT": 
            generate,self.chatbot = generateGPTResponse.generate_chatgpt(self.chatbot,prompt)

            return generate
        else: assert False, "Invalid model name"
    

    def get_description(self, path:str, problem_template_file_path:str, \
        with_examples:bool, with_constraints:bool, remarks='Implement the above task in Python.'):
        desc=None
        with open(path,'r',encoding='UTF8') as fr:
            prob=fr.read()
            
            desc=prob.split('Example')[0]
            if with_examples:
                try:
                    desc=desc+'Example 1:'+prob.split('Example 1:')[1].split('Constraints:')[0]
                except:
                    desc=desc+'Example:'+prob.split('Example:')[1].split('Constraints:')[0]
            if with_constraints:
                desc=desc+'Constraints:'+prob.split('Constraints:')[1]
        with open(problem_template_file_path,'r',encoding='UTF8') as fr:
            template=fr.read().strip()
            desc+='\n```\n'+template+'\n```'
        desc+=remarks
        if self.model_name!="ChatGPT":
            desc="'''\n'+desc+'\n'''\n"+template
            desc+='\n'+'\n'.join(
                [l for l in template.split('\n') if l.strip()!='' \
                    and (not l.strip().startswith('#'))][:2])

        return desc

    def handlePathCreation(self,root_path,folder_name):

        
        problem_folder_path = os.path.join(root_path, folder_name)
        
        print()
        print('HERE------------------------------------------------------------------')
        print(problem_folder_path)

        if not os.path.isdir(problem_folder_path):
            print('ERROR with folders')
            return 0

        problem_instructions_file_path = os.path.join(problem_folder_path, "README.md")
        try:
            problem_template_file_path = glob.glob(problem_folder_path + '/*.py')[0]
        except:
            print('problem premium')
            print(problem_folder_path)
            return 0

        output_dir=os.path.join(problem_folder_path, self.config.target_folder)
        print(output_dir)

        if not os.path.exists(output_dir): os.mkdir(output_dir)

        return problem_instructions_file_path, problem_template_file_path,output_dir 
    
    
    def output_exists(self, out_path:str):
        if os.path.exists(out_path):
            with open(out_path,'r',encoding='UTF8') as fr:
                content=fr.read()
                if content.strip()=='':
                    return False
                return True
    
    def executeEachRep(self,output_path,prompt, rep):
        tryAgain = True

        print(f'Asking {self.model_name}...')
        curr_time=time.time()

        response=self.generate(prompt, self.config.max_length)
        time_used=time.time()-curr_time
        print(f'{self.model_name} response received.')
        with open(output_path,'w',encoding='UTF8') as f:
            f.write(response)
            print('Response written to',output_path)
        print('Time used:',time_used)

        #Generate the output file
        py_file_path=LeetCodeUtil().generate_submit_file(output_path, self.model_name)

        #submit test on leetcode, we try a couple of times before we stop trying
        while tryAgain:
            output = LeetCodeUtil().run_leetcode_pipeline(py_file_path,rep)
            tryAgain, prompt = createPrompt.evaluateOutput(output)
            print('pups')
            response = self.generate(prompt, self.config.max_length)

        return 0
        
    
    def generate_selection(self, with_examples:bool, with_constraints:bool, \
        remarks='Implement the above task in Python.', repetition=5):
        
        root_path=os.path.normpath(self.config.generation_path)

        folder_path_list = handleQuestionBank.main(self.config.sampled_df_path, self.config.logFile)

        #we iterate over all folders (problems) in the path
        for folder_name in folder_path_list:
            
            folder_name = str(folder_name)

            #We don't want to iterate over hidden files such as .DS_Store
            if folder_name.startswith('.'):
                continue
            print(folder_name)

            try:
                problem_instructions_file_path, problem_template_file_path,output_dir = self.handlePathCreation(root_path, folder_name)
            except Exception as e:
                print(e)
                print('folder path creation failed')

            prompt=self.get_description(problem_instructions_file_path, problem_template_file_path, with_examples, with_constraints, remarks)
            
            #iterate x times over the problem (repeating experiment)
            for i in range(1,repetition+1):

                rep = '/output_'+str(i)+'.txt'
                output_path=output_dir+rep

                if self.output_exists(output_path): 
                    continue

                self.executeEachRep(output_path,prompt, rep)
                
            handleQuestionBank.logQuestionGeneration(self.config.logFile,folder_name)
                
            # LeetCodeUtil().remove_leetcode_result(py_file_path)


