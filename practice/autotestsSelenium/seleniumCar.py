import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

driver = webdriver.Chrome()

try:
    # driver.get('https://erikdark.github.io/Qa_autotests_17/')
    # WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#price1'),"550"))
    # WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#buyButton1'))).click()
    # WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#price2'),"800"))
    # WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#buyButton2'))).click()
    # WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#price3'),"19000"))
    # WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#buyButton3'))).click()
    driver.get('https://erikdark.github.io/Qa_autotests_17/')
    check1 = 0
    check2 = 0
    check3 = 0
    while check1==0 or check2==0 or check3 == 0:
        # if driver.find_element(By.CSS_SELECTOR,'#price1').text == "550" and check1==0:
        #     check1 += 1
        #     for i in range(30):
        #         driver.find_element(By.CSS_SELECTOR, '#buyButton1').click()
        if int(driver.find_element(By.CSS_SELECTOR,'#price1').text) == 550 and check1==0:
            check1 += 1
            WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#buyButton1'))).click()
        elif int(driver.find_element(By.CSS_SELECTOR,'#price1').text) <= 550 and check1==0:
            check1 += 1
        if driver.find_element(By.CSS_SELECTOR,'#price2').text == "800" and check2==0:
            check2 += 1
            for i in range(30):
                driver.find_element(By.CSS_SELECTOR, '#buyButton2').click()
        elif int(driver.find_element(By.CSS_SELECTOR,'#price2').text) <= 750 and check2==0:
            check2 += 1
        if driver.find_element(By.CSS_SELECTOR,'#price3').text == "19000" and check3==0:
            check3 += 1
            for i in range(30):
                driver.find_element(By.CSS_SELECTOR, '#buyButton3').click()
        elif int(driver.find_element(By.CSS_SELECTOR,'#price2').text) <= 18550  and check3==0:
            check3 += 1
    if driver.find_element(By.CSS_SELECTOR,'#message1').text == 'Вы успешно купили автомобиль!' and driver.find_element(By.CSS_SELECTOR,'#message2').text == 'Вы успешно купили автомобиль!' and driver.find_element(By.CSS_SELECTOR,'#message3').text == 'Вы успешно купили автомобиль!':
        print('Купили все')
        driver.quit()
    if driver.find_element(By.CSS_SELECTOR,'#message1').text != 'Вы успешно купили автомобиль!' or driver.find_element(By.CSS_SELECTOR,'#message2').text != 'Вы успешно купили автомобиль!' or driver.find_element(By.CSS_SELECTOR,'#message3').text != 'Вы успешно купили автомобиль!':
        print('Все машины не купишь')
        driver.quit()
    
finally:
    time.sleep(5)
    driver.quit()