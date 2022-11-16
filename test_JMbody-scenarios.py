from body_functions import *
from chromedriver_py import binary_path as chromeBinary
from selenium.webdriver.chrome.service import Service

# chrome_location = "/Users/alexdezho/Downloads/chromedriver"  # chrome_location = 'C:/ChromeDriver/chromedriver'
chromeService_obj = Service(chromeBinary)

tag = 'chrome'
JM_url = "https://stage.jewelersmutual.com/"
Redirect_url = "https://httpstatus.io/"
layout_builder = "https://stage.jewelersmutual.com/user/login"


def test_25_BodyToPersonalInsurance():
    if tag == 'chrome':
        driver = webdriver.Chrome(chrome_location)
        print('working with Chrome')
    else:
        if tag == 'ie':
            driver = webdriver.Ie(ie_location)
            print('working with IE')
        else:
            if tag == 'edge':
                driver = webdriver.Edge(edge_location)
                print('working with EDGE')
            else:
                driver = webdriver.Firefox(firefox_location)
                print('working with FireFox')

    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(3)
    print('Access Personal Insurance')
    driver.find_element_by_partial_link_text(
        'EXPLORE PERSONAL JEWELRY INSURANCE').click()
    time.sleep(10)
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    assert str(personal_insurance_body_validation(driver)
               ) == 'True', 'Body elements of Personal insurance - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 25 - PASSED')
    driver.close()


def test_26_BodyToLogIn():
    if tag == 'chrome':
        driver = webdriver.Chrome(chrome_location)
        print('working with Chrome')
    else:
        if tag == 'ie':
            driver = webdriver.Ie(ie_location)
            print('working with IE')
        else:
            if tag == 'edge':
                driver = webdriver.Edge(edge_location)
                print('working with EDGE')
            else:
                driver = webdriver.Firefox(firefox_location)
                print('working with FireFox')

    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(3)
    print('Access Log in')
    driver.find_element_by_partial_link_text('Log in').click()
    time.sleep(10)
    assert str(login_Personal_Jewelry_body_validation(driver)
               ) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 26 - PASSED')
    driver.close()


def test_27_BodyToRegisterForAnOnlineAccount():
    if tag == 'chrome':
        driver = webdriver.Chrome(chrome_location)
        print('working with Chrome')
    else:
        if tag == 'ie':
            driver = webdriver.Ie(ie_location)
            print('working with IE')
        else:
            if tag == 'edge':
                driver = webdriver.Edge(edge_location)
                print('working with EDGE')
            else:
                driver = webdriver.Firefox(firefox_location)
                print('working with FireFox')

    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(3)
    print('Access BodyToRegisterForAnOnlineAccount')
    driver.find_element_by_partial_link_text(
        'Register for an online account').click()
    # stopped here
    time.sleep(10)
    assert str(body_ToRegisterForAnOnlineAccount(driver)
               ) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 27 - PASSED')
    driver.close()


def test_28_BodyToAddanitemtomyPolicy():
    if tag == 'chrome':
        driver = webdriver.Chrome(chrome_location)
        print('working with Chrome')
    else:
        if tag == 'ie':
            driver = webdriver.Ie(ie_location)
            print('working with IE')
        else:
            if tag == 'edge':
                driver = webdriver.Edge(edge_location)
                print('working with EDGE')
            else:
                driver = webdriver.Firefox(firefox_location)
                print('working with FireFox')

    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(3)
    print('Access Add an item to my policy')
    driver.find_element_by_partial_link_text(
        'Add an item to my policy').click()
    time.sleep(10)
    assert str(login_Personal_Jewelry_body_validation(driver)
               ) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 28 - PASSED')
    driver.close()


def test_29_BodyTopaymybill():
    if tag == 'chrome':
        driver = webdriver.Chrome(chrome_location)
        print('working with Chrome')
    else:
        if tag == 'ie':
            driver = webdriver.Ie(ie_location)
            print('working with IE')
        else:
            if tag == 'edge':
                driver = webdriver.Edge(edge_location)
                print('working with EDGE')
            else:
                driver = webdriver.Firefox(firefox_location)
                print('working with FireFox')

    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(3)
    print('Access Pay My Bill')
    driver.find_element_by_partial_link_text('Pay My Bill').click()
    time.sleep(10)
    assert str(pay_my_bill_body_validation(driver)
               ) == 'True', 'Body elements of pay my bill - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 29 - PASSED')
    driver.close()


def test_31_BodyToLearnaboutclaims():
    if tag == 'chrome':
        driver = webdriver.Chrome(chrome_location)
        print('working with Chrome')
    else:
        if tag == 'ie':
            driver = webdriver.Ie(ie_location)
            print('working with IE')
        else:
            if tag == 'edge':
                driver = webdriver.Edge(edge_location)
                print('working with EDGE')
            else:
                driver = webdriver.Firefox(firefox_location)
                print('working with FireFox')

    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(3)
    print('Learn about claims')
    driver.find_element_by_partial_link_text('Learn about claims').click()
    time.sleep(10)
    assert str(claims_body_validation(driver)
               ) == 'True', 'Body elements of claims - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 31 - PASSED')
    driver.close()


def test_32_BodyToGetaquoteformultipleItems():
    if tag == 'chrome':
        driver = webdriver.Chrome(chrome_location)
        print('working with Chrome')
    else:
        if tag == 'ie':
            driver = webdriver.Ie(ie_location)
            print('working with IE')
        else:
            if tag == 'edge':
                driver = webdriver.Edge(edge_location)
                print('working with EDGE')
            else:
                driver = webdriver.Firefox(firefox_location)
                print('working with FireFox')

    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,400)")
    time.sleep(3)
    print('Get a quote for multiple items')
    driver.find_element_by_partial_link_text(
        'Get a quote for multiple items').click()
    time.sleep(10)
    assert str(get_a_quote_body_validation(driver)
               ) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 32 - PASSED')
    driver.close()


def test_33_BodyToExplorePersonalJewelryInsurance():
    if tag == 'chrome':
        driver = webdriver.Chrome(chrome_location)
        print('working with Chrome')
    else:
        if tag == 'ie':
            driver = webdriver.Ie(ie_location)
            print('working with IE')
        else:
            if tag == 'edge':
                driver = webdriver.Edge(edge_location)
                print('working with EDGE')
            else:
                driver = webdriver.Firefox(firefox_location)
                print('working with FireFox')

    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,800)")
    time.sleep(3)
    print('EXPLORE PERSONAL JEWELRY INSURANCE')
    driver.find_element_by_partial_link_text(
        'EXPLORE PERSONAL JEWELRY INSURANCE').click()
    time.sleep(10)
    assert str(personal_insurance_body_validation(driver)
               ) == 'True', 'Body elements of claims - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 33 - PASSED')
    driver.close()
