from selenium import webdriver
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element('tag name', 'input')
    input1.send_keys("Evgeniy")
    input2 = browser.find_element('name', 'last_name')
    input2.send_keys("Andreev")
    input3 = browser.find_element('class name', 'city')
    input3.send_keys("Yaroslavl")
    input4 = browser.find_element('id', 'country')
    input4.send_keys("Russia")
    button = browser.find_element('css selector', 'button.btn')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла