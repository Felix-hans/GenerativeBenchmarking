import sys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

sys.path.append("scraping")
import scraper

'''
Scraping is not possible with chatGPT as it recognizes the input as a scraping instance.
'''

scrapeInstance = scraper.Scraper(headless=False)

driver = scrapeInstance.startUp()
driver.get('https://chat.openai.com/')


def activateGPT(gpt4=False):

    #click the log in button
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(("xpath",
                                                    '//*[@id="__next"]/div[1]/div[1]/div[4]/button[1]/div'))).click()

    #type mail address
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(("xpath",
                                                    '//*[@id="username"]'))).send_keys('felixbastian.hans@gmail.com')


    #click continue
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(("xpath",
                                                    '/html/body/div/main/section/div/div/div/div[1]/div/form/div[2]/button'))).click()


    #type password
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(("xpath",
                                                    '//*[@id="password"]'))).send_keys('Jfmamjjas0nd!' + Keys.ENTER)                                  


    #A window pops open to warn about GPT issues
    try:
        #next
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(("xpath",
                                                    '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button/div'))).click()

        #next
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(("xpath",
                                                    '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]/div'))).click()
                                                    # //*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]/div

        #done
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(("xpath",
                                                '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]/div'))).click()
                                                # //*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]/div

    except:
        print('box not found')


    #click on the select box to select the language model
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(("xpath",
                                            '//*[@id="headlessui-listbox-button-:r2:"]/span[1]'))).click()

    except:
        print('2 not found')


    #Activate gpt4 if wanted, otherwise 3.5 stays as default
    if gpt4 == True:
        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(("xpath",
                                                '//*[@id="headlessui-listbox-option-:r17:"]'))).click()

        except:
            print('GPT4 not found')


def sendPromt(promt):

    #write promt
    try:
        time.sleep(1)
        #If the side pane is there, otherwise another path has to be used
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(("xpath",
                                                    '//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[2]/textarea'))).send_keys(promt)
        
        # time.sleep(1)
        # WebDriverWait(driver, 5).until(EC.element_to_be_clickable(("xpath",
        #                                         '//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[2]/textarea'))).send_keys(Keys.COMMAND+Keys.ENTER)
    except:
        print("does not work")
        #if the side pane is not there
        
    # #send promt
    # WebDriverWait(driver, 5).until(EC.element_to_be_clickable(("xpath",
    #                                             '//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[2]/button'))).click()

    time.sleep(10)
    

def logChat():
    # Take the parent table (div) and take all their children (representing chat conversation)
    parent_div = driver.find_element("xpath", '//*[@id="__next"]/div[2]/div/main/div[1]/div/div/div')
    child_divs = parent_div.find_elements_by_xpath('./*')

    print("chidren")
    print(child_divs)
    print(len(child_divs))

    #each child has to be unpacked 
    
    # Access the nested divs using indices
    last_nested_div = child_divs.find_elements_by_xpath('./*')[-1]

    last_nested_child_div = last_nested_div.find_elements_by_xpath('./*')[0].find_elements_by_xpath('./*')[1].find_elements_by_xpath('./*')[1].find_elements_by_xpath('./*')[1].find_elements_by_xpath('./*')[0].click()


    # second_nested_div = child_divs.find_elements_by_xpath('./*')[1]
    #Get table
    #Access each element's text
    #Add to log dictionary


activateGPT()
promt = 'test'
sendPromt(promt)
# logChat()
