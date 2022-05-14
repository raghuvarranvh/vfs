# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:18:40 2022

@author: rgv1cob
"""

from selenium import webdriver
#from bs4 import BeautifulSoup
import requests
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

#%%

chrome_options = Options()
chrome_options.add_argument("auto-open-devtools-for-tabs")
driver = webdriver.Chrome(executable_path ='C:/Users/rgv1cob/Downloads/chromedriver_1.exe',options=chrome_options)
driver.implicitly_wait(120)
driver.get("https://visa.vfsglobal.com/ind/en/deu/login")


time.sleep(10)
#%% 
print("web page loaded; entering user credentials")


username = driver.find_element_by_id("mat-input-0")
username.clear()
username.send_keys("raghuvarranvh@gmail.com")

passwd = driver.find_element_by_id("mat-input-1")
passwd.clear()
passwd.send_keys("Raghu#27")
#%%
time.sleep(10)
#%% sign in

driver.find_element_by_class_name("mat-button-wrapper").click()
#%%

time.sleep(10)

#%% start new booking
#driver.find_element_by_css_selector("body > app-root > div > app-dashboard > section > div > div.row.mb-10.mb-md-25 > div.col-12.col-sm-auto.d-lg-none > button").click()
#driver.find_element_by_xpath("/html/body/app-root/div/app-dashboard/section/div/div[1]/div[2]/button").click()
driver.find_element_by_class_name("mat-button-base").click()
#%%
time.sleep(10)
print("start new booking successfully")
                                    
#%% click on ecenter
driver.find_element_by_id("mat-select-0").click()
time.sleep(10)
#%% Find the element id of chennai since it is changing dynamic
center_id = driver.execute_script("return document.getElementById('mat-select-0-panel').children[4].getAttribute('id')")
#%%
# select chennnai center
driver.find_element_by_id(center_id).click()
#%%
print("center chosen")
time.sleep(10)

#%% click on appointment category
driver.find_element_by_id("mat-select-2").click()
time.sleep(10)
print("category chosen")
#%% Find the element id of schengen visa since it is changing dynamic
category_id = driver.execute_script("return document.getElementById('mat-select-2-panel').children[5].getAttribute('id')")
#%%
#select schengen visa
driver.find_element_by_id(category_id).click()
#%%
time.sleep(10)
#%% click on sub category
driver.find_element_by_id("mat-select-4").click()
time.sleep(10)
#%%
#%% Find the element id of business since it is changing dynamic
subcategory_id = driver.execute_script("return document.getElementById('mat-select-4-panel').children[5].getAttribute('id')")

#%% select business
driver.find_element_by_id(subcategory_id).click()
#%%
time.sleep(10)
#%% Get response
resp=driver.execute_script("return document.getElementsByClassName('alert')[0].innerHTML")
print(resp)
#%%
