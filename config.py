class Config:
    def __init__(self):
        # replace self.path with the path to data or data_des
        
        self.path = '/Users/XXXX-1.XXXX-2/Documents/University/project/refactory/data_des/'
        
        # replace self.generation_path with the path to code_generation_dataset
        self.generation_path = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data/problems'
        self.run_path = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data'
        self.target_folder = '0107_result_sampled_hard'
        
        # self.generation_path = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/code_generation_dataset'
        
        # update self.openai_api_key and self.openai_organization with your own key and organization
        self.openai_api_key = ''
        self.openai_organization = ''

        #Define question query configs
        self.questionBank = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data/Leetcode_question_bank_V01.xlsx'
        self.logFile = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data/Leetcode_question_log.xlsx'
        # self.sampled_df_path = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data/sampled_df.xlsx'
        self.sampled_df_path = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data/sampled_df_hard_2.xlsx'
        self.generated_name = 'generated_sampled_df_hard_questions'
        self.validated_name = 'validated_sampled_df_hard_questions'
        
        '''Question sampling parameters'''
        self.period = 'Before_2021'
        self.premium = False
        self.type_list = ['Dynamic_Programming','Math' ,'Design' ,'Simulation' ,'Array' ,'String' ,'Sorting' ,'Hash_Table']
        self.difficulty_dict = {'Easy': 5,'Medium': 5, 'Hard': 5}
        
        #Question configs
        self.repetition = 5 #How often to repeat the test

        #GPT configs
        self.max_length = 1024
        self.tryAgainAttempts = 2
        