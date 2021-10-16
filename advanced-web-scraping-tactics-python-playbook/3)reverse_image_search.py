from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

# adding options
chromeOptions = Options()
chromeOptions.add_argument("--kiosk")

# opening the webpage

#driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe', options=chromeOptions)

driver = webdriver.Chrome(executable_path='/snap/chromium/1753/usr/lib/chromium-browser/chromedriver', options=chromeOptions)

driver.get("https://tineye.com/")

# file upload
file_upload = driver.find_element_by_name("image")
#file_upload.send_keys("/Users/pratheerth/Downloads/logo.jpg")

# page source
page_source_overview = driver.page_source
doc = BeautifulSoup(page_source_overview, "html.parser")

# grab the site names
site_names = doc.find_all(class_="match")
print(site_names)

for site in site_names:
    print(site.a.string)

driver.quit()
