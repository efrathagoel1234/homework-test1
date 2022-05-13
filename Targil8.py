#Targil8
#Open Chrome browser on any webpage.
#Delete all cookies from browser.
#Make sure all cookies are deleted by printing all cookies stored in the browser.


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


from selenium.webdriver.common.by import By
import time
import sys
driver = webdriver.Chrome(executable_path="C:\\Users\\hagoel\\downloads\\chromedriver.exe")
driver.get("http://www.walla.co.il")
driver.delete_all_cookies()
lst = driver.get_cookies()
for cookie in lst:
    print(cookie)

driver.quit()