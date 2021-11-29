from selenium import webdriver
from selenium.webdriver.common.by import By

import logging
import time

logger = logging.getLogger('simple_example')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driverChrome = webdriver.Chrome(executable_path='C:/Users/u6071468/PycharmProjects/TAU/chromedriver.exe')

logger.info('Przechodzę na stronę Zalando')
driverChrome.get('https://www.zalando.pl/')
temp = driverChrome.find_element(By.CLASS_NAME, 'z-navicat-header_navToolItemLink')
temp.click()
logger.warning('Jakieś ostrzeżenie')
time.sleep(2)

temp = driverChrome.find_element(By.ID, 'login.email')
temp.click()
time.sleep(2)
temp.send_keys("login")
logger.error('Jakiś Error')
time.sleep(2)

temp = driverChrome.find_element(By.XPATH, '//*[@id="sso"]/div/div[2]/main/div/div[2]/div/div/div/div/a')
temp.click()
time.sleep(2)
driverChrome.close()
