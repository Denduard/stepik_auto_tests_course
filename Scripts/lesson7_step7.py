from selenium import webdriver
from selenium.webdriver.common.by import By
import math,time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #img = browser.find_element(By.ID, "treasure")
    
    x_element = browser.find_element(By. ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    

    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(y)
    
    checkbox1 = browser.find_element(By.XPATH, "//input[@type='checkbox']")
    checkbox1.click()
    
    radio1 = browser.find_element(By.ID, "robotsRule")
    radio1.click()
    
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
