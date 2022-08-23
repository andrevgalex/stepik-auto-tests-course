from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаю Y
    x_element = browser.find_element_by_id("input_value").text
    y = calc(x_element)

    # Скролл
    browser.execute_script("window.scrollBy(0, 200);")

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
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла