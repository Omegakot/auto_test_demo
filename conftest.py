
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language")

@pytest.fixture(scope='session')
def browser(request):
    language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    print("запуск драйвера")
    yield browser
    time.sleep(10)
    browser.quit()
