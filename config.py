class Config:
    def __init__(self):
        # replace self.path with the path to data or data_des

        #python main.py RQ1 generate ChatGPT
        
        self.path = '/Users/XXXX-1.XXXX-2/Documents/University/project/refactory/data_des/'
        
        # replace self.generation_path with the path to code_generation_dataset
        self.generation_path = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data/problems'
        self.run_path = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data'
        
        
        # self.generation_path = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/code_generation_dataset'
        
        # update self.openai_api_key and self.openai_organization with your own key and organization
        self.openai_api_key = ''
        self.openai_organization = ''

        #Define question query configs
        self.questionBank = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data/Leetcode_question_bank_V01.xlsx'
        self.logFile = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data/Leetcode_question_log.xlsx'
        # self.sampled_df_path = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data/sampled_df.xlsx'
        self.sampled_df_path = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data/EXP01/asses_languages.xlsx'
        self.generated_name = 'EXP01_python_3_gen'
        self.validated_name = 'EXP01_python_3_val'
        self.language = 'python' #python, csharp, go, java, javascript,ruby
        self.languageLeetCode = 'python' #python, csharp,golang,java,javascript,ruby
        self.languageFileFormat = 'py' #py,cs,go,java,js,rb
        self.target_folder = 'EXP01/python_3'
        
        '''Question sampling parameters'''
        self.period = 'Before_2021'
        self.premium = False
        self.type_list = ['Dynamic_Programming','Math' ,'Design' ,'Simulation' ,'Array' ,'String' ,'Sorting' ,'Hash_Table']
        self.difficulty_dict = {'Easy': 5,'Medium': 5, 'Hard': 5}
        
        #Question configs
        self.repetition = 3 #How often to repeat the test

        #GPT configs
        self.max_length = 1024
        self.tryAgainAttempts = 0
        