from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time as t


driver = webdriver.Chrome()
driver.get("https://questions.examside.com/past-years/jee/question/pmatch-list-i-with-list-ii-p-pstyle-typetextcss-jee-main-physics-motion-aqfllelnyaim2mz5")

elem = driver.find_elements(By.CLASS_NAME , "question-component")

for i in elem:
    print(i.text)
    print()
    print()
