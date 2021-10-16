from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select

import httplib2
import socket
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.command import Command
chromeOptions = Options()
# chromeOptions.add_argument("--start-maximized")
chromeOptions.add_experimental_option("detach", True)
chromeOptions.add_experimental_option('useAutomationExtension', False)
import json
import os
import time
import logging

driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe')
driver.implicitly_wait(0.5)

def open_site(url):
    driver.get(url)

def return_Reviews_list():
    Reviews_dic = {}

    # select = Select(driver.find_element_by_xpath("//select[@id='star-count-dropdown']"))
    # select.select_by_visible_text('All stars')

    all_star_review = driver.find_element_by_xpath("//div[@class='a-row a-spacing-base a-size-base']/span").text

    select = Select(driver.find_element_by_xpath("//select[@id='star-count-dropdown']"))
    select.select_by_visible_text('5 star only')

    time.sleep(2)

    five_star_review = driver.find_element_by_xpath("//div[@class='a-row a-spacing-base a-size-base']/span").text


    select = Select(driver.find_element_by_xpath("//select[@id='star-count-dropdown']"))
    select.select_by_visible_text('4 star only')

    time.sleep(2)

    four_star_review = driver.find_element_by_xpath("//div[@class='a-row a-spacing-base a-size-base']/span").text


    select = Select(driver.find_element_by_xpath("//select[@id='star-count-dropdown']"))
    select.select_by_visible_text('3 star only')

    time.sleep(2)

    three_star_review = driver.find_element_by_xpath("//div[@class='a-row a-spacing-base a-size-base']/span").text


    select = Select(driver.find_element_by_xpath("//select[@id='star-count-dropdown']"))
    select.select_by_visible_text('2 star only')

    time.sleep(2)

    two_star_review = driver.find_element_by_xpath("//div[@class='a-row a-spacing-base a-size-base']/span").text


    select = Select(driver.find_element_by_xpath("//select[@id='star-count-dropdown']"))
    select.select_by_visible_text('1 star only')

    time.sleep(2)

    one_star_review = driver.find_element_by_xpath("//div[@class='a-row a-spacing-base a-size-base']/span").text


    Reviews_dic['All stars'] = all_star_review
    Reviews_dic['5 star only'] = five_star_review
    Reviews_dic['4 star only'] = four_star_review
    Reviews_dic['3 star only'] = three_star_review
    Reviews_dic['2 star only'] = two_star_review
    Reviews_dic['1 star only'] = one_star_review

    return Reviews_dic





open_site('https://www.amazon.com/product-reviews/B08FZFQM27')
print(return_Reviews_list())





