import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re

# driver = webdriver.Chrome()
# x = True
# try:
#     driver.get('https://erikdark.github.io/QA_autotests_14/')
#     while x == True:
#         try:
#             btn = driver.find_element(By.ID,'verify').click()
#             message = driver.find_element(By.ID,'verify_message')
#             if 'Verification successful!' in message.text:
#                 print('Yes')
#                 x = False
#                 break
#             else:
#                 continue
#         except:
#             continue
# finally:
#     time.sleep(5)
#     driver.quit()


driver = webdriver.Firefox()
#driver.implicitly_wait(5)

try:
    driver.get('https://erikdark.github.io/Qa_autotest_15/')  
    #btn = driver.find_element(By.ID,'verify').click()
    btn = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID, 'verify'))).click()
    message = driver.find_element(By.ID,'verify_message')
    assert 'Verification successful!' in message.text
finally:
    time.sleep(5)
    driver.quit()
