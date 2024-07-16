import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

service_obj = Service("msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)
driver.get("https://rahulshettyacademy.com")
time.sleep(2)
driver.maximize_window()
print(driver.title)