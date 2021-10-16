# importing required libraries

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# adding options
chromeOptions = Options()
chromeOptions.add_argument("--kiosk")


# opening the webpage

driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe', options=chromeOptions)

driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

# web driver wait
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "email_create")))


# email submit

dest_search = driver.find_element_by_name("email_create")
dest_search.clear()
dest_search.send_keys("test_user1@live.com")

# clicking on the 'create an account' button
submit_button = driver.find_element_by_xpath("//button[@id='SubmitCreate']")
submit_button.click()

# Filling in your information
# 1st Section

# radio button

radio_button_male = driver.find_element_by_id("id_gender1")
radio_button_male.click()

# account info

first_name = driver.find_element_by_id("customer_firstname")
first_name.send_keys("Test1")

last_name = driver.find_element_by_id("customer_lastname")
last_name.send_keys("User1")

password = driver.find_element_by_id("passwd")
password.send_keys("password123")


# date of birth
dob_date = Select(driver.find_element_by_id("days"))
dob_date.select_by_value('10')

dob_month = Select(driver.find_element_by_id("months"))
dob_month.select_by_visible_text('May ')

dob_year = Select(driver.find_element_by_id("years"))
dob_year.select_by_value('2000')


# checkbox

newsletter = driver.find_element_by_id("newsletter")
newsletter.click()

# 2nd section

first_name_2 = driver.find_element_by_id("firstname")
first_name_2.send_keys("Test")

last_name_2 = driver.find_element_by_id("lastname")
last_name_2.send_keys("User")

address = driver.find_element_by_id("address1")
address.send_keys("Some Address, Po Box - 1111")

city = driver.find_element_by_id("city")
city.send_keys("Greatest City")

state = Select(driver.find_element_by_id("id_state"))
state.select_by_visible_text("Alabama")

post_code = driver.find_element_by_id("postcode")
post_code.send_keys("00000")

mob_phone = driver.find_element_by_id("phone_mobile")
mob_phone.send_keys("1111111111")

alias_addr = driver.find_element_by_id("alias")
alias_addr.send_keys("Home")

reg_button = driver.find_element_by_xpath("//button[@id='submitAccount']").click()

# closing the current window
driver.quit()