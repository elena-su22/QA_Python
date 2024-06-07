import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import re
import string


# try:
#     driver = webdriver.Chrome()
#     driver.get('https://erikdark.github.io/QA_autotests_09/')
#     num = driver.find_element(By.CSS_SELECTOR,'#challenge').text
#     num = num.split()
#     sum1 = int(num[2]) + int(num[4].replace('?', ''))
#     print(sum1)
#     driver.find_element(By.CSS_SELECTOR, '#answerSelect').click()
#     for i in range(1,100):
#         text1=driver.find_element(By.CSS_SELECTOR, f'option:nth-child({i})').text
#         if text1 == str(sum1):
#             driver.find_element(By.CSS_SELECTOR, f'option:nth-child({i})').click()
#     driver.find_element(By.CSS_SELECTOR, '#submitBtn').click()
#     time.sleep(5)
# except Exception as ex:
#      print(ex)
# assert driver.find_element(By.CSS_SELECTOR, "#message").text == 'You guessed it! Well done!'
# driver.quit()


# загрузка картинки
# try:
#     driver = webdriver.Chrome()
#     driver.get('https://erikdark.github.io/QA_autotests_11/')
#     driver.find_element(By.CSS_SELECTOR, '#imageInput').send_keys(r'C:\Users\AttekPC\Desktop\smoke1.jpg')
#     time.sleep(2)
#     driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#     time.sleep(2)
# except Exception as ex:
#      print(ex)

# driver.quit()


# try:
#     driver = webdriver.Chrome()
#     driver.get('https://erikdark.github.io/QA_autotests_12/')
#     driver.find_element(By.CSS_SELECTOR, '#startTaskBtn').click()
#     driver.switch_to.alert.accept()
#     driver.switch_to.alert.send_keys('50')
#     driver.switch_to.alert.accept()
#     assert driver.switch_to.alert.text == 'Правильно! Ответ 50.'
#     time.sleep(2)
# except Exception as ex:
#      print(ex)

# driver.quit()


try:
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/QA_autotests_13/')
    driver.find_element(By.CSS_SELECTOR, '#openNewPageBtn').click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.CSS_SELECTOR, '#displayTextBtn').click()
    assert driver.find_element(By.CSS_SELECTOR, '#displayText').text == 'Я СДЕЛАЛ', 'плохо!'
    time.sleep(2)
except Exception as ex:
     print(ex)

driver.quit()
