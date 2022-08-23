from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняю текстовые поля
    first_name = browser.find_element_by_name('firstname')
    first_name.send_keys("Evgeniy")
    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys("Andreev")
    e_mail = browser.find_element_by_name('email')
    e_mail.send_keys("andrevgalex@gmail.com")

    # Прикрепляю файл
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '../file.txt')  # добавляем к этому пути имя файла
    file = browser.find_element_by_id('file')
    file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла