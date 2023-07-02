import time
import sys

def generate_chatgpt_api(chatbot,prompt):
     
     resp=chatbot.ask(prompt)
     
     
     return resp,chatbot
     

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

