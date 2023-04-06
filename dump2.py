from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://questions.examside.com/past-years/jee/question/pmatch-list-i-with-list-ii-p-pstyle-typetextcss-jee-main-physics-motion-aqfllelnyaim2mz5")
# assert "Python" in driver.title
elem = driver.find_element(By.CLASS_NAME , "question-component")
# a = open("exp5.html", "w")
elem2=elem.find_element(By.CLASS_NAME, "text-center")
elem3=elem2.find_element(By.TAG_NAME, "Button")
elem3.click()


elem5 = elem.find_elements(By.TAG_NAME , "Div")
# with open("exp7.html", "w", encoding="utf-8") as f:
#     te=elem.get_attribute("innerHTML")
#     print(len(elem5))
#     f.write(te)

for i in elem5:
    x=i.get_attribute("innerHTML")
    if "Explanation" in i.text:
        print("ok")
        with open("exp9.html", "w", encoding="utf-8") as f:
             f.write(x)


#getting the text of the question
# te = elem5.find_element(By.CLASS_NAME, "question").get_attribute("innerHTML")
# with open("exp5.html", "w", encoding="utf-8") as f:
#     f.write(te)


#get answer
# te = elem5.find_element(By.CLASS_NAME,"options").text
# print(te)
# with open("exp6.html", "w", encoding="utf-8") as f:
#     f.write(te)

# spliter=te.split("\n")
# print(spliter)
# ansDict={"A":"1","B":"2","C":"3","D":"4"}
# i=0
# d="ABCD"
# ca="A"
# while i <len(spliter) :
#     if spliter[i] in d :
#         if spliter[i+1] ==  'Correct Answer' :
#             ca=spliter[i]
#             ansDict[spliter[i]]=spliter[i+2]
#             i=i+3
#         else :
#             ansDict[spliter[i]]=spliter[i+1]
#             i+=2
# print(ansDict,ca)

# t.sleep(2)

# driver.close()
