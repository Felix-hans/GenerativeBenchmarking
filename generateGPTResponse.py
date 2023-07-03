import time
import sys
import openai
import yaml

def generate_chatgpt_api(messages):

    with open('/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/gptConfig.yaml', 'r') as file:
        config = yaml.safe_load(file)
     
    openai.api_key = config['OPENAI_KEY']
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
     
    return response['choices'][0]['message']['content']
     

def generate_chatgpt(chatbot, prompt):
        time.sleep(2)
        resp='Unusable response produced by ChatGPT, maybe its unavailable.'
        fail_cnt=0

        while 'Unusable response produced by ChatGPT, maybe its unavailable.' in resp:
            try:
                resp=chatbot.ask(prompt)

                # chatbot.new_conversation() # To start a new conversation
            except Exception as e:
                resp='Unusable response produced by ChatGPT, maybe its unavailable.'
            if fail_cnt==0: pass
            elif fail_cnt==5:
                print('Failed',fail_cnt,'time(s).')
                print('Exit program.')
                sys.exit()
            else:
                print('Failed',fail_cnt,'time(s).')
                print("Wait for",2**(fail_cnt-1),"seconds.")
                time.sleep(2**(fail_cnt-1))
            fail_cnt+=1

        return resp,chatbot

