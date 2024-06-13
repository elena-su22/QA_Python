import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re

# для запуска  рабочим print: pytest -s test_pytests1\test_2fixture2.py, можно добавить -v чтобы отображать названия тестов, --reruns 5 - колво перезапусков после установки pipinstall

@pytest.fixture
def driver():
    driver1 = webdriver.Firefox()
    driver1.implicitly_wait(3)
    yield driver1
    driver1.quit()

def test_valid_login(driver):
    driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')
    driver.find_element(By.CSS_SELECTOR, '#openModalButton').click()
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('testuser')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('password123')
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    assert WebDriverWait(driver,3).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'[type="submit"]'))), 'bnt is here'

@pytest.mark.xfail
def test_no_pass(driver):
    driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')
    driver.find_element(By.CSS_SELECTOR, '#openModalButton').click()
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('testuser')
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    try:
        assert WebDriverWait(driver,3).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'[type="submit"]')))
    except:
        print('bnt is here, no pass')
    # assert WebDriverWait(driver,3).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'[type="submit"]'))), 'bnt is here, no pass'

@pytest.mark.xfail
def test_no_login(driver):
    driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')
    driver.find_element(By.CSS_SELECTOR, '#openModalButton').click()
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('password123')
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    try:
        assert WebDriverWait(driver,3).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'[type="submit"]')))
    except:
        print('bnt is here, no login')

@pytest.mark.xfail
def test_invalid_login(driver):
    driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')
    driver.find_element(By.CSS_SELECTOR, '#openModalButton').click()
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('test')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('password123')
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    driver.switch_to.alert.accept()
    try:
        assert WebDriverWait(driver,3).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'[type="submit"]')))
    except:
        print('bnt is here, invalid login')

@pytest.mark.xfail
def test_invalid_pass(driver):
    driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')
    driver.find_element(By.CSS_SELECTOR, '#openModalButton').click()
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('testuser')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('password')
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    driver.switch_to.alert.accept()
    try:
        assert WebDriverWait(driver,3).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'[type="submit"]')))
    except:
        print('bnt is here, invalid pass')