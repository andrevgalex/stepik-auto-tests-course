from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

#pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py - RETURN'Ы КРУТЫЕ!!!
