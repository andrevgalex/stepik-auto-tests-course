import pytest
import time
import math
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By




# @pytest.mark.parametrize('number', ["236895"])
@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, number):
    # открыть страницу
    link = f"https://stepik.org/lesson/{number}/step/1?auth=login"
    browser.get(link)
    # print("\nlink opened")

    # авторизоваться на странице со своим логином и паролем
    # Открываем файл с конфигом в режиме чтения
    with open('config.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
    # print("\nautorization")
    auth_login = browser.find_element(By.NAME, "login")
    auth_login.send_keys(config['login_stepik'])
    auth_password = browser.find_element(By.NAME, "password")
    auth_password.send_keys(config['password_stepik'])

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
    # print("\nautorization submited")

    # если поле не пустое, то начать задание заново
    # print("\ncheck previous try")
    try:
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.again-btn")))
        clickable = True
    except TimeoutException as exc:
        clickable = False
        print("\n", exc)
    if clickable:
        button_reset = browser.find_element(By.CSS_SELECTOR, "button.again-btn")
        button_reset.click()
        # print("\nclick reset")
        button_ok = browser.find_element(By.XPATH, "//button[text()='OK']")
        button_ok.click()
        # print("\nclick OK")
        # поле перед вводом должно быть пустым
        text_area = browser.find_element(By.CSS_SELECTOR, "textarea")
        text_area.clear()
    # ввести правильный ответ
    text_area = browser.find_element(By.CSS_SELECTOR, "textarea")
    answer = math.log(int(time.time()))
    text_area.send_keys(answer)
    time.sleep(3)

    # print("\nanswer inputed")

    # нажать кнопку "Отправить"
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
    )
    button.click()
    # print("\nclick Send")

    # дождаться фидбека о том, что ответ правильный
    # проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
    # print("\ncheck feedback")
    feedback = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
    if (feedback.text != 'Correct!'):
        final = feedback.text
        print("\n", final)
# The owls are not what they seem! OvO
