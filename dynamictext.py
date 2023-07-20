import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service("/Users/archanamuddappuram/Documents/chromedriver")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(3)
allcon=driver.find_element(By.CSS_SELECTOR,"li[class = 'ui-menu-item']")
print(len(allcon))




