# イトマル 圓絲蛛
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver=webdriver.Chrome()

#打開頁面
driver.get("https://www.gamer.com.tw/")
#搜尋
search=driver.find_element(By.NAME,"search")
#搜尋內容
search.clear()
search.send_keys("pokemon sleep 寶可夢sp")
search.send_keys(Keys.RETURN)
driver.implicitly_wait(2)
# 標題的class name
titles=driver.find_elements(By.CLASS_NAME,"gs-title")
for t in titles:
	title=t.text
#點擊搜尋標題
link=driver.find_elements(By.LINK_TEXT,f"{title}")
for l in link:
    l.click()
text=driver.find_elements(By.TAG_NAME,"sp")
#返回搜尋頁面
driver.back()

time.sleep(5)
driver.quit()