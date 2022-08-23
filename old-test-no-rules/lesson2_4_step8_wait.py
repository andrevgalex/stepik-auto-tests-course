from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
    # Нажать на кнопку
    book_button.click()

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    # Получаю Y
    x_element = browser.find_element_by_id("input_value").text
    y = calc(x_element)
    # Код, который ищет поле ввода ответа и заполняет форму
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Отправляем заполненную форму
    submit_button = browser.find_element_by_id("solve")
    submit_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла