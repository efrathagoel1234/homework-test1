from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\\hagoel\\downloads\\chromedriver.exe")
driver.get("C:\\Users\\hagoel\\AppData\\Local\\Temp\\Temp1_tip_calc.zip\\tip_calc\\index.html")
driver.find_element(By.XPATH,'//*[@id="billamt"]').send_keys(100)
driver.find_element(By.XPATH,'//*[@id="serviceQual"]/option[2]'.click())


print("passed value")
driver.maximize_window()
driver.refresh()
input()
driver.close()



#source = "https://github.com/"
#my_xpath = '/html/body/div[4]/div[2]/div[2]/div/div[1]/img'
#driver = webdriver.Chrome()
#driver.get(source)
#x = driver.find_element_by_xpath(my_xpath)
#y = driver.find_element(By.XPATH, my_xpath)
#driver.quit()