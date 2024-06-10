import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re

# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(3)
#     yield driver
#     driver.quit()

driver = webdriver.Chrome()
#pytest test_pytests1\test_2fixture.pydriver.implicitly_wait(3)


def test_valid_login():
    try:
        driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')
        driver.find_element(By.CSS_SELECTOR, '#openModalButton').click()
        driver.find_element(By.CSS_SELECTOR, '#username').send_keys('testuser')
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys('password123')
        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        assert WebDriverWait(driver,3).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'[type="submit"]'))), 'bnt is here'
    finally:
        driver.quit()

@pytest.mark.xfail
def test_no_pass():
    try:
        driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')
        driver.find_element(By.CSS_SELECTOR, '#openModalButton').click()
        driver.find_element(By.CSS_SELECTOR, '#username').send_keys('testuser')
        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        assert WebDriverWait(driver,3).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'[type="submit"]'))), 'bnt is here, pass fail'
    finally:
        driver.quit()

@pytest.mark.xfail
def test_no_login():
    try:
        driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')
        driver.find_element(By.CSS_SELECTOR, '#openModalButton').click()
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys('password123')
        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        assert WebDriverWait(driver,3).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'[type="submit"]'))), 'bnt is here, login fail'
    finally:
        driver.quit()