import glob
import os, time
#from chatgpt_wrapper import ChatGPT
from config import Config
from leetcode_util import LeetCodeUtil
import handleQuestionBank
import generateGPTResponse
import leetcode_util
import createPrompt
import createOneShot
import verifyResponse

class GenerationUtil:
    def __init__(self):
        self.model_name = "ChatGPT"
        #self.chatbot = ChatGPT()
        self.config = Config()
        self.messages = []

  
    def generate(self,template, prompt=None, max_length=1024):


        #This is the old version referring to the inofficial chatgpt api
        #response,self.chatbot = generateGPTResponse.generate_chatgpt(self.chatbot,prompt)

        #This is the new version referring to the official chatgpt api

        response = generateGPTResponse.generate_chatgpt_api(self.messages)

        #We check whether the response fulfills the requirements we defined
        #verifyResponse.verifyResponse(self.messages,response,self.config.language, template)

        return response
        

    def get_description(self, path:str, problem_template_file_path:str, \
        with_examples:bool, with_constraints:bool):


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
            desc+=' Here is the provided template to create the solution:\n '
            desc+='\n```\n'+template+'\n```'
        if self.model_name!="ChatGPT":
            desc="'''\n'+desc+'\n'''\n"+template
            desc+='\n'+'\n'.join(
                [l for l in template.split('\n') if l.strip()!='' \
                    and (not l.strip().startswith('#'))][:2])
        
        return desc,template

    def handlePathCreation(self,root_path,folder_name):

        
        problem_folder_path = os.path.join(root_path, str(folder_name))
        
        print()
        print('HERE------------------------------------------------------------------')
        print(problem_folder_path)

        if not os.path.isdir(problem_folder_path):
            print('ERROR with folders')
            return 0

        problem_instructions_file_path = os.path.join(problem_folder_path, "README.md")
        try:
            problem_template_file_path = glob.glob(problem_folder_path + f'/*.{self.config.languageFileFormat}')[0]
        except:
            print('problem premium')
            print(problem_folder_path)
            return 0

        output_dir= os.path.join(self.config.run_path, self.config.target_folder,folder_name)
        if not os.path.exists(output_dir): os.mkdir(output_dir)
        

        return problem_instructions_file_path, problem_template_file_path,output_dir 
    
    
    def output_exists(self, out_path:str):
        if os.path.exists(out_path):
            with open(out_path,'r',encoding='UTF8') as fr:
                content=fr.read()
                if content.strip()=='':
                    return False
                return True
    

    def renameFile(self,old_name,iteration,type):
        try:
            path, filename = os.path.split(old_name)
            new_filename = filename.rsplit('.', 1)[0] + f'_attempt_{iteration}.{type}'
            new_name = os.path.join(path, new_filename)

            os.rename(old_name, new_name)
            
        except FileNotFoundError:
            print(f"The file {old_name} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    
    def executeEachRep(self,output_dir,output_path,folder_name,prompt, rep,remarks,template):
        tryAgain = True

        print(f'Asking {self.model_name}...')
        curr_time=time.time()

        self.messages.append({"role": "system", "content": remarks})

        #Append one shot
        '''
        one_shot_user, one_shot_assistant = createOneShot.createOneShot(self.config.language)
        self.messages.append({"role": "user", "content": one_shot_user})
        self.messages.append({"role": "assistant", "content": one_shot_assistant})
        
        #
        '''
        self.messages.append({"role": "user", "content": prompt})

        #print(self.messages)
        response=self.generate(template)
        #response=self.generate(template)
        

        print()
        print('RESPONSE----------------------------')
        print(response)

        
        time_used=time.time()-curr_time
        print(f'{self.model_name} response received.')
        with open(output_path,'w',encoding='UTF8') as f:
            f.write(response)
        print('Time used:',time_used)
        print()

        #Generate the output file
        py_file_path=LeetCodeUtil().generate_submit_file(output_path, folder_name)
        
        #submit test on leetcode, we try a couple of times before we stop trying
        iteration = 0
        while tryAgain:
            

            output = LeetCodeUtil().run_leetcode_test(py_file_path)
            tryAgain, errorPrompt,runtime_error = createPrompt.evaluateOutput(tryAgain, output)

            if(runtime_error == True):
                self.messages.append({"role": "user", "content": 'There is a runtime error. Do not deviate from the provided template.'})
                response=self.generate(template)
                output = LeetCodeUtil().run_leetcode_test(py_file_path)
                tryAgain, errorPrompt,runtime_error = createPrompt.evaluateOutput(tryAgain, output)
                print(response)


            
            handleQuestionBank.logQuestionValidation(folder_name,rep,output_dir,self.config.sampled_df_path, self.config.logFile, iteration,tryAgain)

            
            #we try again if the result was not accepted or we reached the maximum of attempts
            if iteration ==self.config.tryAgainAttempts or tryAgain == False:
                    break
            
            print(f'Iteration: {iteration}')

            if tryAgain:

                self.messages.append({"role": "user", "content": errorPrompt})
                response=self.generate(template)
                #response = self.generate(prompt, self.config.max_length)

                #We name the current file "attempt" to not overwrite
                self.renameFile(py_file_path, iteration, '{self.config.languageFileFormat}')
                self.renameFile(py_file_path[:-3]+'_result.txt', iteration,'txt')

                with open(output_path,'w',encoding='UTF8') as f:
                    f.write(response)
                print('Response written to',output_path)

                py_file_path=LeetCodeUtil().generate_submit_file(output_path, folder_name)

            iteration = iteration + 1
     
        #This is the command from the inofficial api to start a new conversation
        #self.chatbot.new_conversation()

        #We clean the message content for the official API
        self.messages = []
        
        return 0
        
    
    def generate_selection(self, with_examples:bool, with_constraints:bool, \
        remarks=''):

        #Define langmuage and import rules (if multiple at the same time, removing them becomes tedious)
        #We remove imports because leetcode has loaded them already and they take a lot of time and make comparisons more difficult
        remarks = f'''Implement the below task in {self.config.language} according to the following rules: 
                    - If necessary to import modules; import every module one by one in a single line (no grouped imports).
                    - Use all variables that are declared.
                    - When writing code, put the code in a markup snippet for this language in the format of ```{self.config.language} ```
                    - First create one code snippet to fill the programming template. Then, create a snippet for execution.
                    - Do not call the functions in the first code snippet to test the functions defined.
                    - Do not change the provided code template that will be given to you.'''

        root_path=os.path.normpath(self.config.generation_path)

        folder_path_list = handleQuestionBank.main(self.config.sampled_df_path, self.config.logFile)

        #We create the path where we run 
        run_folder_path = os.path.join(self.config.run_path, self.config.target_folder)
        if not os.path.exists(run_folder_path): os.mkdir(run_folder_path)

        #we iterate over all folders (problems) in the path
        for folder_name in folder_path_list:
            
            folder_name = str(folder_name)
            print('-------------------------------------------------------------------------------------')
            print(folder_name)

            #We don't want to iterate over hidden files such as .DS_Store
            if folder_name.startswith('.'):
                continue
            

            try:
                problem_instructions_file_path, problem_template_file_path,output_dir = self.handlePathCreation(root_path, folder_name)

            except Exception as e:
                print(e)
                print('folder path creation failed')

            prompt,template=self.get_description(problem_instructions_file_path, problem_template_file_path, with_examples, with_constraints)
            #print('TEMPLATE -------------------------')
            #print(template)
            #iterate x times over the problem (repeating experiment)
            for i in range(1,self.config.repetition+1):

                rep = '/output_'+str(i)+'.txt'
                output_path=output_dir+rep

                if self.output_exists(output_path): 
                    continue

                self.executeEachRep(output_dir,output_path,folder_name,prompt, i,remarks,template)
                
            handleQuestionBank.logQuestionGeneration(self.config.logFile,folder_name)
                
            # LeetCodeUtil().remove_leetcode_result(py_file_path)


