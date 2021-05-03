from selenium import webdriver
import time

try:
    # link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # elements = browser.find_element_by_class_name("first_block").find_elements_by_tag_name("input")

    # Выбор всех обязательных полей
    # elements = browser.find_elements_by_css_selector("[required]")
    # for element in elements:
    #    element.send_keys("Моооой ответ!!")

    # Выбор каждого из обязательных полей 1
    element1 = browser.find_element_by_css_selector("input.first[required]")
    element2 = browser.find_element_by_css_selector("input.second[required]")
    element3 = browser.find_element_by_css_selector("input.third[required]")

    # Выбор каждого из обязательных полей 2
    # element1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
    # element2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
    # element3 = browser.find_element_by_css_selector("[placeholder='Input your email']")

    element1.send_keys("Моооой ответ!!")
    element2.send_keys("Моооой ответ!!")
    element3.send_keys("Моооой ответ!!")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()