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

def test_login(driver):
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    driver.find_element(By.CSS_SELECTOR, '[href="login.html"]').click()
    users = ['user1','user2','user3','user4','user5']
    for i in users:
        driver.find_element(By.CSS_SELECTOR, '#login').clear()
        driver.find_element(By.CSS_SELECTOR, '#password').clear()
        driver.find_element(By.CSS_SELECTOR, '#login').send_keys(i)
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Pass1234')
        driver.find_element(By.XPATH, """//button[contains(text(), 'Войти')]""").click()
        assert driver.find_element(By.CSS_SELECTOR,'#loginMessage').text == 'Вход успешен!'

def test_newuser(driver):
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    driver.find_element(By.CSS_SELECTOR, '[href="login.html"]').click()
    driver.find_element(By.CSS_SELECTOR, '#newLogin').send_keys('user6')
    driver.find_element(By.CSS_SELECTOR, '#newPassword').send_keys('Pass1234')
    driver.find_element(By.XPATH, """//button[contains(text(), 'Добавить')]""").click()
    assert driver.find_element(By.CSS_SELECTOR,'#addUserMessage').text == 'Пользователь добавлен!'
    driver.find_element(By.CSS_SELECTOR, '#login').send_keys('user6')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Pass1234')
    driver.find_element(By.XPATH, """//button[contains(text(), 'Войти')]""").click()
    assert driver.find_element(By.CSS_SELECTOR,'#loginMessage').text == 'Вход успешен!'

def test_newusers3(driver):
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    driver.find_element(By.CSS_SELECTOR, '[href="login.html"]').click()
    listlogin = ['user7','user8','user9']
    for i in listlogin:
        driver.find_element(By.CSS_SELECTOR, '#newLogin').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#newPassword').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#newLogin').send_keys(i)
        driver.find_element(By.CSS_SELECTOR, '#newPassword').send_keys('Pass1234')
        driver.find_element(By.XPATH, """//button[contains(text(), 'Добавить')]""").click()
        assert driver.find_element(By.CSS_SELECTOR,'#addUserMessage').text == 'Пользователь добавлен!'
    for ii in listlogin:
        driver.find_element(By.CSS_SELECTOR, '#login').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#login').send_keys(ii)
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Pass1234')
        driver.find_element(By.XPATH, """//button[contains(text(), 'Войти')]""").click()
        assert driver.find_element(By.CSS_SELECTOR,'#loginMessage').text == 'Вход успешен!'

def test_newusers3(driver):
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    driver.find_element(By.CSS_SELECTOR, '[href="shop.html"]').click()
    driver.find_element(By.CSS_SELECTOR, '[data-name="Товар 1"]').click()
    driver.find_element(By.CSS_SELECTOR, '[data-name="Товар 2"]').click()
    driver.find_element(By.CSS_SELECTOR, '[data-name="Товар 3"]').click()