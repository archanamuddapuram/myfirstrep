from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/archanamuddappuram/Documents/chromedriver")
driver = webdriver.Chrome(service = service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"email").send_keys("arch.m1183@gmail.com")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.NAME,"name").send_keys("archana")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
#con1=driver.find_element(By.XPATH, "//div[@class = 'alert-success']").text
#print(con1)
abc = driver.find_element(By.CLASS_NAME, "alert-success").text
print(abc)
assert "Success" in abc