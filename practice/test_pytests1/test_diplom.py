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

# def test_name(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.CSS_SELECTOR, '[href="registration.html"]').click()
#     falsename = ['123','qwerty123','qwer-ty123','qwer ty','qwerty!']
#     for i in falsename:
#         driver.find_element(By.CSS_SELECTOR, '#name').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#email').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#password').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#name').send_keys(i)
#         driver.find_element(By.CSS_SELECTOR, '#email').send_keys('qwerty@mail.ru')
#         driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Qwerty123')
#         driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys('Qwerty123')
#         driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#         assert driver.find_element(By.CSS_SELECTOR,'#message').text == 'Имя может содержать только буквы и знак "-"'
#     truename = ['qwerty','qwer-ty']
#     for ii in truename:
#         driver.find_element(By.CSS_SELECTOR, '#name').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#email').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#password').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#name').send_keys(ii)
#         driver.find_element(By.CSS_SELECTOR, '#email').send_keys('qwerty@mail.ru')
#         driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Qwerty123')
#         driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys('Qwerty123')
#         driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#         assert driver.find_element(By.CSS_SELECTOR,'#message').text == 'Регистрация успешна!'

# def test_email(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.CSS_SELECTOR, '[href="registration.html"]').click()
#     falsemail = ['qwerty','qwerty@','@qwerty','qwerty@qwe.','qwerty@.q','qwer@ty@mail.ru']
#     for i in falsemail:
#         driver.find_element(By.CSS_SELECTOR, '#name').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#email').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#password').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#name').send_keys('qwerty')
#         driver.find_element(By.CSS_SELECTOR, '#email').send_keys(i)
#         driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Qwerty123')
#         driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys('Qwerty123')
#         driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#         assert WebDriverWait(driver,3).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'#message')))
#     falsemail2 = ['qwerty@qwer']
#     for i in falsemail2:
#         driver.find_element(By.CSS_SELECTOR, '#name').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#email').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#password').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#name').send_keys('qwerty')
#         driver.find_element(By.CSS_SELECTOR, '#email').send_keys(i)
#         driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Qwerty123')
#         driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys('Qwerty123')
#         driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#         assert driver.find_element(By.CSS_SELECTOR,'#message').text == 'Введите корректный email'
#     driver.find_element(By.CSS_SELECTOR, '#name').send_keys(Keys.BACKSPACE * 20)
#     driver.find_element(By.CSS_SELECTOR, '#email').send_keys(Keys.BACKSPACE * 20)
#     driver.find_element(By.CSS_SELECTOR, '#password').send_keys(Keys.BACKSPACE * 20)
#     driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(Keys.BACKSPACE * 20)
#     driver.find_element(By.CSS_SELECTOR, '#name').send_keys('qwerty')
#     driver.find_element(By.CSS_SELECTOR, '#email').send_keys('qwerty@mail.ru')
#     driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Qwerty123')
#     driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys('Qwerty123')
#     driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#     assert driver.find_element(By.CSS_SELECTOR,'#message').text == 'Регистрация успешна!'

# def test_pass(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.CSS_SELECTOR, '[href="registration.html"]').click()
#     falsepass = ['Qwerty1','qwerty123','QWERTY123','12345678']
#     for i in falsepass:
#         driver.find_element(By.CSS_SELECTOR, '#name').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#email').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#password').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#name').send_keys('qwerty')
#         driver.find_element(By.CSS_SELECTOR, '#email').send_keys('qwerty@mail.ru')
#         driver.find_element(By.CSS_SELECTOR, '#password').send_keys(i)
#         driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(i)
#         driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#         assert driver.find_element(By.CSS_SELECTOR,'#message').text == 'Пароль должен содержать не менее 8 символов, включая 1 заглавную букву, 1 строчную букву и 1 цифру'
#     truepass = ['Qwertyqwe1','QWERTYQWe1','Qw123456','Qwertyqwe1!!@#$%^&*()?/\"№;:,.<>']
#     for ii in truepass:
#         driver.find_element(By.CSS_SELECTOR, '#name').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#email').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#password').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#name').send_keys('qwerty')
#         driver.find_element(By.CSS_SELECTOR, '#email').send_keys('qwerty@mail.ru')
#         driver.find_element(By.CSS_SELECTOR, '#password').send_keys(ii)
#         driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(ii)
#         driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#         assert driver.find_element(By.CSS_SELECTOR,'#message').text == 'Регистрация успешна!'

