#Targil7
#Open Chrome browser on Facebook website https://www.facebook.com/
#Login into Facebook (No need to send me credentials).


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import sys
driver = webdriver.Chrome(executable_path="C:\\Users\\hagoel\\downloads\\chromedriver.exe")
try:
    source = "https://facebook.com/"
    driver.get(source)
    driver.refresh()
    driver.find_element(By.ID,"email").send_keys("efrathagoel@gmail.com")
    driver.find_element(By.ID,"pass").send_keys("FirstFaceBook123")
    driver.find_element(By.ID,"u_0_d_XF").click()
   #driver.find_element(By,XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[3]/button').click()
    #submit.send_keys(Keys.enter)


#class="fb-login-button"

except NoSuchElementException:
    print("no such element")
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise


driver.quit()