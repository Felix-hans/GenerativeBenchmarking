
import pandas as pd
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


import os
import time
import multiprocessing
import numpy as np

cwd = os.getcwd()

class Scraper:

    def __init__(self, headless):
        self.driverPath = '/Users/fhans/Desktop/Breaking_Paris_2024/chromedriver_112'
        self.proxyDriverPath = '/Users/fhans/Desktop/Breaking_Paris_2024/chromedriver_112_proxy'
        
        # self.proxy_df = self.getProxies()
        # self.driver = self.startUp()
        self.counter = 0
        self.IP = 10
        self.headless = headless
        
    def countUp(self):
        if self.counter <10:
            self.counter = self.counter + 1

        else:
            self.IP = self.IP+1
            self.counter = 0


    def startUp(self):
        # options = Options()
        #we count one up always when this is called to cap the number of startups (reducing the number of IP calls)
        self.countUp()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = self.headless
        chrome_options.add_argument("--window-size=1920,1200")
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chrome_options.add_argument('--ignore-certificate-errors')
        
        
        # print(PROXY)
        # PROXY = "23.23.23.23:3128" # IP:PORT or HOST:PORT

        driver = webdriver.Chrome(options=chrome_options, executable_path=self.driverPath)
        # driver.get("http://whatismyipaddress.com")

        # driver = webdriver.Chrome(options = options, executable_path=self.driverPath)
        
        return driver

    def getProxies(self):
        # Get free proxies for rotating
        PROXY = str(self.proxy_df['IP Address'][self.IP])  + ':' +str(self.proxy_df['Port'][self.IP])
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        options = Options()
        options.headless = False
        driver = webdriver.Chrome(options = options, executable_path=self.proxyDriverPath)
        driver.get('https://sslproxies.org')

        table = driver.find_element(By.TAG_NAME, 'table')
        thead = table.find_element(By.TAG_NAME, 'thead').find_elements(By.TAG_NAME, 'th')
        tbody = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

        headers = []
        for th in thead:
            headers.append(th.text.strip())

        proxies = []
        for tr in tbody:
            proxy_data = {}
            tds = tr.find_elements(By.TAG_NAME, 'td')
            for i in range(len(headers)):
                proxy_data[headers[i]] = tds[i].text.strip()
            proxies.append(proxy_data)
        
        proxies_df = pd.DataFrame.from_dict(proxies)
        driver.quit()

        return proxies_df

    

