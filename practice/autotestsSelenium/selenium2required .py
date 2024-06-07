import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import string

# try:
#     driver = webdriver.Chrome()
#     driver.get('https://easysmarthub.ru/blog/')
#     findlink = driver.find_element(By.LINK_TEXT, "Что такое базы данных?")
#     findlink.click()
#     time.sleep(5)
#     findlink = driver.find_element(By.LINK_TEXT, "Эрик Спичак")
#     findlink.click()
#     time.sleep(5)
# except Exception as ex:
#     print(ex)
# finally:
#     driver.quit()

# try:
#     driver = webdriver.Chrome()
#     driver.get('https://erikdark.github.io/Qa_autotest_02/')
#     input1 = driver.find_elements(By.CSS_SELECTOR, 'input')
#     for i in input1:
#         i.send_keys('Lena')
#     btn = driver.find_element(By.ID, 'submitBtn')
#     btn.click()
#     time.sleep(5)
# except Exception as ex:
#     print(ex)
# finally:
#     driver.quit()

# try:
#     driver = webdriver.Chrome()
#     driver.get('https://erikdark.github.io/Qa_autotest_03/')
#     data1 = ['lena','lena','lena123@gmail.com','+79111111111','lena']
#     input1 = driver.find_elements(By.CSS_SELECTOR, 'input')
#     for i,ii in zip(input1,data1):
#         i.send_keys(ii)
#     time.sleep(2)
# except Exception as ex:
#     print(ex)
# try:
#     btn = driver.find_element(By.CSS_SELECTOR, "button")
#     btn.click()
#     time.sleep(2)
# except Exception as ex:
#     print(ex)
# cong = driver.find_element(By.TAG_NAME, "h2")
# cong_text = cong.text
# message = "no"
# assert cong_text == "Поздравляю, вы прошли первый уровень.", message
# driver.quit()


# #required 1,2,3
# # [required] or input:required

# #checkrequired 
# try:
#     driver = webdriver.Chrome()
#     driver.get('https://erikdark.github.io/Qa_autotest_03/')
#     input1 = driver.find_element(By.CSS_SELECTOR, '#firstName')
#     input1.send_keys('lena')
#     input2 = driver.find_element(By.CSS_SELECTOR, '#lastName')
#     input2.send_keys('lena')
#     input3 = driver.find_element(By.CSS_SELECTOR, '#email')
#     input3.send_keys('lena123@gmail.com')
#     time.sleep(2)
#     btn = driver.find_element(By.CSS_SELECTOR, "button")
#     btn.click()
#     time.sleep(2)
# except Exception as ex:
#     print(ex)
# cong = driver.find_element(By.TAG_NAME, "h2")
# cong_text = cong.text
# message = "no"
# assert cong_text == "Поздравляю, вы прошли первый уровень.", message
# driver.quit()

# #checknorequired 
# try:
#     driver = webdriver.Chrome()
#     driver.get('https://erikdark.github.io/Qa_autotest_03/')
#     input4 = driver.find_element(By.CSS_SELECTOR, '#phone')
#     input4.send_keys('+79111111111')
#     input5 = driver.find_element(By.CSS_SELECTOR, '#address')
#     input5.send_keys('lena')
#     time.sleep(2)
#     btn = driver.find_element(By.CSS_SELECTOR, "button")
#     btn.click()
#     time.sleep(2)
# except Exception as ex:
#     print(ex)
# cong = driver.find_element(By.TAG_NAME, "h2")
# cong_text = cong.text
# message = "no"
# assert cong_text == "Поздравляю, вы прошли первый уровень.", message
# driver.quit()


# try:
#     driver = webdriver.Chrome()
#     mystr = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890!@#$%^&*,.=-+'
#     mylst = list(mystr)
#     for i in mylst:
#         driver.get('https://erikdark.github.io/Qa_autotest_04/')
#         input1 = driver.find_element(By.CSS_SELECTOR, '#firstName')
#         input1.send_keys(i)
#         time.sleep(2)
# except Exception as ex:
#     print(ex)


# try:
#     driver = webdriver.Chrome()
#     driver.get('https://erikdark.github.io/Qa_autotests_05/')
#     cong = driver.find_element(By.CSS_SELECTOR, "#challenge")
#     cong_text = cong.text
#     textwithoutpunct = re.sub(r'[^\w\s]', '', cong_text)
#     listtext = textwithoutpunct.split()
#     a = int(listtext[2])
#     b = int(listtext[3])
#     c = a+b
#     input1 = driver.find_element(By.CSS_SELECTOR, "#answer")
#     input1.send_keys(c)
#     btn1 = driver.find_element(By.CSS_SELECTOR, "#notRobot")
#     btn1.click()
#     btn2 = driver.find_element(By.CSS_SELECTOR, "#cool")
#     btn2.click()
#     time.sleep(1)
#     btn3 = driver.find_element(By.CSS_SELECTOR, "#submitBtn")
#     btn3.click()
#     time.sleep(2)
#     cong2 = driver.find_element(By.CSS_SELECTOR, "#message")
#     cong2_text = cong2.text
#     message = "no"
#     assert cong2_text == "Поздравляю, Elon Musk!", message
# except Exception as ex:
#      print(ex)

# driver.quit()

# try:
#     driver = webdriver.Chrome()
#     driver.get('https://erikdark.github.io/Qa_autotest_07/')
#     nums = driver.find_element(By.CSS_SELECTOR,'#numberImage')
#     b = nums.get_attribute('data-b')
#     blist = b.split('?')
#     sum = int(blist[0]) + int(blist[1])
#     input1 = driver.find_element(By.CSS_SELECTOR, '#answer')
#     input1.send_keys(sum)
#     time.sleep(1)
#     btn3 = driver.find_element(By.CSS_SELECTOR, "#submitBtn")
#     btn3.click()
#     time.sleep(2)
# except Exception as ex:
#      print(ex)

# driver.quit()

### 7 dif
try:
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/Qa_autotest_07/')
    numb = driver.find_element(By.CSS_SELECTOR,'#numberImage')
    b = numb.get_attribute('data-b')
    numa = driver.find_element(By.CSS_SELECTOR,'#challenge').text
    numal = numa.split()
    sum1 = int(b) + int(numal[2])
    input1 = driver.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(sum1)
    time.sleep(1)
    btn3 = driver.find_element(By.CSS_SELECTOR, "#submitBtn")
    btn3.click()
    time.sleep(2)
except Exception as ex:
     print(ex)

driver.quit()

try:
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/QA_autotests_08/')


except Exception as ex:
     print(ex)

driver.quit()
