# Test Case
#------------------
# 1) Open Web Browser(Chrome/Firefox/Edge)
# 2) Open URL https://opensource-demo.orangehrmlive.com/
# 3) Enter username (Admin).
# 4) Enter password (admin123)
# 5) Click on log in
# 6) Capture title on the home page. (Actual title)
# 7) Verify title of the page: OrangeHRM (Expected)
# 8) Close browser


# Selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)

url = 'https://opensource-demo.orangehrmlive.com/'
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(url)
driver.maximize_window()

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