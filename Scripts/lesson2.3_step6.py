from selenium import webdriver
from selenium.webdriver.common.by import By
import math,time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CLASS_NAME, "btn")
    button1.click()
   # browser.switch_to.window(new_window)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button2 = browser.find_element(By.CLASS_NAME, "btn")
    button2.click()

    
finally:
    time.sleep(5)
