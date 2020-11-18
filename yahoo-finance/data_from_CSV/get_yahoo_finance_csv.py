from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import sys
from pathlib import Path
p = Path.cwd().parent
sys.path.append(str(p))

from connection.db_config import config


import time

driver = webdriver.Chrome("F:\Mango\Documents\Code\Python\chromedriver\chromedriver.exe")

try:
    myurl = "https://finance.yahoo.com/"
    driver.get(myurl)

    # input for search
    driver.find_element_by_id('yfin-usr-qry').clear()
    driver.find_element_by_id('yfin-usr-qry').send_keys('AAPL')
    
    # click submit btn
    time.sleep(2)
    sub = driver.find_element_by_id('header-desktop-search-button')
    sub.click()
    time.sleep(3)

    # click Historical Data link
    ul = driver.find_element_by_id('quote-nav').find_element_by_tag_name('ul')
    items = ul.find_elements_by_css_selector('a span')
    for item in items:
        if item.text == "Historical Data":
            item.click()
            break
    time.sleep(2)

    # click download button to download csv
    
    items = driver.find_elements_by_css_selector('a span')
    for item in items:
        if item.text == "Download":
            item.click()
            break

    time.sleep(1)
    
    driver.quit()
except:
    pass