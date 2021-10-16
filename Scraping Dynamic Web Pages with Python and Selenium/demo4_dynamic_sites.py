"""---------lack of bot access--------------
websites are free to choose whether theu allow agent or bots.
always check robots.txt and terms of service.
www.website name/robots.txt
CAPTCHA's (Completely Automated Public Turing test)
"""

'''---------Frequently structural changes---------------

outsource the project to the service provoder soo that he can keep an eye on the changes.
'''

"""------------Getting block / banned--------------------

Unnatuarally high requets from the the same IP maycause the server to block that IP.

websites can also make use of Honeypot traps, Honeypots are mean to detect crawlers or scrapers,
These are the hidden links hidden not visible to users and can be extracted by scrapers.Once they visit your may be
flagged for investigation for further investigation or may be instantly blocked.
"""


""" --------------------Data Quality--------------------------------
write test cases to test whether the scrapers extract the data meets the data quality or not."""

"""-----------------Overcoming Challenges and Increasing Efficiency--------------------
Avoid Loading Images
Employ Disk Cache
"""


# Navigation
# importing required packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# adding options on chrome
chromeOptions = Options()
chromeOptions.add_argument("--kiosk")


# navigating to the premier league site

driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://www.premierleague.com/")

# clicking on the players tab
players_ele = driver.find_element_by_link_text("Players").click()

# searching for wayne rooney
# web driver wait
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "search-input")))

search_ele = driver.find_element_by_id("search-input")
search_ele.send_keys("Wayne Rooney")
search_ele.send_keys(Keys.RETURN)

# clicking on wayne rooney
# implicitly_wait tells driver to wait for no reason but explicit_wait tells to wait until specific condition meets.
driver.implicitly_wait(3)
click_wayne = driver.find_element_by_xpath("//img[@data-player='p13017']").click()

page_source_overview = driver.page_source

# Beautiful Soup

from bs4 import BeautifulSoup

# loading page source info
soup = BeautifulSoup(page_source_overview, 'lxml')

# locating the titles
title_finder = soup.find_all("span", class_="title")

print(title_finder)

print(10*"-" + "These are the latest news headlines about Wayne Rooney" + 10*"-" + "\n")
for title in title_finder:
    print(title.string)

    # stats button element
time.sleep(1)
wayne_stats = driver.find_element_by_xpath("//a[@href='stats']").click()

page_source_stats = driver.page_source

soup = BeautifulSoup(page_source_stats, "lxml")

# locating all the stats
stat_finder = soup.find_all("span", class_="allStatContainer")

print(stat_finder)

print(10*"-" + "Wayne Rooney Stats" + 10*"-" + "\n")
for stat in stat_finder:
    print(stat["data-stat"] +  " - " + stat.string)
