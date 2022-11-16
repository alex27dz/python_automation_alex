import time  # using sleep time
from selenium import webdriver  # selenium framework for web elements actions

# google chrome webdriver location
chrome_location = '/Users/alexdezho/Documents/Personal/chromedriver'

# simple scenario as a function
def regular_test_scenario():
    driver = webdriver.Chrome(chrome_location)
    driver.get('https://google.com/')
    driver.maximize_window()
    time.sleep(3)
    driver.close()


# simple scenario as a pytest function
def test_01_hi():
    driver = webdriver.Chrome(chrome_location)
    driver.get('https://google.com/')
    driver.maximize_window()
    time.sleep(3)
    driver.close()

# calling the regular function
# regular_test_scenario()

