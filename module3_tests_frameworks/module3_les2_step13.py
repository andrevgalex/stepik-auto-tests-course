from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class UniqSelectors(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        element1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        element2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        element3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")

        element1.send_keys("Моооой ответ!!")
        element2.send_keys("Моооой ответ!!")
        element3.send_keys("Моооой ответ!!")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Invalid welcome text")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        element1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        element2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        element3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")

        element1.send_keys("Моооой ответ!!")
        element2.send_keys("Моооой ответ!!")
        element3.send_keys("Моооой ответ!!")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Invalid welcome text")


if __name__ == "__main__":
    unittest.main()