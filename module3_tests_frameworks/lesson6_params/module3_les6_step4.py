import pytest
import time
import math
from selenium.webdriver.common.by import By

answer = math.log(int(time.time()))

@pytest.mark.parametrize('number', ["236895"])
# @pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, number):
    # открыть страницу
    # link = f"https://stepik.org/lesson/{number}/step/1"
    # browser.get(link)
    # browser.implicitly_wait(5)

    # todo авторизоваться на странице со своим логином и паролем
    link = f"https://stepik.org/lesson/236896/step/1?auth=login"
    browser.get(link)
    browser.implicitly_wait(5)
    auth_login = browser.find_element(By.NAME, "login")
    auth_login.send_keys('login')
    auth_password = browser.find_element(By.NAME, "password")
    auth_password.send_keys('password')
    browser.find_element(By.CSS_SELECTOR, "[button.type='submit']")
    time.sleep(10)

    # ввести правильный ответ (поле перед вводом должно быть пустым)
    textarea = browser.find_element(By.CSS_SELECTOR, "textarea")
    textarea.send_keys(answer)
    time.sleep(10)
    # нажать кнопку "Отправить"
    button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    button.click()

    # todo дождаться фидбека о том, что ответ правильный
    # browser.implicitly_wait(5)
    time.sleep(10)

    # todo проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
