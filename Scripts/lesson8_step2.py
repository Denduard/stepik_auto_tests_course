from selenium import webdriver
#импортируем библиотеку селект
from selenium.webdriver.support.ui import Select 
#мпортируем бибилотеку со многими локаторами ( tag name,ID,class name и тд)
from selenium.webdriver.common.by import By
import time


try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    #получаем ТЕКСТОВОЕ значение первого слагаемого и присваеваем к переменной икс 
    x = browser.find_element(By.ID, "num1").text
    #получаем ТЕКСТОВОЕ значение второго слагаемого и присваеваем к переменной игрек
    y = browser.find_element(By.ID, "num2").text
    #производим сложение переменной икс и игрек как ЦИФРОВОЕ значение
    summary = (int(x) + int(y))
    #используем метод селект для открытия выпадающего очка, а потом применяем Select чтобы считать значения списков 
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    #используя метод селект бай вэлью(если у тега есть атрибут вэлью) класса селект и переменную саммари, которое преобразовано в СТРОКОВЕ знач. при помощи метода str
    # и сравниваем значение аттрибута вэлью со СТРОКОВЫМ значением переменной саммари
    select.select_by_value(str(summary))
                    
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()
    #пиздец ебаный нихуя не понятно на ранндоме ебучем вывезли и ТО НАХУЙ 
    
