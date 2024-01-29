from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://open.spotify.com/"
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
# chrome_options.binary_location = ".//CFT driver/chromedriver-win64/chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(url)
driver.maximize_window()

