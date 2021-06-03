from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from configparser import ConfigParser
import requests
import json

CONFIG = ConfigParser()
CONFIG.read('config.ini')

driverpath = CONFIG.get('MAIN', 'DRIVER_LOCATION')
url = CONFIG.get('ORDER', 'URL')
print('********AutoBuy for Realme.in Flash sales******')
driver = webdriver.Chrome(driverpath)
driver.maximize_window()
driver.get(url)
input('Please Login on the window and then press enter here')

def buy_check():
    try:
        nobuyoption = True
        while nobuyoption:
            try:
                driver.refresh()
                time.sleep(0.5)
                t = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[6]/div[3]/a[2]')
                t.click()
                buyprod = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[13]/div[2]/div[2]/a[2]')
                print('Adding to Cart: ' + time.ctime())
                quan = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div[6]/div[4]/div/a[2]/span')
                quan.click()
                nobuyoption = False
            except:
                nobuyoption = True
                print('Wait: ' + time.ctime())
        buyprod.click()
        print('Next button Clicked: ' +  time.ctime())
       # buy_recheck()
    except:
        print('buy_check Failed. Retrying: ' + time.ctime())
        time.sleep(1)
        buy_check()
        
def buy_recheck():        
    try:
       # WebDriverWait(driver, 4).until(EC.element_to_be_clickable(find_element_by(By.XPATH,'//*[@id="app"]/div[2]/div[6]/div/div/div[2]/a'))
        print('Wait')
    except:
        print('Wait')
        time.sleep(0.5)	
        buy_check()

def deliver_continue():
    try:
        addr_sal_avl = True
        while addr_sal_avl:
            try:
                time.sleep(0.5)
                address_sel = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[6]/div/div/div[2]/a')
                address_sel.click()
                addr_sal_avl = False
                print('In Stock')
            except:
                addr_sal_avl = True
                print('Wait')
        print('In Stock')
    except:
        buy_check()

def run_script():
    buy_check()
    deliver_continue()


if __name__ == "__main__":
   run_script()
