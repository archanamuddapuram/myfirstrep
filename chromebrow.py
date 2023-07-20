from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj = Service("/Users/archanamuddappuram/Documents/chromedriver")
driver = webdriver.Chrome(service = service_obj)
driver.maximize_window()
driver.get("http://google.com")
print(driver.title)
print(driver.current_url)
driver.get("http://youtube.com")
driver.back()
driver.close()
