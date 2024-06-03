import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pygame

# driver = webdriver.Chrome()
# driver.get('http://fortesters.easysmarthub.ru/form1/')
# inputone = driver.find_element(By.NAME, 'name')
# inputone.send_keys('Lena')
# btn = driver.find_element(By.NAME, 'button')
# btn.click()
# time.sleep(5)

# driver = webdriver.Chrome()
# driver.get('https://google.com/')
# inputone = driver.find_element(By.NAME,"q")
# inputone.send_keys('Lena')
# time.sleep(5)
# btn = driver.find_element(By.NAME, "btnK")
# btn.click()
# time.sleep(10)
# # "textarea#APjFqb.gLFyf"
# # "input.gNO89b.

# driver = webdriver.Chrome()
# driver.get('https://erikdark.github.io/Qa_autotest_01/')
# inputone = driver.find_element(By.ID,"inputField")
# inputone.send_keys('Lena')
# time.sleep(5)
# btn = driver.find_element(By.CSS_SELECTOR, 'button.btn:nth-child(3)')
# btn.click()
# time.sleep(5)

driver = webdriver.Chrome()
driver.get('https://erikdark.github.io/Qa_autotest_01/')
btn = driver.find_elements(By.CSS_SELECTOR, 'button.btn')
num = 0
for i in btn:
    num+=1
print(num)
if num == 8:
    print('da')
else:
    print('no')
driver.quit()