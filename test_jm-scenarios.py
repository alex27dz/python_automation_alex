from chromedriver_py import binary_path as chromeBinary
from selenium.webdriver.chrome.service import Service

from about_functions import *
from body_functions import *
from business_functions import *
from Generic_functions_modules import *

#chrome_location = "/Users/alexdezho/Downloads/chromedriver"  # chrome_location = 'C:/ChromeDriver/chromedriver'
chromeService_obj = Service(chromeBinary)
ie_location = "C:/ChromeDriver/IEDriverServer"
firefox_location = 'H:/Public/Alex_D_Framework/FireFoxDriver'
edge_location = "C:/ChromeDriver/msedgedriver"
tag = 'chrome'
JM_url = "https://stage.jewelersmutual.com/"
Redirect_url = "https://httpstatus.io/"
layout_builder = "https://stage.jewelersmutual.com/user/login"


def test_01_HomePageToPersonalInsurance():
    if tag == 'chrome':
        print('\nworking with Chrome')
        driver = webdriver.Chrome(service=chromeService_obj)
    else:
        if tag == 'ie':
            print('\nworking with IE')
            driver = webdriver.Ie(ie_location)
        else:
            if tag == 'edge':
                print('\nworking with EDGE')
                driver = webdriver.Edge(edge_location)
            else:
                print('\nworking with FireFox')
                driver = webdriver.Firefox(firefox_location)

    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Personal Insurance')
    url = '/jewelry-engagement-ring-insurance-quote'
    driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Personal Insurance').click()
    time.sleep(10)
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(personal_insurance_body_validation(driver)) == 'True', 'Body elements of Personal insurance - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 01 - PASSED')
    driver.close()
def test_02_HomePageToGetaQuote():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    print('Access GetaQuote')
    url = '/jewelry-engagement-ring-insurance-quote'
    driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Get a Quote').click()
    time.sleep(10)
    assert str(get_a_quote_body_validation(driver)) == 'True', 'Body elements of Get a Quote - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 02 - PASSED')
    driver.close()
def test_03_HomePageToPayMyBill():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    url = '/jewelry-engagement-ring-insurance-quote'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Pay My Bill').click()
    time.sleep(10)
    assert str(pay_my_bill_body_validation(driver)) == 'True', 'Body elements of pay my bill - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 03 - PASSED')
    driver.close()
