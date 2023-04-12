from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time as t
from selenium.webdriver import ActionChains
from PIL import Image
def get_img(canvas,driver ,name):
    # canvas = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]')

    location = canvas.location
    size = canvas.size

    driver.save_screenshot("shot.png")

    x = location['x']
    y = location['y']
    w = size['width']
    h = size['height']
    width = x + 1.4*w
    height = y + h*1.2

    im = Image.open('shot.png')
    im = im.crop((int(x*1.2), int(y*3.5), int(width), int(height)))
    im.save(name+'.png')

def get_png(htm,name):
    driver2.get("https://mybyways.com/blog/convert-svg-to-png-using-your-browser")
    
    htm=htm.replace('histogram_Number_of_UMIs_svg',name)
    htm=htm.replace('histogram_Genes_detected_svg',name)
    htm=htm.replace('histogram_Fraction_mitochrondrial_UMIs_svg',name)

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
    t.sleep(3)


driver = webdriver.Chrome()
action = ActionChains(driver)
driver2 = webdriver.Chrome()
driver2.get("https://mybyways.com/blog/convert-svg-to-png-using-your-browser")
impl = ["Transcription factor EB", "Brain-specific angiogenesis inhibitor-1",
        "Multiple epidermal growth factor-like domains 10", "Mertk", "C9ORF72", "PINK1", "PARKIN", "OPTN", "TBK1 kinase"]




