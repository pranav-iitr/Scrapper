import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
import base64
from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.get("https://cellxgene.cziscience.com/e/b74100ea-1a1a-486a-9cad-70ae44150935.cxg/")
t.sleep(10)
canvas = driver.find_element(By.XPATH, '//*[@id="graph-wrapper"]/canvas')

# get the canvas as a PNG base64 string
canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(22);", canvas)

# decode
canvas_png = base64.b64decode(canvas_base64)

# save to a file
with open(r"canvas.png", 'wb') as f:
    f.write(canvas_png)
