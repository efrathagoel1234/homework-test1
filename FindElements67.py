#targil6
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\hagoel\\downloads\\chromedriver.exe")

source = "https://translate.google.com/"
driver.get(source)
driver.refresh()
driver.find_element(By.XPATH,'/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys("Efrat")
Print_Source = driver.find_element(By.XPATH,'/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').get_attribute('value')
#Need still to find other methods
#Print_Source = driver.find_element(By.ID('tw-source-text'))

print ("the value in the field is ",Print_Source )
driver.quit()



