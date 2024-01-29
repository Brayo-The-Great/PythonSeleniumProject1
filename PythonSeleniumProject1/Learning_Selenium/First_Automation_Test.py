from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_name("username").send_keys("Admin")
driver.find_element_by_name("password").send_keys("admin123")
driver.find_element_by_name("oxd-button").click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()