class Config:
    def __init__(self):
        # replace self.path with the path to data or data_des
        
        self.path = '/Users/XXXX-1.XXXX-2/Documents/University/project/refactory/data_des/'
        
        # replace self.generation_path with the path to code_generation_dataset
        self.generation_path = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data/problems'
        self.target_folder = '2405_result_hard_design'
        # self.generation_path = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/code_generation_dataset'
        
        # update self.openai_api_key and self.openai_organization with your own key and organization
        self.openai_api_key = ''
        self.openai_organization = ''

        #Define question query configs
        self.questionBank = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data/Leetcode_question_bank_V01.xlsx'
        self.logFile = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data/Leetcode_question_log.xlsx'
        # self.sampled_df_path = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data/sampled_df.xlsx'
        self.sampled_df_path = '/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data/assess_hard_design.xlsx'
        self.generated_name = 'generated_hard_design'
        self.validated_name = 'validated_hard_design'
        
        '''Question sampling parameters'''
        self.period = 'Before_2021'
        self.premium = False
        self.type_list = ['Dynamic_Programming','Math' ,'Design' ,'Simulation' ,'Array' ,'String' ,'Sorting' ,'Hash_Table']
        self.difficulty_dict = {'Easy': 5,'Medium': 5, 'Hard': 5}