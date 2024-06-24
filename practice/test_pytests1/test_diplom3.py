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

# для запуска  рабочим print: pytest -s test_pytests1\test_diplom.py

@pytest.fixture
def driver():
    driver1 = webdriver.Chrome()
    driver1.implicitly_wait(3)
    yield driver1
    driver1.quit()

def test_shop(driver):
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    driver.find_element(By.CSS_SELECTOR, '[href="shop.html"]').click()
    listbuy = ['[data-name="Товар 1"]','[data-name="Товар 2"]','[data-name="Товар 3"]']
    for i in listbuy:
        driver.find_element(By.CSS_SELECTOR, i).click()
        driver.switch_to.alert.accept()
    driver.find_element(By.CSS_SELECTOR, '#cartButton').click()
    cartItems = driver.find_element(By.CSS_SELECTOR, '#cartItems').text
    listcartItems = ['Товар 1 - $100','Товар 2 - $200','Товар 3 - $350']
    for i in listcartItems:
        assert i in cartItems
    driver.find_element(By.CSS_SELECTOR, '.close').click()
    driver.find_element(By.CSS_SELECTOR, '[data-name="Товар 1"]').click()
    driver.switch_to.alert.accept()
    driver.find_element(By.CSS_SELECTOR, '#cartButton').click()
    cartItems = driver.find_element(By.CSS_SELECTOR, '#cartItems').text
    cartItemsspl = cartItems.split('Товар')
    sumthing1 = 0
    for i in cartItemsspl:
        if '1' in i:
            sumthing1 +=1
    assert sumthing1 == 2

@pytest.mark.xfail
def test_shopprice(driver):
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    driver.find_element(By.CSS_SELECTOR, '[href="shop.html"]').click()
    listbuy = ['[data-name="Товар 1"]','[data-name="Товар 2"]','[data-name="Товар 3"]']
    for i in listbuy:
        driver.find_element(By.CSS_SELECTOR, i).click()
        driver.switch_to.alert.accept()
    price = driver.find_elements(By.CSS_SELECTOR, '.product p')
    price1 = price[0].text
    price1list = price1.split('$')
    price1 = price1list[1]
    price2 = price[1].text
    price2list = price2.split('$')
    price2 = price2list[1]
    price3 = price[2].text
    price3list = price3.split('$')
    price3 = price3list[1]
    driver.find_element(By.CSS_SELECTOR, '#cartButton').click()
    pricein = driver.find_elements(By.CSS_SELECTOR, '#cartItems div')
    pricein1 = pricein[0].text
    pricein1list = pricein1.split('$')
    pricein1 = pricein1list[1]
    pricein2 = pricein[1].text
    pricein2list = pricein2.split('$')
    pricein2 = pricein2list[1]
    pricein3 = pricein[2].text
    pricein3list = pricein3.split('$')
    pricein3 = pricein3list[1]
    assert price1 == pricein1, 'price1 diff'
    assert price2 == pricein2, 'price2 diff'
    assert price3 == pricein3, 'price3 diff'