def test_04_HomePageToClaims():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    print('Access Claims')
    url = '/jewelry-engagement-ring-insurance-quote'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Claims').click()
    time.sleep(10)
    assert str(claims_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 04 - PASSED')
    driver.close()
def test_05_HomePageToManagePolicy():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    print('Access Manage my policy')
    url = '/jewelry-engagement-ring-insurance-quote'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Manage My Policy').click()
    time.sleep(10)
    assert str(manage_my_policy_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 05 - PASSED')
    driver.close()
def test_06_HomePageToBlog():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    print('Access Blog')
    url = '/jewelry-engagement-ring-insurance-quote'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Blog').click()
    time.sleep(10)
    assert str(blog_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 06 - PASSED')
    driver.close()

def test_16_AnswersToJewelryInsurance101():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    print('Access Jewelry Insurance 101')
    url = '/jewelry-insurance-101'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Jewelry Insurance 101').click()
    time.sleep(10)
    assert str(answers_JewelryInsurance101_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 16 - PASSED')
    driver.close()
def test_17_AnswersToFAQ():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    print('Access FAQ')
    url = '/jewelry-insurance-101'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('FAQ').click()
    time.sleep(10)
    assert str(answers_FAQ_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    # assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 17 - PASSED')
    driver.close()
def test_18_AboutUsToAboutUs():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    print('Access About Us')
    url = '/jewelry-insurance-101'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('About Us').click()
    time.sleep(10)
    assert str(aboutus_aboutus_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 18 - PASSED')
    driver.close()
def test_19_AboutUsToSocialResponsibility():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    print('Access SocialResponsibility')
    url = '/jewelry-insurance-101'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Social Responsibility').click()
    time.sleep(10)
    assert str(aboutus_socialresponsibility_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 19 - PASSED')
    driver.close()
def test_20_AboutUsToCareers():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    print('Access Careers')
    url = '/jewelry-insurance-101'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Careers').click()
    time.sleep(10)
    assert str(aboutus_careers_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    # assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 20 - PASSED')
    driver.close()
def test_21_AboutUsToNewsroom():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    print('Access Newsroom')
    url = '/jewelry-insurance-101'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Newsroom').click()
    time.sleep(10)
    assert str(aboutus_newsroom_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 21 - PASSED')
    driver.close()
def test_22_LogInToPersonalJewelry():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    print('Access Personal Jewelry')
    url = 'https://my.testjewelersmutual.com/plportal'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    # driver.find_element_by_link_text('Personal Jewelry').click()
    # time.sleep(10)
    assert str(login_Personal_Jewelry_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 22 - PASSED')
    driver.close()
def test_23_LogInToAgent():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    #assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    #assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Agent')
    url = 'https://my.testjewelersmutual.com/plportal'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    # driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Agent').click()
    time.sleep(10)
    assert str(login_agent_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 23 - PASSED')
    driver.close()
def test_24_LogInToZingPlatform():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    #assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    #assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Zing Platform')
    url = 'https://my.testjewelersmutual.com/plportal'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    # driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Zing Platform').click()
    time.sleep(10)
    assert str(login_ZingPlatform_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 24 - PASSED')
    driver.close()

def test_34_footerToPersonalJewelryInsurance():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Personal Jewelry Insurance')
    driver.find_element_by_link_text('Personal Jewelry Insurance').click()
    time.sleep(10)
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(personal_insurance_body_validation(driver)) == 'True', 'Body elements of Personal insurance - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 34 - PASSED')
    driver.close()
def test_35_footerToGetaQuote():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Get a Quote')
    driver.find_element_by_link_text('Get a Quote').click()
    time.sleep(10)
    assert str(get_a_quote_body_validation(driver)) == 'True', 'Body elements of Get a Quote - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 35 - PASSED')
    driver.close()
def test_36_footerToFAQ():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('FAQ')
    driver.find_element_by_link_text('FAQ').click()
    time.sleep(10)
    assert str(answers_FAQ_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    # assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 36 - PASSED')
    driver.close()
def test_37_footerToManageMyPolicy():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Manage My Policy')
    driver.find_element_by_link_text('Manage My Policy').click()
    time.sleep(10)
    assert str(login_Personal_Jewelry_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 37 - PASSED')
    driver.close()
def test_38_footerToClaims():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Claims')
    driver.find_element_by_link_text('Claims').click()
    time.sleep(10)
    assert str(claims_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 38 - PASSED')
    driver.close()
def test_39_footerToPayMyBill():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Pay My Bill')
    driver.find_element_by_link_text('Pay My Bill').click()
    time.sleep(10)
    assert str(pay_my_bill_body_validation(driver)) == 'True', 'Body elements of pay my bill - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 39 - PASSED')
    driver.close()
def test_40_footerToBusinessInsurance():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Jewelry Business Insurance')
    driver.find_element_by_link_text('Jewelry Business Insurance').click()
    time.sleep(10)
    assert str(business_insurance_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 40 - PASSED')
    driver.close()
def test_41_footerToZingPlatform():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Zing® Platform')
    driver.find_element_by_link_text('Zing® Platform').click()
    time.sleep(10)
    assert str(business_zingplatform_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 41 - PASSED')
    driver.close()
def test_42_footerToJMShippingSolution():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('JM™ Shipping Solution')
    driver.find_element_by_link_text('JM™ Shipping Solution').click()
    time.sleep(10)
    assert str(business_jm_shipping_solution_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 42 - PASSED')
    driver.close()
def test_43_footerToJMCarePlan():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('JM™ Care Plan')
    driver.find_element_by_link_text('JM™ Care Plan').click()
    time.sleep(10)
    assert str(business_jmcareplan_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 43 - PASSED')
    driver.close()
def test_44_footerToJewelryAppraisalSolution():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Jewelry Appraisal Solution')
    driver.find_element_by_link_text('Jewelry Appraisal Solution').click()
    time.sleep(10)
    assert str(business_appraisalsolution_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 44 - PASSED')
    driver.close()
def test_45_footerToJMUniversity():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('JM™ University')
    driver.find_element_by_link_text('JM™ University').click()
    time.sleep(10)
    assert str(body_jmuniversity(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 45 - PASSED')
    driver.close()
def test_46_footerToJewelerPrograms():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Jeweler Programs')
    driver.find_element_by_link_text('Jeweler Programs').click()
    time.sleep(10)
    assert str(business_jewelerprograms_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 46 - PASSED')
    driver.close()
def test_47_footerToPayMyBill():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Pay My Bill')
    driver.find_element_by_link_text('Pay My Bill').click()
    time.sleep(10)
    assert str(business_paymybill_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 47 - PASSED')
    driver.close()
def test_48_footerToBusinessClaims():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Business Claims')
    driver.find_element_by_link_text('Business Claims').click()
    time.sleep(10)
    assert str(business_claims_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 48 - PASSED')
    driver.close()
def test_49_footerToBlog():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Blog')
    driver.find_element_by_link_text('Blog').click()
    time.sleep(10)
    assert str(blog_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 49 - PASSED')
    driver.close()
def test_50_footerToAboutUs():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('About Us')
    driver.find_element_by_link_text('About Us').click()
    time.sleep(10)
    assert str(aboutus_aboutus_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 50 - PASSED')
    driver.close()
def test_51_footerToCareers():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Careers')
    driver.find_element_by_link_text('Careers').click()
    time.sleep(10)
    assert str(aboutus_careers_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    # assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 51 - PASSED')
    driver.close()
def test_52_footerToNewsroom():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Newsroom')
    driver.find_element_by_link_text('Newsroom').click()
    time.sleep(10)
    assert str(aboutus_newsroom_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 52 - PASSED')
    driver.close()
def test_53_footerToSocialResponsibility():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Social Responsibility')
    driver.find_element_by_link_text('Social Responsibility').click()
    time.sleep(10)
    assert str(aboutus_socialresponsibility_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 53 - PASSED')
    driver.close()
def test_54_footerToCOVIDResources():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('COVID-19 Resources')
    driver.find_element_by_link_text('COVID-19 Resources').click()
    time.sleep(10)
    assert str(body_COVIDResources(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 54 - PASSED')
    driver.close()
def test_55_footerToContactUs():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Contact Us')
    driver.find_element_by_link_text('Contact Us').click()
    time.sleep(10)
    assert str(body_ContactUs(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 55 - PASSED')
    driver.close()
def test_56_footerToShareYourConcerns():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Share Your Concerns')
    driver.find_element_by_link_text('Share Your Concerns').click()
    time.sleep(10)
    assert str(body_ShareYourConcerns(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 56 - PASSED')
    driver.close()
def test_57_footerHomuchdoesitcosttoresizearing():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('How much does it cost to resize a ring?')
    driver.find_element_by_link_text('How much does it cost to resize a ring?').click()
    time.sleep(10)
    assert str(body_Homuchdoesitcosttoresizearing(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 57 - PASSED')
    driver.close()
def test_58_footerHowtocleangoldjewelry():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('How to clean gold jewelry the right way')
    driver.find_element_by_link_text('How to clean gold jewelry the right way').click()
    time.sleep(10)
    assert str(body_Howtocleangoldjewelry(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 58 - PASSED')
    driver.close()
def test_59_footerHowmuchshouldcost():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('How much should an appraisal cost?')
    driver.find_element_by_link_text('How much should an appraisal cost?').click()
    time.sleep(10)
    assert str(body_Howmuchshouldcost(driver)) == 'True', 'Body elements of claims - not found'
    # assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 59 - PASSED')
    driver.close()
def test_60_footerHowtomakearing():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('How to make a ring smaller without resizing')
    driver.find_element_by_link_text('How to make a ring smaller without resizing').click()
    time.sleep(10)
    assert str(body_Howtomakearing(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 60 - PASSED')
    driver.close()
def test_61_footerMoreblogarticles():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('More blog articles')
    driver.find_element_by_link_text('More blog articles').click()
    time.sleep(10)
    assert str(body_Moreblogarticles(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 61 - PASSED')
    driver.close()
def test_62_footerToPrivacyPolicy():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Privacy Policy')
    driver.find_element_by_link_text('Privacy Policy').click()
    time.sleep(10)
    assert str(body_PrivacyPolicy(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 62 - PASSED')
    driver.close()
def test_63_footerToTermsofUse():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Terms of Use')
    driver.find_element_by_link_text('Terms of Use').click()
    time.sleep(10)
    assert str(body_TermsofUse(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 63 - PASSED')
    driver.close()

def test_66_Additional_link_engagementringinsurance():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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

    driver.get('https://www.jewelersmutual.com/engagement-ring-insurance')
    driver.maximize_window()
    time.sleep(10)
    assert str(body_engagementringinsurance(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 66 - PASSED')
    driver.close()
def test_70_Additional_link_adiamor():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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

    driver.get('https://www.jewelersmutual.com/adiamor')
    driver.maximize_window()
    time.sleep(10)
    assert str(body_adiamor(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 70 - PASSED')
    driver.close()
def test_71_Additional_link_briangavindiamonds():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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

    driver.get('https://www.jewelersmutual.com/briangavindiamonds')
    driver.maximize_window()
    time.sleep(10)
    assert str(body_briangavindiamonds(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 71 - PASSED')
    driver.close()
def test_72_Additional_link_jamesallen():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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

    driver.get('https://www.jewelersmutual.com/jamesallen')
    driver.maximize_window()
    time.sleep(10)
    assert str(body_jamesallen(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 72 - PASSED')
    driver.close()
def test_73_Additional_link_bluenile():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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

    driver.get('https://www.jewelersmutual.com/bluenile')
    driver.maximize_window()
    time.sleep(10)
    assert str(body_bluenile(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 73 - PASSED')
    driver.close()
def test_74_Additional_link_whiteflash():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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

    driver.get('https://www.jewelersmutual.com/whiteflash')
    driver.maximize_window()
    time.sleep(10)
    assert str(body_whiteflash(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 74 - PASSED')
    driver.close()
def test_76_Additional_link_watchinsurance():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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

    driver.get('https://www.jewelersmutual.com/watch-insurance')
    driver.maximize_window()
    time.sleep(10)
    assert str(body_watchinsurance(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 76 - PASSED')
    driver.close()
def test_80_Additional_link_howtocleanandcareforyourdiamondring():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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

    driver.get('https://www.jewelersmutual.com/how-to-clean-and-care-for-your-diamond-ring')
    driver.maximize_window()
    time.sleep(10)
    assert str(body_howtocleanandcareforyourdiamondring(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 80 - PASSED')
    driver.close()
def test_81_Additional_link_weinsurejewelry():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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

    driver.get('https://www.jewelersmutual.com/we-insure-jewelry')
    driver.maximize_window()
    time.sleep(10)
    assert str(body_weinsurejewelry(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 81 - PASSED')
    driver.close()
def test_82_Additional_link_coronavirusBusiness():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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

    driver.get('https://www.jewelersmutual.com/coronavirus-businesses')
    driver.maximize_window()
    time.sleep(10)
    assert str(body_coronavirusBusiness(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 82 - PASSED')
    driver.close()
def test_83_Additional_link_GuidetoJewelryInsurance():
    if tag == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
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

    driver.get('https://www.jewelersmutual.com/jewelry-insurance-guide')
    driver.maximize_window()
    time.sleep(10)
    assert str(body_GuidetoJewelryInsurance(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 83 - PASSED')
    driver.close()