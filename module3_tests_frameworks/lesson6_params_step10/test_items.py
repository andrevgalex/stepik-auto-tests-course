import time
from types import FunctionType as function
from selenium.webdriver.common.by import By


def test_available_item(browser: function):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "btn-add-to-basket")