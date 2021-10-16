# 1. Dealing with forms and dropdown menus

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

# 1. a. Locating the elements in the form

driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://www.pluralsight.com/buy?requestId=70a5a334-2be9-4158-a524-f12eb3aac30e&priceOptionId=3424225b-adf2-4e9b-a094-45d31de7f260&legacyTrackingId=IND-M-PLUS&planId=Individual+plan&quantity=1&analyticsStep=1")

# web driver wait
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "firstName")))


# first name
first_name = driver.find_element_by_name("firstName")
first_name.clear()
first_name.send_keys("John")

# last name
last_name = driver.find_element_by_name("lastName")
last_name.clear()
last_name.send_keys("Doe")

# email
email = driver.find_element_by_name("email")
email.clear()
email.send_keys("john_is_a_doe_6483@gmail.com")

# confirmation email
conf_email = driver.find_element_by_name("confirmationEmail")
conf_email.clear()
conf_email.send_keys("john_is_a_doe_6483@gmail.com")


# 1. b. Dropdown menu, checkbox & submit

# country of residence
time.sleep(2)
country_element = driver.find_element_by_xpath("//select[@data-test='country']")
all_options = country_element.find_elements_by_tag_name("option")

for option in all_options:
    if option.get_attribute("value") == "US":
        option.click()

# checkboxes
time.sleep(1)
checkbox = driver.find_element_by_xpath("//div[@role='checkbox']")
checkbox.click()

# submit button
submit_ele = driver.find_element_by_xpath("//button[@data-test='submitButton']")
time.sleep(2)
submit_ele.click()

driver.quit()


# 2. Handling iFrames

# switch to iframe by name
driver.switch_to_frame("frameName")

# switch to parent frame
driver.switch_to_default_content()

# 3. Handling popups
popup = driver.switch_to_alert()