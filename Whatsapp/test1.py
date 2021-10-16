from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:\\Users\\Abdul samad\\AppData\\Local\\Google\\Chrome\\User Data\\Default") # change to profile path
# chrome_options.add_argument('--profile-directory=Profile 1')

driver = webdriver.Chrome(options=chrome_options) # change the executable_path too
time.sleep(2)

driver.get('https://web.whatsapp.com/')



# driver = webdriver.Chrome(ChromeDriverManager().install())

name = "Haider Office"

# filepath = input('Enter your filepath (images/video): ')
filepath = r'D:\01PythonMUL\Docs\bioinformatics.txt'


input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
attachment_box.click()

# image_box = driver.find_element_by_xpath(
#     '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box = driver.find_element_by_xpath(
    '//input[@accept="*"]')
image_box.send_keys(filepath)


send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
send_button.click()


