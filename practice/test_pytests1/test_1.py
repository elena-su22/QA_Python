import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re

def test_reg1():
    try:
        driver = webdriver.Chrome()
        driver.get('https://erikdark.github.io/PyTest_01_reg_form/')
        driver.find_element(By.CSS_SELECTOR, '#username').send_keys('Lena')
        driver.find_element(By.CSS_SELECTOR, '#email').send_keys('Lena@mail.ru')
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Lena123!')
        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        assert driver.find_element(By.CSS_SELECTOR, '#success-message').text == 'Вы успешно зарегистрированы!'
    finally:
        driver.quit()

def test_regerrmail():
    try:
        driver = webdriver.Chrome()
        driver.get('https://erikdark.github.io/PyTest_01_reg_form/')
        driver.find_element(By.CSS_SELECTOR, '#username').send_keys('Lena')
        driver.find_element(By.CSS_SELECTOR, '#email').send_keys('L')
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Lena123!')
        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        assert driver.find_element(By.CSS_SELECTOR, '#success-message').text == 'Вы успешно зарегистрированы!', 'Почта в неверном формате'
        # with pytest.raises(NoSuchElementException):
        #     driver.find_element(By.CSS_SELECTOR, '#success-message').text
        #     pytest.fail('Не должно быть регистрации с неверным форматом почты') == 'Вы успешно зарегистрированы!'
    finally:
        driver.quit()

#NoSuchElementException - только для того, что совсем не существует, не просто нет на странице, а вообще нет в коде