# def test_confirmpass(driver):
#     passlist = ['Qwertyqwe1','QWERTYQWe1','Qw123456','Qwertyqwe1!!@#$%^&*()?/\"№;:,.<>']
#     for i in range(20):
#         pass1 = random.choice(passlist)
#         confpass = random.choice(passlist)
#         driver.get('https://erikdark.github.io/QA_DIPLOM/')
#         driver.find_element(By.CSS_SELECTOR, '[href="registration.html"]').click()
#         driver.find_element(By.CSS_SELECTOR, '#name').send_keys('qwerty')
#         driver.find_element(By.CSS_SELECTOR, '#email').send_keys('qwerty@mail.ru')
#         driver.find_element(By.CSS_SELECTOR, '#password').send_keys(pass1)
#         driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys(confpass)
#         driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#         if pass1 == confpass:
#             assert driver.find_element(By.CSS_SELECTOR,'#message').text == 'Регистрация успешна!'
#         else:
#             assert driver.find_element(By.CSS_SELECTOR,'#message').text == 'Пароли не совпадают'

# def test_login(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.CSS_SELECTOR, '[href="login.html"]').click()
#     users = ['user1','user2','user3','user4','user5']
#     for i in users:
#         driver.find_element(By.CSS_SELECTOR, '#login').clear()
#         driver.find_element(By.CSS_SELECTOR, '#password').clear()
#         driver.find_element(By.CSS_SELECTOR, '#login').send_keys(i)
#         driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Pass1234')
#         driver.find_element(By.XPATH, """//button[contains(text(), 'Войти')]""").click()
#         assert driver.find_element(By.CSS_SELECTOR,'#loginMessage').text == 'Вход успешен!'

# def test_newuser(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.CSS_SELECTOR, '[href="login.html"]').click()
#     driver.find_element(By.CSS_SELECTOR, '#newLogin').send_keys('user6')
#     driver.find_element(By.CSS_SELECTOR, '#newPassword').send_keys('Pass1234')
#     driver.find_element(By.XPATH, """//button[contains(text(), 'Добавить')]""").click()
#     assert driver.find_element(By.CSS_SELECTOR,'#addUserMessage').text == 'Пользователь добавлен!'
#     driver.find_element(By.CSS_SELECTOR, '#login').send_keys('user6')
#     driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Pass1234')
#     driver.find_element(By.XPATH, """//button[contains(text(), 'Войти')]""").click()
#     assert driver.find_element(By.CSS_SELECTOR,'#loginMessage').text == 'Вход успешен!'

# def test_newusers3(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.CSS_SELECTOR, '[href="login.html"]').click()
#     listlogin = ['user7','user8','user9']
#     for i in listlogin:
#         driver.find_element(By.CSS_SELECTOR, '#newLogin').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#newPassword').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#newLogin').send_keys(i)
#         driver.find_element(By.CSS_SELECTOR, '#newPassword').send_keys('Pass1234')
#         driver.find_element(By.XPATH, """//button[contains(text(), 'Добавить')]""").click()
#         assert driver.find_element(By.CSS_SELECTOR,'#addUserMessage').text == 'Пользователь добавлен!'
#     for ii in listlogin:
#         driver.find_element(By.CSS_SELECTOR, '#login').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#password').send_keys(Keys.BACKSPACE * 20)
#         driver.find_element(By.CSS_SELECTOR, '#login').send_keys(ii)
#         driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Pass1234')
#         driver.find_element(By.XPATH, """//button[contains(text(), 'Войти')]""").click()
#         assert driver.find_element(By.CSS_SELECTOR,'#loginMessage').text == 'Вход успешен!'

