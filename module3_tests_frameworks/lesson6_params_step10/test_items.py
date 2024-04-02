import time
from types import FunctionType as function
from selenium.webdriver.common.by import By


def test_available_item(browser: function):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    # link = " https://selenium1py.pythonanywhere.com/catalogue/love_82/"
    browser.get(link)
    try:
        browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > .btn-add-to-basket")
        is_element_present = True
    except:
        is_element_present = False
    assert is_element_present == True, "\nThe book is not available"
