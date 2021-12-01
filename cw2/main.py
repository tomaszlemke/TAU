from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging
import time

logger = logging.getLogger('simple_example')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# driverChrome = webdriver.Chrome(executable_path='C:/Users/u6071468/PycharmProjects/TAU/chromedriver.exe')


# logger.info('Przechodzę na stronę Zalando')
# driverChrome.get('https://www.zalando.pl/')
# temp = driverChrome.find_element(By.CLASS_NAME, 'z-navicat-header_navToolItemLink')
# temp.click()
# logger.info('Przechodzę na stronę logowania')
# time.sleep(2)
#
# temp = driverChrome.find_element(By.ID, 'login.email')
# temp.click()
# time.sleep(2)
# temp.send_keys("login")
# logger.info('Sprawdzam funkcjonalność "Zapomniałem Hasło"')
# time.sleep(2)
#
# temp = driverChrome.find_element(By.XPATH, '//*[@id="sso"]/div/div[2]/main/div/div[2]/div/div/div/div/a')
# temp.click()
# time.sleep(2)
#
#
# logger.info('Sprawdzam walidację formatu adresu email')
# temp = driverChrome.find_element(By.XPATH, '//*[@id="sso"]/div/div[2]/main/div/div[2]/div/div[1]/form/button/span')
# temp.click()
# time.sleep(2)
#
# driverChrome.close()
# -----------------------------------------------------------------------------
# driverFireFox = webdriver.Firefox(executable_path='C:/Users/u6071468/PycharmProjects/TAU/geckodriver.exe')
#
# logger.info('Przechodzę na stronę Zalando')
# driverFireFox.get('https://www.zalando.pl/')
# temp = driverFireFox.find_element(By.CLASS_NAME, 'z-navicat-header_navToolItemLink')
# temp.click()
# logger.info('Przechodzę na stronę logowania')
# time.sleep(2)
#
# temp = driverFireFox.find_element(By.ID, 'login.email')
#
# temp.click()
# time.sleep(2)
# temp.send_keys("login")
# logger.info('Sprawdzam funkcjonalność "Zapomniałem Hasło"')
# time.sleep(2)
#
# temp = driverFireFox.find_element(By.XPATH, '//*[@id="sso"]/div/div[2]/main/div/div[2]/div/div/div/div/a')
# temp.click()
# time.sleep(2)
#
#
# logger.info('Sprawdzam walidację formatu adresu email')
# temp = driverFireFox.find_element(By.XPATH, '//*[@id="sso"]/div/div[2]/main/div/div[2]/div/div[1]/form/button/span')
# temp.click()
# time.sleep(2)
#
# driverFireFox.close()

driverChrome = webdriver.Chrome(executable_path='C:/Users/u6071468/PycharmProjects/TAU/chromedriver.exe')

logger.info('Przechodzę na stronę Sklepu NewBalance')
driverChrome.get('https://nbsklep.pl/')

try:
    temp = WebDriverWait(driverChrome, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/app-root/app-menu/app-menu-mobile-newbalance/app-cookies-newbalance/div/div/div/div[2]/div/div[2]/span[2]')))
    temp.click()

finally:
    logger.info('Cookies done')

try:
    temp = WebDriverWait(driverChrome, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="popupContainer"]/div[1]/img')))
    temp.click()
finally:
    logger.info('Newsletter exit')

try:
    temp = WebDriverWait(driverChrome, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-menu/app-menu-mobile-newbalance/ul/li[2]/a[1]')))
    temp.click()
finally:
    logger.info('Otwieram Search bar')

try:
    temp = WebDriverWait(driverChrome, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/app-root/app-menu/app-menu-mobile-newbalance/div/div[2]/div/app-searcher-default/form/input')))
    temp.click()

finally:
    logger.info('Focus na search bar')

try:
    temp = WebDriverWait(driverChrome, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/app-root/app-menu/app-menu-mobile-newbalance/div/div[2]/div/app-searcher-default/form/input')))
    temp.send_keys('ML574HA2')

finally:
    logger.info('Wprowadzam kod')

try:
    temp = WebDriverWait(driverChrome, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/app-root/app-menu/app-menu-mobile-newbalance/div/div[2]/div/app-searcher-default/button/span[1]')))
    temp.click()

finally:
    logger.info('Szukam')

try:
    temp = WebDriverWait(driverChrome, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/app-root/app-content-page-newbalance/div/div/ul[2]/li[1]/div/div/div[2]/a/div[1]/nb-img/img')))
    temp.click()

finally:
    logger.info('Otwieram okno produktu')

try:
    temp = WebDriverWait(driverChrome, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                 '/html/body/app-root/app-product-newbalance/div[2]/div[1]/div[1]/div[2]/app-product-form-newbalance/form/ul/li[1]/div/app-price-default/div/div/em/b')))
    cena = temp.text
finally:
    logger.info('Pobralem cene produktu')

cena = cena[:-3]
if int(cena) < 200:
    logger.info('Kupuj')
else:
    logger.info('Poczekaj az bedzie taniej')
