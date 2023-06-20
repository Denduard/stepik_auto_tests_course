from selenium import webdriver
from selenium.webdriver.common.by import By
import os,time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)


    input1 = browser.find_element(By.XPATH,"//input[@name='firstname']")
    input1.send_keys("DiniZ")
    input2 = browser.find_element(By.XPATH,"//input[@name='lastname']")
    input2.send_keys("DiniZ")
    input3 = browser.find_element(By.XPATH,"//input[@name='email']")
    input3.send_keys("DiniZ")
    current_dir = os.path.abspath(os.path.dirname("C:\\Users\\Денис Саринов\\selenium_python\\environments\\selenium_env\\Scripts\\lesson8_step9.txt"))
    file_path = os.path.join(current_dir, 'lesson8_step9.txt')
    input4 = browser.find_element(By.ID,"file")
    input4.send_keys(file_path)                              
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
finally:
 time.sleep(8)

                                
