from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаю Y
    x_element = browser.find_element_by_id("input_value").get_attribute("valuex")
    # x = x_element.text
    y = calc(x_element)

    # Код, который ищет поле ввода ответа и заполняет форму
    element = browser.find_element_by_id("answer")
    element.send_keys(y)

    # Проставляю Чекбоксы и Радиобатоны
    check = browser.find_element_by_id("robotCheckbox")
    check.click()
    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()