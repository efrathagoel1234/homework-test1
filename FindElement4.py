#targil4
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\hagoel\\downloads\\chromedriver.exe")

source = "https://www.google.com/search?q=google+translate&rlz=1C1JZAP_enIL988IL993&oq=google+translate&aqs=chrome..69i57j0i512j0i433i512j0i131i433i512j0i512l5j0i271.6870j0j7&sourceid=chrome&ie=UTF-8"
driver.get(source)
driver.refresh()
driver.find_element(By.XPATH,'//*[@id="tw-source-text-ta"]').send_keys("Efrat")



#targil5
#Open Youtube web page
#Type a name of a song
#Click on search.
source = "https://www.youtube.com"
driver.get(source)
driver.refresh()
driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys("enemy")
driver.find_element(By,XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button/yt-icon').click()
driver.quit()
