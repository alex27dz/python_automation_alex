from business_functions import *
from chromedriver_py import binary_path as chromeBinary
from selenium.webdriver.chrome.service import Service

chromeService_obj = Service(chromeBinary)

tag = 'chrome'
JM_url = "https://stage.jewelersmutual.com/"
Redirect_url = "https://httpstatus.io/"
layout_builder = "https://stage.jewelersmutual.com/user/login"

def test_07_BusinessToBusinessInsurance():
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access BusinessInsurance')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Business Insurance').click()
    time.sleep(10)
    assert str(business_insurance_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 07 - PASSED')
    driver.close()
def test_08_BusinessToClaims():
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Businessclaims')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Claims').click()
    time.sleep(10)
    assert str(business_claims_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    # assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 08 - PASSED')
    driver.close()
def test_09_BusinessToPayMyBill():
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access PayMyBill')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Pay My Bill').click()
    time.sleep(10)
    assert str(business_paymybill_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    # assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    # assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 09 - PASSED')
    driver.close()
def test_10_BusinessToZingPlatform():
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Zing Platform')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Zing Platform').click()
    time.sleep(10)
    assert str(business_zingplatform_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 10 - PASSED')
    driver.close()
def test_11_BusinessToShippingSolution():
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access JM Shipping Solution')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('JM Shipping Solution').click()
    time.sleep(10)
    assert str(business_jm_shipping_solution_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    # assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 11 - PASSED')
    driver.close()
def test_12_BusinessToJmCarePlan():
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access JM Care Plan')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('JM Care Plan').click()
    time.sleep(10)
    assert str(business_jmcareplan_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 12 - PASSED')
    driver.close()
def test_13_BusinessToAppraisalSolution():
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Appraisal Solution')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Appraisal Solution').click()
    time.sleep(10)
    assert str(business_appraisalsolution_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 13 - PASSED')
    driver.close()
def test_14_BusinessToJewelerPrograms():
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access JewelerPrograms')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Jeweler Programs').click()
    time.sleep(10)
    assert str(business_jewelerprograms_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 14 - PASSED')
    driver.close()
def test_15_BusinessToPawnbrokers():
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Pawnbrokers')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Pawnbrokers').click()
    time.sleep(10)
    assert str(business_pawnbrokers_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 15 - PASSED')
    driver.close()