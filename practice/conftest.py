import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name',action='store', default=None, help='Choose browser: chrome or firefox')


@pytest.fixture(scope='function')
def driver(request):
    driver_name = request.config.getoption('browser_name')
    driver = None
    if driver_name == 'Chrome':
        driver = webdriver.Chrome()
    elif driver_name == 'Firefox':
        driver = webdriver.Firefox()
