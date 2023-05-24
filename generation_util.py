import glob
import os, sys, time, torch, openai
from chatgpt_wrapper import ChatGPT
from transformers import AutoModelForCausalLM, AutoTokenizer
from config import Config
from leetcode_util import LeetCodeUtil
import handleQuestionBank
import generateGPTResponse


class GenerationUtil:
    def __init__(self, model_name):
        self.model_name = model_name
        if model_name == "ChatGPT":
            self.chatbot = ChatGPT()
        elif model_name == "CodeGen":
            self.model, self.tokenizer, self.device = self.load_model("Salesforce/codegen-2B-mono")
        elif model_name == "Codex":
            config=Config()
            openai.api_key = config.openai_api_key
            openai.organization = config.openai_organization
            
    
    def load_model(self, checkpoint):
        device=torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)
        model.eval()
        tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        return model, tokenizer, device
    
  
    def generate(self, prompt, max_length=1024):


        if self.model_name == "ChatGPT": return generateGPTResponse.generate_chatgpt(self.chatbot,prompt)
        elif self.model_name == "Codex": return self.generate_codex(prompt, max_length)
        elif self.model_name == "CodeGen": return self.generate_codegen(prompt, max_length)
        else: assert False, "Invalid model name"
    
    def generate_all(self, with_examples:bool, with_constraints:bool, \
        remarks='Implement the above task in Python.', max_length=1024, repetition=5):
        
        def output_exists(out_path:str):
            if os.path.exists(out_path):
                with open(out_path,'r',encoding='UTF8') as fr:
                    content=fr.read()
                    if content.strip()=='':
                        return False
                    return True
        
        config=Config()
        root_path=os.path.normpath(config.generation_path)

        #we iterate over all folders (problems) in the path
        for folder_name in os.listdir(root_path):

            #We don't want to iterate over hidden files such as .DS_Store
            if folder_name.startswith('.'):
                continue
            
            problem_folder_path = os.path.join(root_path, folder_name)
            
            print()
            print('HERE------------------------------------------------------------------')
            print(problem_folder_path)

            if not os.path.isdir(problem_folder_path):
                print('ERROR with folders')
                break

            problem_instructions_file_path = os.path.join(problem_folder_path, "README.md")
            problem_template_file_path = glob.glob(problem_folder_path + '/*.py')[0]
            output_dir=os.path.join(problem_folder_path, config.target_folder)
            
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            prompt=self.get_description(problem_instructions_file_path, problem_template_file_path, with_examples, with_constraints, remarks)
            
            response=self.generate(prompt, max_length)
            
            #iterate x times over the problem (repeating experiment)
            if not os.path.exists(output_dir): os.mkdir(output_dir)
            for i in range(1,repetition+1):
                output_path=output_dir+'/output_'+str(i)+'.txt'
                if output_exists(output_path): continue
                print(f'Asking {self.model_name}...')
                curr_time=time.time()
                response=self.generate(prompt, max_length)
                time_used=time.time()-curr_time
                print(f'{self.model_name} response received.')
                with open(output_path,'w',encoding='UTF8') as f:
                    f.write(response)
                    print('Response written to',output_path)
                print('Time used:',time_used)
                py_file_path=LeetCodeUtil().generate_submit_file(output_path, self.model_name)
                
                # LeetCodeUtil().remove_leetcode_result(py_file_path)
           
    
    
    def generate_codex(self, prompt, max_length=1024):
        try:
            resp=openai.Completion.create(engine="code-davinci-002", prompt=prompt,max_tokens=max_length)
            resp=prompt+resp.choices[0].text
            return resp
        except Exception as e:
            print(e)
            sys.exit()
    
    def generate_codegen(self, prompt, max_length=1024):
        model, tokenizer, device = self.model, self.tokenizer, self.device
        with torch.no_grad():
            completion = model.generate(**(tokenizer(prompt, return_tensors="pt")).to(device), \
                max_length=max_length, do_sample=True)
            answer = tokenizer.decode(completion[0])
        return answer
    
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

    def generate_selection(self, with_examples:bool, with_constraints:bool, \
        remarks='Implement the above task in Python.', max_length=1024, repetition=5):
        
        def output_exists(out_path:str):
            if os.path.exists(out_path):
                with open(out_path,'r',encoding='UTF8') as fr:
                    content=fr.read()
                    if content.strip()=='':
                        return False
                    return True
        
        config=Config()

        root_path=os.path.normpath(config.generation_path)

        folder_path_list = handleQuestionBank.main(config.sampled_df_path, config.logFile)

        #we iterate over all folders (problems) in the path
        for folder_name in folder_path_list:

            folder_name = str(folder_name)
            #We don't want to iterate over hidden files such as .DS_Store
            if folder_name.startswith('.'):
                continue
            
            problem_folder_path = os.path.join(root_path, folder_name)
            
            print()
            print('HERE------------------------------------------------------------------')
            print(problem_folder_path)

            if not os.path.isdir(problem_folder_path):
                print('ERROR with folders')
                break

            problem_instructions_file_path = os.path.join(problem_folder_path, "README.md")
            try:
                problem_template_file_path = glob.glob(problem_folder_path + '/*.py')[0]
            except:
                print('problem premium')
                print(problem_folder_path)
                continue

            output_dir=os.path.join(problem_folder_path, config.target_folder)
            print(output_dir)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            prompt=self.get_description(problem_instructions_file_path, problem_template_file_path, with_examples, with_constraints, remarks)
            
            response=self.generate(prompt, max_length)
            
            #iterate x times over the problem (repeating experiment)
            if not os.path.exists(output_dir): os.mkdir(output_dir)
            for i in range(1,repetition+1):
                output_path=output_dir+'/output_'+str(i)+'.txt'
                if output_exists(output_path): continue
                print(f'Asking {self.model_name}...')
                curr_time=time.time()
                response=self.generate(prompt, max_length)
                time_used=time.time()-curr_time
                print(f'{self.model_name} response received.')
                with open(output_path,'w',encoding='UTF8') as f:
                    f.write(response)
                    print('Response written to',output_path)
                print('Time used:',time_used)
                py_file_path=LeetCodeUtil().generate_submit_file(output_path, self.model_name)

            
            handleQuestionBank.logQuestionGeneration(config.logFile,folder_name)
                
                # LeetCodeUtil().remove_leetcode_result(py_file_path)