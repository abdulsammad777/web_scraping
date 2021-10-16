# from webwhatsapi import WhatsAPIDriver
# import simon


import pywhatkit as kit
from selenium import webdriver

# kit.search('https://web.whatsapp.com/')


# kit.playonyt("Alan walker")

# kit.help()
# kit.sendwhatmsg("+923054491767", "testing", 17, 37)
kit.sendwhatmsg("+92 313 1211998", "testing", 17, 55)

# driver = webdriver.Chrome()
# send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
# send_button.click()
# kit.sendwhatmsg("+92 320 2665545", "I love studytonight.com!", 15, 18)


# kit.se("+923054491767", "D:\\01PythonMUL\\Docs\\queries.docs", 12, 44)

# from selenium import webdriver
# from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.options import Options
# # from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
#
#
# options = webdriver.ChromeOptions()
# # options.add_argument("user-data-dir=C:\\Users\\Abdul samad\\AppData\\Local\\Google\\Chrome\\Default")
# options.add_argument("user-data-dir= C:\\Users\\Abdul samad\\test")
#
#
# driver = webdriver.Chrome(options=options)
# driver.implicitly_wait(0.5)
#
# # driver = webdriver.Chrome(ChromeDriverManager().install())
#
# driver.get('https://web.whatsapp.com/')
# html_source = driver.page_source
# soup = BeautifulSoup(html_source, 'html.parser')
# divs = soup.find('div', {"class":"_3jid7"})
# # print(divs.attrs["data-ref"])
# # in whatsapp web, qr code is the value of "data-ref" attribute of div element with class "_1pw2F"
#
# # qrCodeFile = driver.find_element_by_xpath('//div[data-ref = "data-ref"])
# name = "Haider Office"
#
# # filepath = input('Enter your filepath (images/video): ')
# filepath = r'D:\Bleedai\Week 2 files\Week 2 files\Media\M2\joker1.png'
#
#
# input('Enter anything after scanning QR code')
#
# user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
# user.click()
#
# attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
# attachment_box.click()
#
# image_box = driver.find_element_by_xpath(
#     '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
# image_box.send_keys(filepath)
#
# sleep(3)
#
# send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
# send_button.click()

