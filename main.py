

import config
import sys
from generation_util import GenerationUtil
from leetcode_util import LeetCodeUtil
from leetcode_analysis import get_latex_tables, length_analysis




def code_generation(model, step):
    #Run this to run the entire pipeline

    # root dir of the dataset, model name, step name (generate, table, length)
    if step=='generate':
        gen=GenerationUtil()
        # gen.generate_all(True, True)
        gen.generate_selection(True,True)
    elif step=='table':
        table1, table2=get_latex_tables()
        with open('./tables.tex', 'w') as f:
            f.write(table1)
            f.write(table2)
        print('Tables are saved in ./tables.tex')
    elif step=='length':
        length_analysis()
        


if __name__ == '__main__':
    cfig = config.Config()
    path = cfig.path

    if len(sys.argv) == 2:
        script_name = sys.argv[0]
        arg1 = sys.argv[1]
        arg2 = ''
        arg3 = ''
    elif len(sys.argv) == 3:
        script_name = sys.argv[0]
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        arg3 = ''
    elif len(sys.argv) == 4:
        script_name = sys.argv[0]
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        arg3 = sys.argv[3]
    else:
        arg1 = 'RQ2'
        arg2 = 'repair'
        arg3 = 'ChatGPT'
    print('RQ: {}'.format(arg1))

    # all_assignments, descriptions = load_data()
    # bug_detection(all_assignments, descriptions)

    if arg1 == 'RQ2':
        step = arg2
        model = arg3
        # RQ-2
        program_repair(path, model, step)
    elif arg1 == 'RQ3':
        exp = arg2
        #RQ-3
        code_explanation(path, exp)
    elif arg1 == 'RQ1':
        step = arg2
        model = arg3
        code_generation(model, step)
        #Run command: python main.py RQ1 generate ChatGPT 

    elif arg1 == 'eval':
        step = arg2
        model = arg3
        LeetCodeUtil().run_leetcode_pipeline()
        


