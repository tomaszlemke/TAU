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
time.sleep(4)
temp = driverChrome.find_element(By.CLASS_NAME, 'btn--cookies')
time.sleep(2)
temp.click()
time.sleep(2)

# temp = driverChrome.find_element(By.XPATH, '/html/body/app-root/app-menu/app-menu-mobile-newbalance/ul/li[2]/a[1]')
# temp.click()
# time.sleep(2)

temp = driverChrome.find_element(By.XPATH, '//*[@id="popupContainer"]/div[1]/img')
time.sleep(2)
temp.click()

temp = driverChrome.find_element(By.CLASS_NAME, 'searcher-input')
time.sleep(2)
temp.click()
time.sleep(1)

temp.send_keys('ML574HA2')

temp = driverChrome.find_element(By.CLASS_NAME, 'icon-search')
time.sleep(2)
temp.click()
time.sleep(4)

temp = driverChrome.find_element(By.XPATH, '/html/body/app-root/app-content-page-newbalance/div/div/ul[2]/li[1]/div/div/div[2]/a/div[1]/nb-img/img')
time.sleep(2)
temp.click()
time.sleep(4)

temp = driverChrome.find_element(By.XPATH, '/html/body/app-root/app-product-newbalance/div[2]/div[1]/div[1]/div[2]/app-product-form-newbalance/form/ul/li[1]/div/app-price-default/div/div/em/b')
cena = temp.text
cena = cena[:-3]
if int(cena) < 200:
    logger.info('Kupuj')
else:
    logger.info('Poczekaj az bedzie taniej')