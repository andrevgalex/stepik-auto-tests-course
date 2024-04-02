import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: '--language=es' or '--language=ru'")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser_obj = webdriver.Chrome(options=options)
    browser_obj.implicitly_wait(10)
    yield browser_obj
    print("\nquit browser..")
    browser_obj.quit()
