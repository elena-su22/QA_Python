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

# для запуска  рабочим print: pytest -s test_pytests1\test_5zadachi.py

@pytest.fixture
def driver():
    driver1 = webdriver.Chrome()
    driver1.implicitly_wait(3)
    yield driver1
    driver1.quit()

def test_zadacha1(driver):
    driver.get('https://erikdark.github.io/zachet_selenium_01/')
    driver.find_element(By.CSS_SELECTOR, '[href="register.html"]').click()
    driver.find_element(By.CSS_SELECTOR, '#name').send_keys('Elena')
    driver.find_element(By.CSS_SELECTOR, '#email').send_keys('Elena@mail.ru')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Elena1234')
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    assert driver.find_element(By.CSS_SELECTOR,'#register-message').text == 'Пользователь зарегистрирован', 'Ошибка'
    time.sleep(3)

def test_zadacha2(driver):
    driver.get('https://erikdark.github.io/zachet_selenium_01/')
    driver.find_element(By.CSS_SELECTOR, '[href="login.html"]').click()
    driver.find_element(By.CSS_SELECTOR, '#email').send_keys('Elena@mail.ru')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Elena1234')
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    assert driver.find_element(By.CSS_SELECTOR,'#login-message').text == 'Пользователь вошел в систему', 'Ошибка'
    time.sleep(3)

def test_zadacha3(driver):
    driver.get('https://erikdark.github.io/zachet_selenium_01/')
    driver.find_element(By.CSS_SELECTOR, '[href="profile.html"]').click()
    driver.find_element(By.CSS_SELECTOR, '#logout-button').click()
    assert driver.find_element(By.CSS_SELECTOR,'#logout-message').text == 'Пользователь вышел из системы', 'Ошибка'
    time.sleep(3)

def test_zadacha4(driver):
    driver.get('https://erikdark.github.io/zachet_selenium_01/')
    driver.find_element(By.CSS_SELECTOR, '[href="table.html"]').click()
    table1 = []
    for i in range(3):
        str1 = driver.find_element(By.CSS_SELECTOR,f'tbody tr:nth-child({i+1})').text
        list1 = str1.split()
        table1.append(list1)

    driver.find_element(By.CSS_SELECTOR, '[onclick="sortTable(0)"]').click()
    assert driver.find_element(By.CSS_SELECTOR,'#sort-message').text == 'Таблица отсортирована по столбцу 1', 'Ошибка'
    table2 = []
    for i in range(3):
        str2 = driver.find_element(By.CSS_SELECTOR,f'tbody tr:nth-child({i+1})').text
        list2 = str2.split()
        table2.append(list2)
    namelist=[]
    for i in table2:
        namelist.append(i[0])
    namelistsort = sorted(namelist)
    namelistsortrev = namelistsort[::-1]
    assert namelist == namelistsort or namelist == namelistsortrev, 'Ошибка'

    driver.find_element(By.CSS_SELECTOR, '[onclick="sortTable(1)"]').click()
    assert driver.find_element(By.CSS_SELECTOR,'#sort-message').text == 'Таблица отсортирована по столбцу 2', 'Ошибка'
    table3 = []
    for i in range(3):
        str3 = driver.find_element(By.CSS_SELECTOR,f'tbody tr:nth-child({i+1})').text
        list3 = str3.split()
        table3.append(list3)
    agelist=[]
    for i in table3:
        agelist.append(i[1])
    agelistsort = sorted(agelist)
    agelistsortrev = agelistsort[::-1]
    assert agelist == agelistsort or agelist == agelistsortrev, 'Ошибка'

    driver.find_element(By.CSS_SELECTOR, '[onclick="sortTable(2)"]').click()
    assert driver.find_element(By.CSS_SELECTOR,'#sort-message').text == 'Таблица отсортирована по столбцу 3', 'Ошибка'
    table4 = []
    for i in range(3):
        str4 = driver.find_element(By.CSS_SELECTOR,f'tbody tr:nth-child({i+1})').text
        list4 = str4.split()
        table4.append(list4)
    citylist=[]
    for i in table4:
        citylist.append(i[2])
    citylistsort = sorted(citylist)
    citylistsortrev = citylistsort[::-1]
    assert citylist == citylistsort or citylist == citylistsortrev, 'Ошибка'

    time.sleep(3)



def test_zadacha5(driver):
    driver.get('https://erikdark.github.io/zachet_selenium_01/')
    driver.find_element(By.CSS_SELECTOR, '[href="dynamic.html"]').click()

    addbtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#add-element")))
    if addbtn:
        print("Добавить элемент доступно")
    addbtn.click()
    newel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content-area p"))).text
    assert newel == 'Новый элемент', 'Ошибка'
    neweladd = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content-area"))).text
    assert 'Элемент добавлен' in neweladd, 'Ошибка'
    time.sleep(3)

def test_zadacha6(driver):
    driver.get('https://erikdark.github.io/SHADOM-DOM-SELENIUM-QA/?name=df&email=EFE%40MAIL.RU')
    container = driver.find_element(By.CSS_SELECTOR, "#shadow-host")
    container_shadow = container.shadow_root
    container2 = container_shadow.find_element(By.CSS_SELECTOR, "#shadow-host-two")
    container_shadow2 = container2.shadow_root
    inputs = container_shadow2.find_elements(By.CSS_SELECTOR, "input")
    input_field1 = inputs[0]
    input_field1.send_keys("Elena")
    input_field2 = inputs[1]
    input_field2.send_keys("Elena@mail.ru")
    subm = container_shadow2.find_element(By.CSS_SELECTOR, '[type="submit"]')
    subm.click()

