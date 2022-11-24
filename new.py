# (Michael, Alex) - Simple automation tests using: selenium, pytest, python
import time  # using sleep time
from selenium import webdriver  # selenium framework for web elements actions
from selenium.webdriver.common.keys import Keys   # for using enter and return
chrome_location = '/Users/alexdezho/Documents/Personal/chromedriver'  # Google Chrome webdriver location


def regular_test_scenario():  # example 1 - simple scenario as a function
    driver = webdriver.Chrome(chrome_location)
    driver.get('https://google.com/')
    driver.maximize_window()
    time.sleep(3)
    googlesearch = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'  # search element
    driver.find_element_by_xpath(googlesearch).click()
    driver.find_element_by_xpath(googlesearch).send_keys('Michael is the best developer')
    driver.find_element_by_xpath(googlesearch).send_keys(Keys.ENTER)
    time.sleep(5)
    driver.close()
    print('first example')


def test_01_itsmyfirsttest():  # example 2 - simple scenario as a pytest function
    driver = webdriver.Chrome(chrome_location)
    driver.get('https://google.com/')
    driver.maximize_window()
    time.sleep(3)
    driver.close()
    print('second example')


def test_02_itsmysecondtest():  # example 3 - simple scenario as a pytest function using regular function
    regular_test_scenario()  # calling the function
    print('third example')



