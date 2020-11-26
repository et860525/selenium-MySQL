from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import sys
from pathlib import Path
p = Path.cwd().parent
sys.path.append(str(p))

import connect_db

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

    ## Roll page
    # method 1
    #target = driver.find_element_by_css_selector('table tfoot')
    #actions = ActionChains(driver)
    #actions.move_to_element(target)
    #actions.perform()

    # method 2
    body = driver.find_element_by_css_selector('body')
    i = 0
    while i < 5:
        i += 1
        body.send_keys(Keys.END)
        time.sleep(0.5)

    # Get historical-prices table
    table = driver.find_element(By.XPATH, "//table[@data-test='historical-prices']")
    
    # Get title
    columns = [th.text.replace('*', '') for th in table.find_element_by_css_selector('tr').find_elements_by_css_selector('th')]
 
    # Get data trs without first(columns) and last(tfoot)
    trs = table.find_elements_by_css_selector('tr')[1:-1]
    
    # Get data
    rows = list()
    for tr in trs:
        # Get td.text
        row = [td.text for td in tr.find_elements_by_css_selector('td')]
        # avoid get some strings in the data
        if not any("Dividend" in s for s in row):
            if not any(s for s in row if "Stock" in s):
                rows.append(row)

    #for row in rows:
    #    print(row)

    connect_db.send_Data2Mysql(rows)

    time.sleep(2)
    
    driver.quit()
except:
    pass