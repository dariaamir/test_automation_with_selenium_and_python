import random

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', default='en',
                     help="Choose interface language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = Options()
        options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def email():
    return ''.join(random.choice('0123456789ABCDEF') for i in range(12)) + "@fakemail.org"


@pytest.fixture(scope="function")
def password():
    return ''.join(random.choice('0123456789ABCDEF') for i in range(16))
