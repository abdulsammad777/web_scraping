
"""xpath = //tagname[@attribute="value"]
// = current node
tagname = selecting correct tag name ,input/div
@ = selecting attribute
attribute = attribute name
value = attribute value"""

from selenium import webdriver
# importing required library
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
# chromeOptions.add_argument("--kiosk")
# driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe')
# driver = webdriver.Chrome(options=chromeOptions)

# driver.get("https://app.pluralsight.com/")
#
# # Locating elements by name
# ele = driver.find_element_by_name("q")
#
# time.sleep()
# ele.clear()
# ele.send_keys('Abdul Sammad')
# ele.send_keys(Keys.RETURN)
#
# driver.quit()

# Locating elements by ID

driver=webdriver.Chrome(options=chromeOptions)
driver.get("https://www.python.org/")


ele = driver.find_element_by_id("id-search-field")
time.sleep(1)
ele.clear()
ele.send_keys("lists")
ele.send_keys(Keys.RETURN)

driver.quit()

# Locating elements by link text

driver=webdriver.Chrome(options=chromeOptions)
driver.get("https://www.pluralsight.com/")

ele = driver.find_element_by_name("q")
time.sleep(1)
ele.clear()
ele.send_keys("Abdul Sammad")
# ele.send_keys("Pratheerth Padman")
ele.send_keys(Keys.RETURN)


ele_link = driver.find_element_by_partial_link_text("Building Image")
time.sleep(1)
ele_link.click()

driver.quit()

# Locating elements by CSS Selector
driver=webdriver.Chrome(options=chromeOptions)
driver.get("https://www.pluralsight.com/")


ele = driver.find_element_by_css_selector("input.header_search--input")
time.sleep(1)
ele.clear()
ele.send_keys("Pratheerth Padman")
ele.send_keys(Keys.RETURN)

driver.quit()

# Locating elements by XPath
driver=webdriver.Chrome(options=chromeOptions)
driver.get("https://www.pluralsight.com/")


ele = driver.find_element_by_xpath("//input[@name='q']")
time.sleep(1)
ele.clear()
ele.send_keys("Pratheerth Padman")
ele.send_keys(Keys.RETURN)
driver.quit()




