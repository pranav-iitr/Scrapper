from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://questions.examside.com/past-years/jee/question/pmatch-list-i-with-list-ii-p-pstyle-typetextcss-jee-main-physics-motion-aqfllelnyaim2mz5")
elem = driver.find_element(By.XPATH , "//*[@v-if='pageData.nextq']")
elem.click()
t.sleep(5)
elem = driver.find_element(By.XPATH , "//*[@v-if='pageData.nextq']")
elem.click()
t.sleep(5)
elem = driver.find_element(By.XPATH , "//*[@v-if='pageData.nextq']")
elem.click()
t.sleep(5)
# a = open("exp5.html", "w")
# elem2=elem.find_element(By.CLASS_NAME, "text-center")
# elem3=elem2.find_element(By.TAG_NAME, "Button")
# elem3.click()

# elem5 = elem.find_elements(By.TAG_NAME , "Div")
driver.close()