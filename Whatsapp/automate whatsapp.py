from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
user_profile_path="C:\\Users\\Abdul samad\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome( executable_path="chromedriver", chrome_options=options)
# driver.get( "https://api.WhatsApp.com/send?phone={}".format("Haider Office")

# driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')

options = webdriver.ChromeOptions()
# options = Options()
options.add_argument(user_profile_path)
# options.add_argument("--user-data-dir=chrome-data")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)

# options.add_argument("user-data-dir=C:\\Users\\Abdul samad\\AppData\\Local\\Google\\Chrome\\Default")


driver = webdriver.Chrome(options=options)
driver.implicitly_wait(0.5)
# driver.maximize_window()
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

sleep(3)

send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
send_button.click()

