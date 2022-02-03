# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 16:44:10 2022

@author: Imke
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


list = ("Amazon Ratenzahlung", "Amazon Rechnung","Asos Ratenzahlung", "H&M Ratenahlung", "Mediamarkt Ratenzahlung")

#funktion bekommt Suchwort, googelt Suchwort, clickt erstes ergebnis an, liefert Link und Titel
def google_search (Suchwort):
    
    browser.get('https://www.google.de')
    time.sleep(5)

    search_box = browser.find_element(By.NAME,'q')
    search_box.send_keys(Suchwort)
    search_box.submit()

    result = browser.find_element(By.TAG_NAME,'h3')
    result.click()
    print (browser.current_url)
    title = browser.title
    print(title)
    
    
    
    
for i in range(0,5):  
    google_search(list[i])    
    
browser.close()