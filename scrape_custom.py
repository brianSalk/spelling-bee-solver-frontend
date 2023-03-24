import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

for hex in driver.find_elements(By.CLASS_NAME, 'hex'):
    print(hex.text)
