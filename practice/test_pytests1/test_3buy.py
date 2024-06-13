import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re

# для запуска  рабочим print: pytest -s test_pytests1\test_3buy.py

@pytest.fixture
def driver():
    driver1 = webdriver.Chrome()
    driver1.implicitly_wait(3)
    yield driver1
    driver1.quit()

def test_buybooks(driver):
    driver.get('http://selenium1py.pythonanywhere.com/ru/')
    driver.find_element(By.LINK_TEXT, 'Предложения').click()
    for i in range(4):
        driver.find_elements(By.CSS_SELECTOR, "button.btn.btn-primary.btn-block")[i].click()

    # WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.btn.btn-primary.btn-block:nth-of-type(1)'))).click()
    # WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.btn.btn-primary.btn-block:nth-of-type(2)'))).click()

    # driver.find_element(By.CSS_SELECTOR, 'button:nth-child(3)').click()
    # driver.find_element(By.CSS_SELECTOR, 'button:nth-child(4)').click()
    # driver.find_element(By.CSS_SELECTOR, 'button:nth-child(5)').click()
    # driver.find_element(By.CSS_SELECTOR, 'button:nth-child(6)').click()

    # driver.get('http://selenium1py.pythonanywhere.com/ru/')
    # list1 = [3,4,5,6]
    # for i in list1:
    #     driver.find_element(By.LINK_TEXT, 'Предложения').click()
    #     driver.find_element(By.CSS_SELECTOR, f'button:nth-child({i})').click()
    #     driver.find_element(By.LINK_TEXT, 'Начало').click()
  
    driver.find_element(By.LINK_TEXT, 'Посмотреть корзину').click()
    driver.find_element(By.LINK_TEXT, 'Перейти к оформлению').click()
    driver.find_element(By.CSS_SELECTOR, '[type="email"]').send_keys('elena@gmail.com')
    driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys('qwerty123')
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    select = Select(driver.find_element(By.TAG_NAME,'select'))
    select.select_by_value('Miss')
    driver.find_element(By.CSS_SELECTOR, '[name="first_name"]').send_keys('elena')
    driver.find_element(By.CSS_SELECTOR, '[name="last_name"]').send_keys('elena')
    driver.find_element(By.CSS_SELECTOR, '[name="line1"]').send_keys('St. Peterburg')
    driver.find_element(By.CSS_SELECTOR, '[name="line4"]').send_keys('St. Peterburg')
    driver.find_element(By.CSS_SELECTOR, '[name="postcode"]').send_keys('187015')
    select = Select(driver.find_element(By.CSS_SELECTOR,'#id_country'))
    select.select_by_value('RU')
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    driver.find_element(By.CSS_SELECTOR, '#view_preview').click()
    driver.find_element(By.CSS_SELECTOR, '#place-order').click()
    time.sleep(10)