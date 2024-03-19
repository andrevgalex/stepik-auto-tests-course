import pytest
import time
import math
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

answer = math.log(int(time.time()))


@pytest.mark.parametrize('number', ["236895"])
# @pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, number):
    # открыть страницу
    print("\nopen link")
    link = f"https://stepik.org/lesson/{number}/step/1?auth=login"
    browser.get(link)

    # авторизоваться на странице со своим логином и паролем
    # Открываем файл с конфигом в режиме чтения
    with open('config.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
    print("\nautorization")
    auth_login = browser.find_element(By.NAME, "login")
    auth_login.send_keys(config['login_stepik'])
    auth_password = browser.find_element(By.NAME, "password")
    auth_password.send_keys(config['password_stepik'])

    print("\nsubmit autorization")
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    # поле перед вводом должно быть пустым
    # text_area = browser.find_element(By.CSS_SELECTOR, "textarea")
    # text_area.clear()
    # если поле не пустое, то начать задание заново
    print("\ncheck previous try")
    clickable = EC.element_to_be_clickable((By.CSS_SELECTOR, "button.again-btn"))
    if clickable:
        print("\nclick reset")
        button_reset = browser.find_element(By.CSS_SELECTOR, "button.again-btn")
        button_reset.click()
        print("\nclick OK")
        time.sleep(5)
        # confirm = browser.switch_to.alert
        # confirm.click()
        button_ok = browser.find_element(By.CSS_SELECTOR, "#ember527 > button:nth-child(1)")
        button_ok.click()
    # ввести правильный ответ
    print("\ninput answer")
    text_area = browser.find_element(By.CSS_SELECTOR, "textarea")
    text_area.send_keys(answer)

    # нажать кнопку "Отправить"
    print("\nclick Send")
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
    )
    # button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    button.click()

    # дождаться фидбека о том, что ответ правильный
    # проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
    print("\ncheck feedback")
    feedback = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
    if (feedback != 'Correct'):
        final = feedback
        print(final)
