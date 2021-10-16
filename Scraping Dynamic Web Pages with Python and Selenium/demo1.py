from selenium import webdriver

# driver = webdriver.chrome()
# driver.get("https://app.pluralsight.com/")

# driver.quit()

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-error")
options.add_argument("--incognito")
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://app.pluralsight.com/")
