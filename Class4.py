from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('C:/Users/hagoel/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('C:/Users/hagoel/Downloads/tip')
driver.find_element(By.XPATH,"/html/body").send_keys("Doron")