# saving

import pickle
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

# login code
# driver.add_cookie({"name": "foo", "value": "bar"})
cookies = driver.get_cookies()
# for cookie in cookies:
#     print(cookie)
pickle.dump(cookies , open("Cookies.pkl","wb"))

# loading
# import pickle
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://web.whatsapp.com/')
# for cookie in pickle.load(open("Cookies.pkl", "rb")):
#     driver.add_cookie(cookie)
