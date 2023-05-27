import subprocess, glob, os, time, random
from config import Config
from tqdm import tqdm
import pandas as pd
import handleQuestionBank

class LeetCodeUtil:
    def __init__(self):
        pass
    
    def generate_submit_file(self, output_file,problem_id, model_name):

        if model_name=='ChatGPT':
            def remove_import(ans:str)->str:
                ans_arr=ans.split('\n')
                for i, l in enumerate(ans_arr):
                    if l.startswith('import ') or l.startswith('from ') or l.strip()=='':
                        continue
                    else:
                        return '\n'.join(ans_arr[i:])
                return ''
            def remove_line_comment(code:str):
                return '\n'.join([l for l in code.split('\n') if not l.strip().startswith('#')])
            with open(output_file,'r',encoding='UTF8') as f:
                # problem_id=os.path.basename(os.path.dirname(os.path.dirname(output_file))).split('-')[0]
                test_num=os.path.basename(output_file).split('_')[-1].split('.')[0]
                ans=f.read().strip()
                ans=remove_line_comment(ans)
                ans=ans.replace("```python","```")
                if ans.startswith("```") and ans.endswith("```"): ans=ans[3:-3].strip()
                ans_splits=ans.split("```")
                class_splits=[l.strip() for l in ans_splits if remove_import(l.strip()).startswith('class ')]
                class_splits.sort(key=lambda x:len(x.split('\n')))
                ans=class_splits[-1]
                assert(remove_import(ans).startswith('class '))
                ans=f'# @lc app=leetcode id={problem_id} lang=python3\n'+ans
                py_file_path=os.path.join(os.path.dirname(output_file),f'{problem_id}.output_{test_num}.py')
                assert("class " in [l for l in remove_import(remove_line_comment(ans)).split('\n') if l.strip()!=''][0])
                try: assert("return" in ans)
                except: print('return not found:',output_file)
                with open(py_file_path,'w',encoding='UTF8') as fw:
                    fw.write(ans)
                print('Generated',py_file_path)
      
        else: assert(False, f'Unknown model_name: {model_name}')
        
        return py_file_path
    
    def remove_leetcode_result(self, py_file_path):
        result_path=py_file_path.replace('.py','_result.txt')
        if os.path.exists(result_path): os.remove(result_path)
        
    
    def iterate_python_files(self, python_file_path,error_exists ,error_total,error_cnt, prev_err,timeout, timeoutCount):
            
        py_result_file=python_file_path[:-3]+'_result.txt'

        #Sometimes leetcode does not answer
        try:
            
            p=subprocess.run(['leetcode','submit',python_file_path,'-l','python3'],capture_output=True, timeout=timeout)

        except subprocess.TimeoutExpired:
            timeoutCount = timeoutCount +1
            print('TIMEOUT')

            if timeoutCount < 3:
                self.iterate_python_files(python_file_path, timeout, timeoutCount= timeoutCount)
            else:
                print("SESSION KEEPS TIMING OUT")
                return False,False


        if 'http error' in str(p.stdout) or "[ERROR] session expired" in str(p.stdout) or\
            "[ERROR] Problem not found!" in str(p.stdout): 
            error_exists=True
            error_total+=1
            if prev_err: error_cnt+=1
            else: error_cnt=1
            prev_err=True
            if error_cnt>20: 
                print('Too many errors.')
                return False,False
        else:
            prev_err=False

            with open(py_result_file,'w',encoding='UTF8') as f:
                f.write('\n**stdout:**\n')
                f.write(str(p.stdout))
                f.write('\n**stderr:**\n')
                f.write(str(p.stderr))
        # time.sleep(5)
        # print('# of http error or session expired error: ',error_total)

        return error_exists, str(p.stdout)
    
    
    def run_leetcode_test(self, python_file_path):

        def result_exists(result_file:str):
            if not os.path.exists(result_file): return False
            with open(result_file,'r',encoding='UTF8') as f:
                result=f.read()
            if "[ERROR] Problem not found!" in result or "ECONNRESET" in result \
                or "Error: socket hang up" in result or "Error: connect ETIMEDOUT" in result \
                    or "Error: getaddrinfo ENOTFOUND" in result or "ECONNABORTED" in result \
                        or "[ERROR] Error: write EPROTO " in result: return False
            return True

        error_exists=True
        error_cnt=0
        error_total=0
        prev_err=False

        while(error_exists):
            
            error_exists=False
            error_cnt=0
            error_total=0

            #iterate the x python files but restart if it takes too long
            error_exists,stdout = self.iterate_python_files(python_file_path, error_exists ,error_total,error_cnt,prev_err,timeout = 300, timeoutCount=0)
        
        return stdout
        
    def run_leetcode_pipeline(self, output_dir):
        config=Config()
        root_path=os.path.normpath(config.generation_path)

        #load all IDs that haven't been treated yet
        #folder_path_list = handleQuestionBank.validateQuestions(config.sampled_df_path, config.logFile)
        
        for folder_name in folder_path_list:

            folder_name = str(folder_name)
            print('--------------------------------------------------------')
            print(folder_name)
            #We don't want to iterate over hidden files such as .DS_Store
            if folder_name.startswith('.'):
                continue
            
            problem_folder_path = os.path.join(root_path, folder_name)

            if not os.path.isdir(problem_folder_path):
                print('ERROR with folders')
                break

            problem_result_folder_path = os.path.join(problem_folder_path, config.target_folder)
            problem_solution_files_path = glob.glob(problem_result_folder_path + '/*.py')
            self.run_leetcode_test(problem_solution_files_path)

            handleQuestionBank.logQuestionValidation(folder_name,problem_result_folder_path,config.sampled_df_path, config.logFile)
        