for i in impl:
    t.sleep(5)

    driver.get(
        "https://cellxgene.cziscience.com/e/b74100ea-1a1a-486a-9cad-70ae44150935.cxg/")
    t.sleep(10)
    elem = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div/div[1]/div/div/div/div/input')
    action.move_to_element(elem).click().perform()
    elem.send_keys(i)
    elem.send_keys(Keys.RETURN)
    t.sleep(10)
    elem = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div/div[2]/div/div/button')
    action.move_to_element(elem).click().perform()
    t.sleep(2)
    action.send_keys(i)
    action.send_keys("CDhkvivgium3D")
    t.sleep(2)
    action.send_keys(Keys.RETURN)
    print("done")
    t.sleep(2)
    elem = driver.find_element(By.XPATH, '//*[@id="category-select-Braak stage"]')
    action.move_to_element(elem).click().perform()
    elem = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div/div[1]/div[9]/div[1]/div[1]/span')
    action.move_to_element(elem).click().perform()


    # elem = driver.find_element(
    #     By.XPATH, '//*[@id="value-toggle-checkbox-Braak stage-Braak 0"]')
    # action.move_to_element(elem).click().perform()
    # elem = driver.find_element(
    #     By.XPATH, '//*[@id="value-toggle-checkbox-Braak stage-Braak II"]')
    # action.move_to_element(elem).click().perform()
    # elem = driver.find_element(
    #     By.XPATH, '//*[@id="value-toggle-checkbox-Braak stage-Braak III"]')
    # action.move_to_element(elem).click().perform()
    # elem = driver.find_element(
    #     By.XPATH, '//*[@id="value-toggle-checkbox-Braak stage-Braak IV"]')
    # action.move_to_element(elem).click().perform()
    # elem = driver.find_element(
    #     By.XPATH, '//*[@id="value-toggle-checkbox-Braak stage-Braak V"]')
    # action.move_to_element(elem).click().perform()
    # elem = driver.find_element(
    #     By.XPATH, '//*[@id="value-toggle-checkbox-Braak stage-Braak VI"]')
    # action.move_to_element(elem).click().perform()

    url_img1='//*[@id="histogram_Number_of_UMIs_svg"]'
    url_img2='//*[@id="histogram_Genes_detected_svg"]'
    url_img3='//*[@id="histogram_Fraction_mitochrondrial_UMIs_svg"]'
    

    elem = driver.find_element(
        By.XPATH, '//*[@id="value-toggle-checkbox-Braak stage-Braak 0"]')
    

    action.move_to_element(elem).click().perform()
    get_img(driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]'),driver,i+"_Braak_0")
  

    svg1=str(driver.find_element(By.XPATH, '//*[@id="histogram_Number_of_UMIs_svg"]').get_attribute('outerHTML'))
    svg2=str(driver.find_element(By.XPATH, '//*[@id="histogram_Genes_detected_svg"]').get_attribute('outerHTML'))
    svg3=str(driver.find_element(By.XPATH, '//*[@id="histogram_Fraction_mitochrondrial_UMIs_svg"]').get_attribute('outerHTML'))

    get_png(svg1,i+"_Braak_0_UMIs")
    get_png(svg2,i+"_Braak_0_Genes")
    get_png(svg3,i+"_Braak_0_Fraction")
    action.move_to_element(elem).click().perform()
    
    elem = driver.find_element(
        By.XPATH, '//*[@id="value-toggle-checkbox-Braak stage-Braak II"]')
    action.move_to_element(elem).click().perform()
    get_img(driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]'),driver,i+"_Braak_II")
    

    svg1=str(driver.find_element(By.XPATH, '//*[@id="histogram_Number_of_UMIs_svg"]').get_attribute('outerHTML'))
    svg2=str(driver.find_element(By.XPATH, '//*[@id="histogram_Genes_detected_svg"]').get_attribute('outerHTML'))
    svg3=str(driver.find_element(By.XPATH, '//*[@id="histogram_Fraction_mitochrondrial_UMIs_svg"]').get_attribute('outerHTML'))

    get_png(svg1,i+"_Braak_II_UMIs")
    get_png(svg2,i+"_Braak_II_Genes")
    get_png(svg3,i+"_Braak_II_Fraction")

    action.move_to_element(elem).click().perform()

    elem = driver.find_element(
        By.XPATH, '//*[@id="value-toggle-checkbox-Braak stage-Braak III"]')
    
    action.move_to_element(elem).click().perform()
    get_img(driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]'),driver,i+"_Braak_III")
  

    svg1=str(driver.find_element(By.XPATH, '//*[@id="histogram_Number_of_UMIs_svg"]').get_attribute('outerHTML'))
    svg2=str(driver.find_element(By.XPATH, '//*[@id="histogram_Genes_detected_svg"]').get_attribute('outerHTML'))
    svg3=str(driver.find_element(By.XPATH, '//*[@id="histogram_Fraction_mitochrondrial_UMIs_svg"]').get_attribute('outerHTML'))

    get_png(svg1,i+"_Braak_III_UMIs")
    get_png(svg2,i+"_Braak_III_Genes")
    get_png(svg3,i+"_Braak_III_Fraction")
    action.move_to_element(elem).click().perform()

    elem = driver.find_element(
        By.XPATH, '//*[@id="value-toggle-checkbox-Braak stage-Braak IV"]')
    
    action.move_to_element(elem).click().perform()
    get_img(driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]'),driver,i+"_Braak_IV")
   

    svg1=str(driver.find_element(By.XPATH, '//*[@id="histogram_Number_of_UMIs_svg"]').get_attribute('outerHTML'))
    svg2=str(driver.find_element(By.XPATH, '//*[@id="histogram_Genes_detected_svg"]').get_attribute('outerHTML'))
    svg3=str(driver.find_element(By.XPATH, '//*[@id="histogram_Fraction_mitochrondrial_UMIs_svg"]').get_attribute('outerHTML'))

    get_png(svg1,i+"_Braak_IV_UMIs")
    get_png(svg2,i+"_Braak_IV_Genes")
    get_png(svg3,i+"_Braak_IV_Fraction")

    action.move_to_element(elem).click().perform()

    
    elem = driver.find_element(
        By.XPATH, '//*[@id="value-toggle-checkbox-Braak stage-Braak V"]')
    
    action.move_to_element(elem).click().perform()
    get_img(driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]'),driver,i+"_Braak_V")
    
    svg1=str(driver.find_element(By.XPATH, '//*[@id="histogram_Number_of_UMIs_svg"]').get_attribute('outerHTML'))
    svg2=str(driver.find_element(By.XPATH, '//*[@id="histogram_Genes_detected_svg"]').get_attribute('outerHTML'))
    svg3=str(driver.find_element(By.XPATH, '//*[@id="histogram_Fraction_mitochrondrial_UMIs_svg"]').get_attribute('outerHTML'))

    get_png(svg1,i+"_Braak_V_UMIs")
    get_png(svg2,i+"_Braak_V_Genes")
    get_png(svg3,i+"_Braak_V_Fraction")
    
    action.move_to_element(elem).click().perform()

    elem = driver.find_element(
        By.XPATH, '//*[@id="value-toggle-checkbox-Braak stage-Braak VI"]')
    
    action.move_to_element(elem).click().perform()
    get_img(driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]'),driver,i+"_Braak_VI")
    
    svg1=str(driver.find_element(By.XPATH, '//*[@id="histogram_Number_of_UMIs_svg"]').get_attribute('outerHTML'))
    svg2=str(driver.find_element(By.XPATH, '//*[@id="histogram_Genes_detected_svg"]').get_attribute('outerHTML'))
    svg3=str(driver.find_element(By.XPATH, '//*[@id="histogram_Fraction_mitochrondrial_UMIs_svg"]').get_attribute('outerHTML'))

    get_png(svg1,i+"_Braak_VI_UMIs")
    get_png(svg2,i+"_Braak_VI_Genes")
    get_png(svg3,i+"_Braak_VI_Fraction")

    
    action.move_to_element(elem).click().perform()

    t.sleep(10)
driver.close()
