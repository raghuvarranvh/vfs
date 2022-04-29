# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:18:40 2022

@author: rgv1cob
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.support.ui import Select
#%%
driver = webdriver.Chrome(executable_path ='C:/Users/rgv1cob/Downloads/chromedriver_1.exe')
driver.get("https://visa.vfsglobal.com/ind/en/deu/login")
#%%

#%%
username = driver.find_element_by_id("mat-input-0")
username.clear()
username.send_keys("raghuvarranvh@gmail.com")

passwd = driver.find_element_by_id("mat-input-1")
passwd.clear()
passwd.send_keys("Raghu#27")
#%% sign in

driver.find_element_by_class_name("mat-button-wrapper").click()
#%%

#%% start new booking
#driver.find_element_by_css_selector("body > app-root > div > app-dashboard > section > div > div.row.mb-10.mb-md-25 > div.col-12.col-sm-auto.d-lg-none > button").click()
#driver.find_element_by_xpath("/html/body/app-root/div/app-dashboard/section/div/div[1]/div[2]/button").click()
driver.find_element_by_class_name("mat-button-wrapper").click()
                             
                                    
#%% click on ecenter
driver.find_element_by_class_name("mat-select-trigger ng-tns-c84-4").click()
#%%

center = driver.find_element_by_id("mat-select-value-1")
ret_test= driver.execute_script("arguments[0].innerText = 'Chennai - Visa Application Centre'", center)
#%%
category = driver.find_element_by_id("mat-select-value-3")
driver.execute_script("arguments[0].innerText = 'Schengen Visa (stay of max. 90 days or less)'", category)
#%%
subcategory = driver.find_element_by_id("mat-select-value-5")
driver.execute_script("arguments[0].innerText = 'business'", subcategory)
#%%
with open("https://visa.vfsglobal.com/ind/en/deu/login") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    
#%%    
wbpage = "https://visa.vfsglobal.com/ind/en/deu/login"
html_page= requests.get(wbpage).text
soup = BeautifulSoup(html_page,features='html.parser')

/html/body/app-root/div/app-login/section/div/div/mat-card/form/button