# def test_shop(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.CSS_SELECTOR, '[href="shop.html"]').click()
#     listbuy = ['[data-name="Товар 1"]','[data-name="Товар 2"]','[data-name="Товар 3"]']
#     for i in listbuy:
#         driver.find_element(By.CSS_SELECTOR, i).click()
#         driver.switch_to.alert.accept()
#     driver.find_element(By.CSS_SELECTOR, '#cartButton').click()
#     cartItems = driver.find_element(By.CSS_SELECTOR, '#cartItems').text
#     listcartItems = ['Товар 1 - $100','Товар 2 - $200','Товар 3 - $350']
#     for i in listcartItems:
#         assert i in cartItems
#     driver.find_element(By.CSS_SELECTOR, '.close').click()
#     driver.find_element(By.CSS_SELECTOR, '[data-name="Товар 1"]').click()
#     driver.switch_to.alert.accept()
#     driver.find_element(By.CSS_SELECTOR, '#cartButton').click()
#     cartItems = driver.find_element(By.CSS_SELECTOR, '#cartItems').text
#     cartItemsspl = cartItems.split('Товар')
#     sumthing1 = 0
#     for i in cartItemsspl:
#         if '1' in i:
#             sumthing1 +=1
#     assert sumthing1 == 2
#     time.sleep(3)

# @pytest.mark.xfail
# def test_shopprice(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.CSS_SELECTOR, '[href="shop.html"]').click()
#     listbuy = ['[data-name="Товар 1"]','[data-name="Товар 2"]','[data-name="Товар 3"]']
#     for i in listbuy:
#         driver.find_element(By.CSS_SELECTOR, i).click()
#         driver.switch_to.alert.accept()
#     price = driver.find_elements(By.CSS_SELECTOR, '.product p')
#     price1 = price[0].text
#     price1list = price1.split('$')
#     price1 = price1list[1]
#     price2 = price[1].text
#     price2list = price2.split('$')
#     price2 = price2list[1]
#     price3 = price[2].text
#     price3list = price3.split('$')
#     price3 = price3list[1]
#     driver.find_element(By.CSS_SELECTOR, '#cartButton').click()
#     pricein = driver.find_elements(By.CSS_SELECTOR, '#cartItems div')
#     pricein1 = pricein[0].text
#     pricein1list = pricein1.split('$')
#     pricein1 = pricein1list[1]
#     pricein2 = pricein[1].text
#     pricein2list = pricein2.split('$')
#     pricein2 = pricein2list[1]
#     pricein3 = pricein[2].text
#     pricein3list = pricein3.split('$')
#     pricein3 = pricein3list[1]
#     assert price1 == pricein1, 'price1 diff'
#     assert price2 == pricein2, 'price2 diff'
#     assert price3 == pricein3, 'price3 diff'

# def test_SQL1(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.CSS_SELECTOR, '[href="database.html"]').click()
#     place = driver.find_element(By.CSS_SELECTOR, '#sqlQuery')
#     place.send_keys("SELECT * FROM TABLE WHERE NAME = 'Иван'")
#     driver.find_element(By.CSS_SELECTOR, '#executeButton').click()
#     assert driver.find_element(By.CSS_SELECTOR, '#sqlMessage') == 'Найдено 1 записей.'
#     time.sleep(3)

# def test_SQL2(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.CSS_SELECTOR, '[href="database.html"]').click()
#     place = driver.find_element(By.CSS_SELECTOR, '#sqlQuery')
#     place.send_keys("ORDER BY age")
#     driver.find_element(By.CSS_SELECTOR, '#executeButton').click()
#     assert driver.find_element(By.CSS_SELECTOR, '#sqlMessage') == 'Данные отсортированы по age.'


# def test_SQL3(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.CSS_SELECTOR, '[href="database.html"]').click()
#     place = driver.find_element(By.CSS_SELECTOR, '#sqlQuery')
#     place.send_keys("DELETE FROM TABLE WHERE ID = 1")
#     driver.find_element(By.CSS_SELECTOR, '#executeButton').click()
#     assert driver.find_element(By.CSS_SELECTOR, '#sqlMessage') == 'Запись с ID 1 удалена.'
