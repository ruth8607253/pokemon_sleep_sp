# イトマル
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()

driver.get("https://www.gamer.com.tw/")
search=driver.find_element(by="name",value="search")
search.send_keys("pokemon sleep")
search.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()