from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    # Получаю Y
    x_element = browser.find_element_by_id("input_value").text
    y = calc(x_element)
    # Код, который ищет поле ввода ответа и заполняет форму
    element = browser.find_element_by_id("answer")
    element.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла