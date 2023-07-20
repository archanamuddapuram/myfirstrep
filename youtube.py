from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("/Users/archanamuddappuram/Documents/chromedriver")
driver = webdriver.Chrome(service = service_obj)
driver.get("http://youtube.com")
driver.find_element(By.NAME,"search_query").send_keys("telugu movies")
driver.find_element(By.XPATH,"//button[@id='search-icon-legacy']").click()
driver.find_element(By.XPATH,"//button[@aria-label='Search filters']").click()
