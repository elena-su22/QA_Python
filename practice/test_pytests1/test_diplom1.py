import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import re
import random

# для запуска  рабочим print: pytest -s test_pytests1\test_diplom1.py

@pytest.fixture
def driver():
    driver1 = webdriver.Chrome()
    driver1.implicitly_wait(3)
    yield driver1
    driver1.quit()

def test_name(driver):
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    driver.find_element(By.CSS_SELECTOR, '[href="registration.html"]').click()
    falsename = ['123','qwerty123','qwer-ty123','qwer ty','qwerty!']
    for i in falsename:
        driver.find_element(By.CSS_SELECTOR, '#name').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#email').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#name').send_keys(i)
        driver.find_element(By.CSS_SELECTOR, '#email').send_keys('qwerty@mail.ru')
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Qwerty123')
        driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys('Qwerty123')
        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        assert driver.find_element(By.CSS_SELECTOR,'#message').text == 'Имя может содержать только буквы и знак "-"'
    truename = ['qwerty','qwer-ty']
    for ii in truename:
        driver.find_element(By.CSS_SELECTOR, '#name').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#email').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#name').send_keys(ii)
        driver.find_element(By.CSS_SELECTOR, '#email').send_keys('qwerty@mail.ru')
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Qwerty123')
        driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys('Qwerty123')
        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        assert driver.find_element(By.CSS_SELECTOR,'#message').text == 'Регистрация успешна!'

def test_email(driver):
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    driver.find_element(By.CSS_SELECTOR, '[href="registration.html"]').click()
    falsemail = ['qwerty','qwerty@','@qwerty','qwerty@qwe.','qwerty@.q','qwer@ty@mail.ru']
    for i in falsemail:
        driver.find_element(By.CSS_SELECTOR, '#name').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#email').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#name').send_keys('qwerty')
        driver.find_element(By.CSS_SELECTOR, '#email').send_keys(i)
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Qwerty123')
        driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys('Qwerty123')
        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        assert WebDriverWait(driver,3).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'#message')))
    falsemail2 = ['qwerty@qwer']
    for i in falsemail2:
        driver.find_element(By.CSS_SELECTOR, '#name').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#email').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#name').send_keys('qwerty')
        driver.find_element(By.CSS_SELECTOR, '#email').send_keys(i)
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Qwerty123')
        driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys('Qwerty123')
        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        assert driver.find_element(By.CSS_SELECTOR,'#message').text == 'Введите корректный email'
    driver.find_element(By.CSS_SELECTOR, '#name').send_keys(Keys.BACKSPACE * 20)
    driver.find_element(By.CSS_SELECTOR, '#email').send_keys(Keys.BACKSPACE * 20)
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys(Keys.BACKSPACE * 20)
    driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(Keys.BACKSPACE * 20)
    driver.find_element(By.CSS_SELECTOR, '#name').send_keys('qwerty')
    driver.find_element(By.CSS_SELECTOR, '#email').send_keys('qwerty@mail.ru')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Qwerty123')
    driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys('Qwerty123')
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    assert driver.find_element(By.CSS_SELECTOR,'#message').text == 'Регистрация успешна!'

def test_pass(driver):
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    driver.find_element(By.CSS_SELECTOR, '[href="registration.html"]').click()
    falsepass = ['Qwerty1','qwerty123','QWERTY123','12345678']
    for i in falsepass:
        driver.find_element(By.CSS_SELECTOR, '#name').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#email').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#name').send_keys('qwerty')
        driver.find_element(By.CSS_SELECTOR, '#email').send_keys('qwerty@mail.ru')
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys(i)
        driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(i)
        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        assert driver.find_element(By.CSS_SELECTOR,'#message').text == 'Пароль должен содержать не менее 8 символов, включая 1 заглавную букву, 1 строчную букву и 1 цифру'
    truepass = ['Qwertyqwe1','QWERTYQWe1','Qw123456','Qwertyqwe1!!@#$%^&*()?/\"№;:,.<>']
    for ii in truepass:
        driver.find_element(By.CSS_SELECTOR, '#name').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#email').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(Keys.BACKSPACE * 20)
        driver.find_element(By.CSS_SELECTOR, '#name').send_keys('qwerty')
        driver.find_element(By.CSS_SELECTOR, '#email').send_keys('qwerty@mail.ru')
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys(ii)
        driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(ii)
        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        assert driver.find_element(By.CSS_SELECTOR,'#message').text == 'Регистрация успешна!'

def test_confirmpass(driver):
    passlist = ['Qwertyqwe1','QWERTYQWe1','Qw123456','Qwertyqwe1!!@#$%^&*()?/\"№;:,.<>']
    for i in range(20):
        pass1 = random.choice(passlist)
        confpass = random.choice(passlist)
        driver.get('https://erikdark.github.io/QA_DIPLOM/')
        driver.find_element(By.CSS_SELECTOR, '[href="registration.html"]').click()
        driver.find_element(By.CSS_SELECTOR, '#name').send_keys('qwerty')
        driver.find_element(By.CSS_SELECTOR, '#email').send_keys('qwerty@mail.ru')
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys(pass1)
        driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(confpass)
        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        if pass1 == confpass:
            assert driver.find_element(By.CSS_SELECTOR,'#message').text == 'Регистрация успешна!'
        else:
            assert driver.find_element(By.CSS_SELECTOR,'#message').text == 'Пароли не совпадают'
    