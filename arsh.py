from selenium import webdriver
from PIL import Image
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
import base64
from selenium import webdriver
import time as t
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://cellxgene.cziscience.com/e/b74100ea-1a1a-486a-9cad-70ae44150935.cxg/")
t.sleep(10)
action = ActionChains(driver)

driver2 = webdriver.Chrome()
driver2.get("https://mybyways.com/blog/convert-svg-to-png-using-your-browser")
action2=ActionChains(driver2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# t.sleep(5)
# driver.save_screenshot("shot.png")
canvas = driver.find_element(By.XPATH, '//*[@id="histogram_Number_of_UMIs_svg"]')
htm=str(canvas.get_attribute('outerHTML'))
htm=htm.replace('histogram_Number_of_UMIs_svg','try2')


elem = driver2.find_element(By.XPATH, '//*[@id="t"]')
elem3 = driver2.find_element(By.XPATH, '//*[@id="l"]')

# action2.move_to_element(elem).perform()

elem.send_keys(Keys.RETURN)
elem.send_keys(htm)
elem3.send_keys(Keys.RETURN)
# elem3.click()
elem2 = driver2.find_element(By.XPATH, '//*[@id="s"]')
elem2.send_keys(Keys.RETURN)
# elem2.click()
t.sleep(25)
# location = canvas.location
# size = canvas.size
# x = location['x']
# y = location['y']
# w = size['width']
# h = size['height']
# width = x + 1.4*w
# height = y + h*1.2

# im = Image.open('shot.png')
# im = im.crop((int(x*1.2), int(y*3.5), int(width), int(height)))
# im.save('image.png')
