from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time as t
import json

ansDict={"A":"1","B":"2","C":"3","D":"4"}


def nextPage(driver):
    elem = driver.find_element(By.XPATH , "//*[@v-if='pageData.nextq']")
    elem.click()
    
def get_question_detail(elem):
    te = elem.find_element(By.CLASS_NAME, "question").get_attribute("innerHTML")
    return te

def get_answer_detail(elem5):
    
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
        temp=""
        ans="A"
        while i <len(spliter):
            

            if spliter[i] in d :
                ansDict[ans]=temp
                ans=spliter[i]
                temp=""

                if i +1 < len(spliter):
                    if spliter[i+1] ==  'Correct Answer' :
                      ca=spliter[i]
                      i+=1
                    
                
                
                i+=1
            else:
                temp+=spliter[i]
                i+=1
            print(spliter)
        return ansDict,ca
   
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

input_url="https://questions.examside.com/past-years/jee/question/pmatch-list-i-with-list-ii-p-pstyle-typetextcss-jee-main-physics-motion-aqfllelnyaim2mz5"
rt=0
dic_json=[]
while rt<10:
    driver.get(input_url)
    elem_it = driver.find_elements(By.CLASS_NAME , "question-component")
    count=len(elem_it)
    print(rt)
    rt+=1
    for i in elem_it :
       
        # i=elem_it[tw]
  
        q=get_question_detail(i)
   
        a,c=get_answer_detail(i)
        # elem_it = driver.find_elements(By.CLASS_NAME , "question-component")
        e=get_explanation(i)
        
        d_t={}
        d_t["question"]=q    
    
        d_t["option1"]=a["A"]
        d_t["option2"]=a["B"]
        d_t["option3"]=a["C"]
        d_t["option4"]=a["D"]
        d_t["correct"]=ansDict[c]    
            
        d_t["explanation"]=e

        dic_json+=[d_t]
            
            
            
        # print("checker")
        # # elem_it = driver.find_elements(By.CLASS_NAME , "question-component")
    try:
        elem = driver.find_element(By.XPATH , "//*[@v-if='pageData.nextq']")
        href=elem.get_attribute("href")
        print(href)
        input_url=href
    except:
        break
json_object = json.dumps(dic_json, indent=4)
with open("share.json","w") as f:
    f.write(json_object)

    # t.sleep(50)
driver.close()

    

