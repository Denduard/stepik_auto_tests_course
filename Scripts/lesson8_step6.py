from selenium import webdriver
from selenium.webdriver.common.by import By
import math,time
def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))
try:


    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #ретерн аргументс[0] возвращает ПЕРВЫЙ эллемент на странице отвечающий условию
    #скролл интовью(тру) заставляет страницу скроллить вниз до заданного  условия ( баттон)
    button.click()
    
    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(y)
    
    checkbox1 = browser.find_element(By.XPATH, "//input[@type='checkbox']")
    checkbox1.click()
    
    radio1 = browser.find_element(By.ID, "robotsRule")
    radio1.click()
    
finally:
    time.sleep(5)
