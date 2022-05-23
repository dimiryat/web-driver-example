# -*- coding: utf-8 -*-
"""
Created on Mon May 23 13:20:41 2022

@author: DennisLin
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

url = 'https://www2.bot.com.tw/house/default.aspx'

try:
    driver = webdriver.Chrome(executable_path='C:\MyPython\Web_Crawler_example\chromedriver.exe')
    driver.set_page_load_timeout(60)
    driver.get(url)
    
    element = driver.find_element_by_id('fromdate_TextBox')
    element.send_keys('1010101')
    element = driver.find_element_by_id('todate_TextBox')
    element.send_keys('1060101')
    
    driver.find_element_by_id('purpose_DDL').click()
    
    for option in driver.find_elements_by_tag_name('option'):
        if option.text == '其他':
            option.click
    
    element = driver.find_element_by_id('Submit_Button').click()
    
    element = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, 'House_GridView'))
        )
    print('============================================')
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    table = soup.find(id='House_GridView')
    for row in table.find_all('tr'):
        print([s for s in row.stripped_strings])
finally:
    driver.quit()