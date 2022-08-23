from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    # link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаю Сумму
    # num1 = browser.find_element_by_id("num1").text
    # num2 = browser.find_element_by_id("num2").text
    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    summ = str(num1+num2)

    # Код, который ищет и выбирает выпадашку с правильным ответом
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(summ)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()