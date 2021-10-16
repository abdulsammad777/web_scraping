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

def UpdateAllLinks(title, main_dict):
    for index in range(1, 101):
        if index < 10:
            link_text = "000" + str(index)
        elif index > 10 and index < 100:
            link_text = "00" + str(index)
        elif index == 100:
            link_text = "0" + str(index)

        link_href = driver.find_element(By.XPATH, '//a[text()="' + link_text + '"]').get_attribute("href")
        main_dict[title][link_text]=link_href


for link_name in lst:
    main_dict = {}
    UpdateAllLinks(link_name, main_dict)

with open("title_urls.json", 'w') as json_file:
    json.dump(dict, json_file)












