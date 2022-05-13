##Targil number 1

from selenium import webdriver
import time

# browser exposes an executable file
# Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="C:\\Users\\Hagoel\\Downloads\\chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
# get method to launch the URL
driver.get("http://www.walla.co.il/")
print("URL IS", driver.current_url)
Current_URL = driver.current_url
print(Current_URL)
# to refresh the browser
driver.refresh()
# check if the variable and the URL are the same
if (driver.current_url == Current_URL):
    print("Are the same")
# to close the browser
driver.close()

##Targil1 with Firfox
# driver = webdriver.Chrome(executable_path="C:\\Users\\Hagoel\\Downloads\\geckodriver.exe")
# to maximize the browser window
# driver.maximize_window()
# get method to launch the URL
# driver.get("http://www.ynet.co.il/")
# to refresh the browser
# driver.refresh()
# to close the browser
# driver.close()


# Targil 3 - locating elements

driver = webdriver.Chrome(executable_path="C:\\Users\\Hagoel\\Downloads\\chromedriver.exe")
driver.get("C:\\Python\\tip_calc\\index.html")
driver.maximize_window()



driver.close()