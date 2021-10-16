from selenium.webdriver.common.by import By
from selenium import webdriver
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

chromeOptions.add_argument('--headless')
chromeOptions.add_argument('--no-sandbox')
chromeOptions.add_argument('--disable-dev-shm-usage')
import json
import os
import time
import logging



driver = webdriver.Chrome(options=chromeOptions)
# driver = webdriver.Chrome(options=chromeOptions)
# executor_url = driver.command_executor._url
# session_id = driver.session_id
driver.implicitly_wait(0.5)
# driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
# driver.close()   # this prevents the dummy browser

def Login(email, password):
    # driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe')
    location = 'https://'+f'{email}'+':'+f'{password}'+'@linkwonderland.pro/admin/list-click-rotators.php'
    driver.get(location)


def get_status():
    try:
        driver.execute(Command.STATUS)
        return "Alive"
    except:
        return "Dead"

def checkLogin():
    global driver
    if get_status() == "Dead":
        driver = webdriver.Chrome(options=chromeOptions)
        Login('jarellano@prodigiousworksllc.com', 'gh453fgh4NG')
    get_current_url = driver.current_url
    if get_current_url == 'https://jarellano%40prodigiousworksllc.com:gh453fgh4NG@linkwonderland.pro/admin/list-click-rotators.php':
        pass
    else:
        Login('jarellano@prodigiousworksllc.com', 'gh453fgh4NG')

def get_sixtieth_value():
    driver.find_element_by_xpath(
        ".//div//select[@name='rotator_links_datatable_length']/option[@value='100']").click()
    Table = driver.find_element(By.XPATH, '//div//table[@class="table table-striped table-bordered table-hover dataTable no-footer"]')
    # TableRows = Table.find_element_by_xpath("//table//tbody[@type='text']")
    TableRows = Table.find_elements_by_xpath(".//tbody//tr")
    table_data_60th = TableRows[59].find_elements_by_xpath(".//td")
    table_data_10th = TableRows[9].find_elements_by_xpath(".//td")

    value_60th = table_data_60th[5].text
    value_10th = table_data_10th[5].text

    return value_60th, value_10th

def UpdateJsonFile(sixteeth_data, link_name, current_value_60th, current_value_10th):
    if not os.path.isfile('data.json'):
        with open('data.json', 'a'):
            pass
    filesize = os.path.getsize("data.json")
    if filesize == 0:
        with open("data.json", 'r+') as json_file:
            json.dump(sixteeth_data, json_file)
            return True
    else:
        with open("data.json", 'r+') as json_file:
            try:
                json_from_file = json.load(json_file)
            except:
                json_from_file = json_file.seek(0)
            if link_name in json_from_file.keys():
                previous_value_60th = json_from_file[link_name]['60']
                previous_value_10th = json_from_file[link_name]['10']
                if previous_value_60th != current_value_60th or previous_value_10th != current_value_10th:
                    json_from_file[link_name]['60'] = current_value_60th
                    json_from_file[link_name]['10'] = current_value_10th
                    json_file.truncate(0)
                    json_file.seek(0)
                    json.dump(json_from_file, json_file)
                    # new_json = json.dumps(json_from_file)
                    # json.dump(new_json, json_file)
                    return True
                else:
                    return False
            else:
                json_from_file[link_name] = sixteeth_data.get(link_name)
                json_file.truncate(0)
                json_file.seek(0)
                json.dump(json_from_file, json_file)
                return True





def comparesixteethvalue(link_name, title_urls):
    value_changing_data = {}
    link_name_url = title_urls[link_name]
    name_id = link_name_url.split('id=')
    id_number = name_id[1]
    click_on_links = "https://linkwonderland.pro/admin/list-click-rotator-links.php?id=" + f"{id_number}"
    # click_on_links = driver.find_element(By.XPATH, '//a[@href="' + click_on_links + '"]')
    # click_on_links.click()https://linkwonderland.pro/admin/list-click-rotator-links.php?id=5
    driver.get(click_on_links)
    value_60th, value_10th = get_sixtieth_value()
    value_changing_data[link_name] = {}
    value_changing_data[link_name]['60'] = int(value_60th)
    value_changing_data[link_name]['10'] = int(value_10th)
    Decision_For_Change = UpdateJsonFile(value_changing_data, link_name, int(value_60th), int(value_10th))
    # Decision_For_Change = UpdateJsonFile(sixteeth_data, link_name, 3)
    if Decision_For_Change is True:
        return True
    else:
        return False


def UpdateAllLinks(sheetUrls,title, links_dict):
    len_ = len(sheetUrls) + 1
    for index in range(1, len_):
        if index < 10:
            link_text = "000" + str(index)
        elif index > 10 and index < 100:
            link_text = "00" + str(index)
        elif index == 100:
            link_text = "0" + str(index)
        try:
            link_url = links_dict[title][link_text]
        except:
            logging.warning(f'--Link NUmber--{link_text} not found for {title}')
        try:
            driver.get(link_url)
            input_tag = driver.find_element_by_id('link_url')
            input_tag.clear()
            input_tag.send_keys(sheetUrls[index-1])
            save_button = driver.find_element_by_xpath('//div//button[@type="submit"]')
            save_button.click()
            time.sleep(1)
            driver.back()
        except:
            logging.warning(f'--Update Error-- Detected for {title} on link number {link_text}')

        if(index == 50):
            driver.quit()
            time.sleep(5)
            checkLogin()
    driver.quit()

def close_driver():
    global driver
    if get_status() != "Dead":
        driver.quit()
