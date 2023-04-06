from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time as t

def nextPage(driver):
    elem = driver.find_element(By.XPATH , "//*[@v-if='pageData.nextq']")
    elem.click()
    
def get_question_detail(elem):
    te = elem.find_element(By.CLASS_NAME, "question").get_attribute("innerHTML")
    return te

def get_answer_detail(elem5):
    try:
        elem2=elem5.find_element(By.CLASS_NAME, "text-center")
        elem3=elem2.find_element(By.TAG_NAME, "Button")
        elem3.click()
        t.sleep(1)
        te = elem5.find_element(By.CLASS_NAME,"options").text
        print()
        spliter=te.split("\n")
        
        ansDict={"A":"1","B":"2","C":"3","D":"4"}
        i=0
        d="ABCD"
        ca="A"
        with open("exp56.html", "a+", encoding="utf-8") as f:
                f.write(str(spliter))
        while i <len(spliter):
            
            if spliter[i] in d :
                if spliter[i+1] ==  'Correct Answer' :
                    ca=spliter[i]
                    ansDict[spliter[i]]=spliter[i+2]
                    i=i+3
                else :
                    ansDict[spliter[i]]=spliter[i+1]
                    i+=2
        return ansDict,ca
    except :
        print("no answer")
        t.sleep(1000)
def get_explanation(elem):
    try :
        elem5 = elem.find_elements(By.TAG_NAME , "Div")
        
        store=""
        for i in elem5:
            # print(i.text)
            x=i.get_attribute("innerHTML")
            if "Explanation" in i.text:
                store=x
        return store
    except :
        print("no explanation")
        return "no explanation"

driver = webdriver.Chrome()

i_ul="https://questions.examside.com/past-years/jee/question/pmatch-list-i-with-list-ii-p-pstyle-typetextcss-jee-main-physics-motion-aqfllelnyaim2mz5"
rt=0
while rt<2:
    driver.get(i_ul)
    elem_it = driver.find_elements(By.CLASS_NAME , "question-component")
    count=len(elem_it)
    print(count)
    rrt=0
    for i in elem_it :
       
        # i=elem_it[tw]
  
        q=get_question_detail(i)
   
        a,c=get_answer_detail(i)
        # elem_it = driver.find_elements(By.CLASS_NAME , "question-component")
        e=get_explanation(i)
        
        with open("exp9.txt", "a+", encoding="utf-8") as f:
            f.write(q)
            f.write("\n")
            f.write(str(a))
            f.write("\n")
            f.write(str(c))
            f.write("\n")
            f.write("\n")
            f.write(e)
            f.write("\n")
            f.write("\n")
            f.write("\n")
        # print("checker")
        # # elem_it = driver.find_elements(By.CLASS_NAME , "question-component")
    elem = driver.find_element(By.XPATH , "//*[@v-if='pageData.nextq']")
    href=elem.get_attribute("href")
    i_ul=href
    print(href)
    # t.sleep(50)
driver.close()

    

