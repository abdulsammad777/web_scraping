from selenium.webdriver.common.by import By
from selenium import webdriver
import json
import os
driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe')

def Login(email, password):
    # driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe')
    location = 'https://'+f'{email}'+':'+f'{password}'+'@linkwonderland.pro/admin/list-click-rotators.php'
    driver.get(location)
Login('jarellano@prodigiousworksllc.com', 'gh453fgh4NG')



driver.find_element_by_xpath(
        ".//div//select[@name='rotator_datatable_length']/option[@value='100']").click()

lst = ['UGoogle Hangouts 001', 'UGoogle Hangouts 002', 'UGoogle Hangouts 003', 'UGoogle Hangouts 004', 'UGoogle Hangouts 005',
        'UGoogle Hangouts 006', 'UGoogle Hangouts 007', 'UGoogle Hangouts 008', 'UGoogle Hangouts 009', 'UGoogle Hangouts 010']


dict = {}
for link_name in lst:

    link_name_url = driver.find_element(By.XPATH, '//a[text()="' + link_name + '"]').get_attribute("href")
    dict[link_name] = link_name_url

with open("title_urls.json", 'w') as json_file:
    json.dump(dict, json_file)












