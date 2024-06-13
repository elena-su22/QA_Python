import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re

# для запуска  рабочим print: pytest -s test_pytests1\test_4send.py

@pytest.fixture
def driver():
    driver1 = webdriver.Chrome()
    driver1.implicitly_wait(3)
    yield driver1
    driver1.quit()

def test_senddata(driver):
    driver.get('https://erikdark.github.io/dovod_repo_QA_form/')
    driver.find_element(By.CSS_SELECTOR, '#login').send_keys('admin123')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('password123')
    driver.find_element(By.CSS_SELECTOR, '#database').send_keys('bd_dovod')
    driver.find_element(By.CSS_SELECTOR, '#host').send_keys('localhost')
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    time.sleep(5)