from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time,math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    await_text_value = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element(("id","price"),"$100")
           
    )
    button1 = browser.find_element(By.ID, "book")
    button1.click()
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    button2 = browser.find_element(By.ID, "answer")
    button2.send_keys(y)
    button3 = browser.find_element(By.ID, "solve")
    button3.click()
    

    
finally:
    time.sleep(10)
     
