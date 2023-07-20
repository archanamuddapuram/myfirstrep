from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/archanamuddappuram/Documents/chromedriver")
driver = webdriver.Chrome(service = service_obj)
driver.get("http://google.com")
driver.maximize_window()
driver.find_element(By.ID,"APjFqb").send_keys("archana")
driver.find_element(By.XPATH,"//input[@name='btnK']").click()


