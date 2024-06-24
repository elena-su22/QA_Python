import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import re
import random

# для запуска  рабочим print: pytest -s test_pytests1\test_diplom4.py

@pytest.fixture
def driver():
    driver1 = webdriver.Chrome()
    driver1.implicitly_wait(3)
    yield driver1
    driver1.quit()

def test_41(driver):
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    driver.find_element(By.CSS_SELECTOR, '[href="database.html"]').click()
    place = driver.find_element(By.CSS_SELECTOR, '#sqlQuery')
    place.send_keys("SELECT * FROM TABLE WHERE NAME = 'Иван'")
    driver.find_element(By.CSS_SELECTOR, '#executeButton').click()
    assert driver.find_element(By.CSS_SELECTOR, '#sqlMessage').text == 'Найдено 1 записей.'

def test_42(driver):
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    driver.find_element(By.CSS_SELECTOR, '[href="database.html"]').click()
    place = driver.find_element(By.CSS_SELECTOR, '#sqlQuery')
    place.send_keys("ORDER BY age")
    driver.find_element(By.CSS_SELECTOR, '#executeButton').click()
    assert driver.find_element(By.CSS_SELECTOR, '#sqlMessage').text == 'Данные отсортированы по age.'
    time.sleep(3)

def test_43(driver):
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    driver.find_element(By.CSS_SELECTOR, '[href="database.html"]').click()
    place = driver.find_element(By.CSS_SELECTOR, '#sqlQuery')
    place.send_keys("DELETE FROM TABLE WHERE ID = 1")
    driver.find_element(By.CSS_SELECTOR, '#executeButton').click()
    assert driver.find_element(By.CSS_SELECTOR, '#sqlMessage').text == 'Запись с ID 1 удалена.'
