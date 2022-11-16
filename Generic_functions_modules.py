import datetime
import json  # working with json dicts
import logging
import pprint
# import names
import time
import urllib.request
from datetime import date
import pytest
import requests
from requests.structures import CaseInsensitiveDict
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

# JM website
JM_url = "https://stage.jewelersmutual.com/"
Redirect_url = "https://httpstatus.io/"
layout_builder = "https://stage.jewelersmutual.com/user/login"

# Drivers location + links & environments ------------------------
# chrome_location_mac = "/Users/alexdezho/Documents/Personal/chromedriver"
chrome_location = '/Users/alexdezho/Documents/Personal/chromedriver'
firefox_location = 'executable_path="C:\\geckodriver.exe"'
ie_location = "C:/IEDriver/IEDriverServer/IEDriverServer"
edge_location = "C:/msedgedriver"

# QA7
qna_regular_QA7 = 'http://mytest07.jewelersnt.local/jewelry-insurance-quote-apply/t/Pa_sa8WRd0W_k02oCEi6cQ'
gw_policy_center_QA7 = 'http://jmtgpc07/pc/PolicyCensuter.do'
qna_internal_QA7 = 'http://jmtapp07/QuoteApply/Internal'

# QA4
qna_regular_QA4 = 'http://mytest04.jewelersnt.local/jewelry-insurance-quote-apply/'
gw_policy_center_QA4 = 'http://jmtgpc04/pc/PolicyCenter.do'
qna_internal_QA4 = 'http://jmtapp04/QuoteApply/Internal'

# Items dictionary
conviction = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
item = {
    "Ring": "jewelry-itemType-1",
    "Earrings": "jewelry-itemType-2",
    "Bracelet": "jewelry-itemType-3",
    "Necklace": "jewelry-itemType-4",
    "Watch": "jewelry-itemType-5",
    "Pendant": "jewelry-itemType-6",
    "Chain": "jewelry-itemType-7",
    "Other": "jewelry-itemType-8",
    "Loose stone": "jewelry-itemType-9",
    "Brooch": "jewelry-itemType-10"
}

def navbar_validation(driver):
    driver.execute_script("window.scrollTo(0,0)")
    print('verifying Navbar containers')
    url = '/jewelry-engagement-ring-insurance-quote'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@href="'+url+'"]')))
    print('Navbar Personal')

    if driver.current_url == 'https://stage.jewelersmutualalex.com/':
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(2)
        print(driver.find_element_by_link_text('Personal Insurance').text)
        print(driver.find_element_by_link_text('Get a Quote').text)
        print(driver.find_element_by_link_text('Pay My Bill').text)
        print(driver.find_element_by_link_text('Claims').text)
        print(driver.find_element_by_link_text('Manage My Policy').text)
        print(driver.find_element_by_link_text('Blog').text)
        print('Navbar Personal passed')

        print('Navbar Business')
        url = '/jewelry-business-jewelers-block-bop-insurance'
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(2)
        print(driver.find_element_by_link_text('Business Insurance').text)
        print(driver.find_element_by_link_text('Claims').text)
        print(driver.find_element_by_link_text('Pay My Bill').text)
        print(driver.find_element_by_link_text('Zing Platform').text)
        print(driver.find_element_by_link_text('JM Shipping Solution').text)
        print(driver.find_element_by_link_text('JM Care Plan').text)
        print(driver.find_element_by_link_text('Jeweler Programs').text)
        print(driver.find_element_by_link_text('Pawnbrokers').text)
        print('Navbar Business passed')

        print('Navbar Answers')
        url = '/jewelry-insurance-101'
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(2)
        print(driver.find_element_by_link_text('Jewelry Insurance 101').text)
        print(driver.find_element_by_link_text('FAQ').text)
        print('Navbar Answers passed')

        print('Navbar About Us')
        url = '/about-us'
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(2)
        print(driver.find_element_by_link_text('About Us').text)
        print(driver.find_element_by_link_text('Social Responsibility').text)
        print(driver.find_element_by_link_text('Careers').text)
        print(driver.find_element_by_link_text('Newsroom').text)
        print('Navbar About Us passed')

        print('Navbar Log In')
        try:
            driver.find_element_by_xpath('//a[contains(@href,"https://my.jewelersmutual.com/PLPortal/Security/")]').click()
            time.sleep(2)
        except:
            driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-main-menu"]/ul/div/li[5]/a').click()
            time.sleep(2)

        print(driver.find_element_by_link_text('Personal Jewelry').text)
        print(driver.find_element_by_link_text('Agent').text)
        print(driver.find_element_by_link_text('Zing Platform').text)
        print('Navbar Log In passed')

    else:
        print('Navbar Personal')
        url = '/jewelry-engagement-ring-insurance-quote'
        action = webdriver.ActionChains(driver)
        element = driver.find_element_by_xpath('//a[@href="' + url + '"]')  # or your another selector here
        action.move_to_element(element)
        action.perform()
        time.sleep(3)
        print(driver.find_element_by_link_text('Personal Insurance').text)
        print(driver.find_element_by_link_text('Get a Quote').text)
        print(driver.find_element_by_link_text('Pay My Bill').text)
        print(driver.find_element_by_link_text('Claims').text)
        print(driver.find_element_by_link_text('Manage My Policy').text)
        print(driver.find_element_by_link_text('Blog').text)
        print('Navbar Personal passed')

        print('Navbar Business')
        url = '/jewelry-business-jewelers-block-bop-insurance'
        action = webdriver.ActionChains(driver)
        element = driver.find_element_by_xpath('//a[@href="' + url + '"]') # or your another selector here
        action.move_to_element(element)
        action.perform()
        time.sleep(2)
        print(driver.find_element_by_link_text('Business Insurance').text)
        print(driver.find_element_by_link_text('Claims').text)
        print(driver.find_element_by_link_text('Pay My Bill').text)
        # print(driver.find_element_by_link_text('Zing Platform').text)
        print(driver.find_element_by_link_text('JM Shipping Solution').text)
        print(driver.find_element_by_link_text('JM Care Plan').text)
        print(driver.find_element_by_link_text('Jeweler Programs').text)
        print(driver.find_element_by_link_text('Pawnbrokers').text)
        print('Navbar Business passed')

        print('Navbar Answers')
        url = '/jewelry-insurance-101'
        action = webdriver.ActionChains(driver)
        element = driver.find_element_by_xpath('//a[@href="' + url + '"]')  # or your another selector here
        action.move_to_element(element)
        action.perform()
        time.sleep(2)
        print(driver.find_element_by_link_text('Jewelry Insurance 101').text)
        print(driver.find_element_by_link_text('FAQ').text)
        print('Navbar Answers passed')

        print('Navbar About Us')
        url = '/about-us'
        action = webdriver.ActionChains(driver)
        element = driver.find_element_by_xpath('//a[@href="' + url + '"]')  # or your another selector here
        action.move_to_element(element)
        action.perform()
        time.sleep(2)
        print(driver.find_element_by_link_text('About Us').text)
        print(driver.find_element_by_link_text('Social Responsibility').text)
        print(driver.find_element_by_link_text('Careers').text)
        print(driver.find_element_by_link_text('Newsroom').text)
        print('Navbar About Us passed')


        print('Navbar Log In')
        try:
            url = 'https://my.testjewelersmutual.com/plportal'
            action = webdriver.ActionChains(driver)
            element = driver.find_element_by_xpath('//a[@href="' + url + '"]')  # or your another selector here
            action.move_to_element(element)
            action.perform()
            time.sleep(2)
            print(driver.find_element_by_link_text('Personal Jewelry').text)
            print(driver.find_element_by_link_text('Agent').text)
            print(driver.find_element_by_link_text('Zing Platform').text)
            print('Navbar Log In passed')
        except:
            print('different log in element name due to different link')

    print('Navbar - verified')
    return True
def footer_validation(driver):
    driver.execute_script("window.scrollTo(0,4000)")
    time.sleep(5)

    print('verifying Footer containers')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'block-footerplmenu')))
    element = driver.find_element_by_id('block-footerplmenu')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)
    print(element.text)
    print(driver.find_element_by_id('block-footerclmenu').text)
    print(driver.find_element_by_id('block-footerinfomenu').text)
    print(driver.find_element_by_id('block-footercontactmenu').text)
    print(driver.find_element_by_id('block-footerrecommendedcontentlinks').text)
    print('Footer - verified')
    return True
def personal_insurance_body_validation(driver):
    print('Verifying Personal_insurance_Body containers')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'What will it cost me?')]")))

    whatwillitcostmebutton = driver.find_element_by_xpath("//a[contains(text(),'What will it cost me?')]")
    print(whatwillitcostmebutton.text)

    header_howthejewelryinsurance = driver.find_element_by_id('title-4366')
    print(header_howthejewelryinsurance.text)

    actions = ActionChains(driver)
    actions.move_to_element(header_howthejewelryinsurance).perform()

    comparisonTable = driver.find_element_by_class_name('comparison-table__center')
    print(comparisonTable.text)
    print(driver.find_element_by_class_name('table-footer').text)

    whatdoesjewelryinsurancecover = driver.find_element_by_id('title-4331')
    print(whatdoesjewelryinsurancecover.text)

    infogrid_jewelryinsurancecover = driver.find_element_by_id('info-grid-4356')
    print(infogrid_jewelryinsurancecover.text)

    protectingallthings = driver.find_element_by_id('text-image-row-4326')
    print(protectingallthings.text)

    image_whatourpolicyholderssay = driver.find_element_by_id('image-container-8266').is_displayed()
    print(image_whatourpolicyholderssay, " Image is displayed")

    whatourpolicyholderssay = driver.find_element_by_id('title-4361')
    print(whatourpolicyholderssay.text)

    image_checkyourrate = driver.find_element_by_id('image-container-8271').is_displayed()
    print(image_checkyourrate, " Image is displayed")

    checkyourrate = driver.find_element_by_id('feature-row-6476')
    print(checkyourrate.text)

    allthingsjewelryinsurance = driver.find_element_by_id('feature-row-4396')
    print(allthingsjewelryinsurance.text)

    element = allthingsjewelryinsurance
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    print('Personal_insurance_Body - verified')
    return True
def get_a_quote_body_validation(driver):
    print('Verifying Get_A_Quote_Body containers')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "appHeaderContainer")))

    jmlogo = driver.find_element_by_id('HeaderImages').is_displayed()
    print(jmlogo, "JM Logo is displayed")

    header_questions = driver.find_element_by_id('QuestionsContainer')
    print(header_questions.text)

    getyourfreejewelryinsurancequote = driver.find_element_by_id('quoteContainer')
    print(getyourfreejewelryinsurancequote.text)

    element = getyourfreejewelryinsurancequote
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    showmyquotebutton = driver.find_element_by_id('quoteInfoNext')
    print(showmyquotebutton.text)

    rightpanel = driver.find_element_by_id('right-panel')
    print(rightpanel.text)

    footer = driver.find_element_by_id('TermsAndPrivacyFooterContainer')
    print(footer.text)

    element = footer
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)

    print('Get_A_Quote_Body - verified')
    return True
def pay_my_bill_body_validation(driver):
    print('Verifying Get_A_Quote_Body containers')
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "jm-logo")))
    jmlogo = driver.find_element_by_class_name('jm-logo').is_displayed()

    if jmlogo:  # checking if it's visible
        print('JM Logo is displayed')
    else:
        print('JM Logo is not displayed')

    quickbillpaybody = driver.find_element_by_id('lookupForm')

    element = quickbillpaybody
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    print(quickbillpaybody.text)
    print(driver.find_element_by_id('continueButton').text)
    print(driver.find_element_by_id('recaptcha').text)
    print(driver.find_element_by_class_name('navbar').text)

    footer = driver.find_element_by_xpath("//div[contains(@class, 'col-md-8 col-sm-6 col-xs-12')]")
    element = footer
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    print(footer.text)

    privacyandterms = driver.find_element_by_xpath("//div[contains(@class, 'col-md-4 col-sm-6 col-xs-12')]")
    print(privacyandterms.text)
    time.sleep(3)

    print('Pay_My_Bill_Body - verified')
    return True
def claims_body_validation(driver):
    print('Verifying claims_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-2801")))

    heroimagecontainer = driver.find_element_by_xpath("//div[contains(@class, 'hero__image-container hero__image-container--no-mobile-image')]")
    print(heroimagecontainer.text)

    herocontent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]")
    print(herocontent.text)

    bodycontent = driver.find_element_by_xpath("//div[contains(@class, 'layout__region layout__region--content')]")
    print(bodycontent.text)

    whatsneeded = driver.find_element_by_id('title-2801')
    print(whatsneeded.text)

    whatsneededcontent = driver.find_element_by_id('info-grid-2826')
    print(whatsneededcontent.text)

    covid19andyourclaim = driver.find_element_by_id('feature-row-6726')
    print(covid19andyourclaim.text)

    howitallworks = driver.find_element_by_id('title-8256')
    print(howitallworks.text)

    startyourclaim = driver.find_element_by_id('text-image-row-2841')
    print(startyourclaim.text)

    chooseajeweler = driver.find_element_by_id('text-image-row-2846')
    print(chooseajeweler.text)

    payyourdeductible = driver.find_element_by_id('text-image-row-2851')
    print(payyourdeductible.text)

    insureyourreplacementjewelry = driver.find_element_by_id('text-image-row-2856')
    print(insureyourreplacementjewelry.text)

    claimsatisfactionratecontent = driver.find_element_by_id('feature-row-2861')
    print(claimsatisfactionratecontent.text)

    claimsatisfactionrateimage = driver.find_element_by_id('image-container-8276').is_displayed()
    print(claimsatisfactionrateimage, " Image is displayed")

    customersstoriesimage = driver.find_element_by_id('image-container-8281').is_displayed()
    print(customersstoriesimage, " Image is displayed")

    customerstoriestext = driver.find_element_by_id('feature-row-8261')
    print(customerstoriestext.text)

    element = driver.find_element_by_id('feature-row-2861')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    claimsrate = driver.find_element_by_id('feature-row-2861')
    print(claimsrate.text)

    whatisandisntcovered = driver.find_element_by_id('info-grid-2921')
    print(whatisandisntcovered .text)

    faqheader = driver.find_element_by_id('title-4196')
    print(faqheader.text)

    faqcontent = driver.find_element_by_id('accordion')
    print(faqcontent.text)

    startaclaim = driver.find_element_by_id('feature-row-8916')
    print(startaclaim.text)

    element = chooseajeweler
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('Claims_Body - verified')
    return True
def manage_my_policy_body_validation(driver):
    print('verifying manage_my_policy containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "jm-logo")))
    print(driver.find_element_by_id('page-body').text)
    time.sleep(3)
    print('manage_my_policy - verified')
    return True
def blog_body_validation(driver):
    print('verifying blog containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "block-jewelers-mutual-content")))

    bloghero = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    print(bloghero .text)

    # mostPopularPosts = driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-sidebars-personal-popular-posts')]")
    # print(mostPopularPosts.text)

    # postsByTopic = driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-topics-jewelry-box-topics')]")
    # print(postsByTopic.text)

    blogposts = driver.find_element_by_xpath("//div[contains(@class, 'layout__region layout__region--first')]")
    print(blogposts.text)

    time.sleep(3)
    print('blog - verified')
    return True
def answers_JewelryInsurance101_body_validation(driver):
    print('verifying JewelryInsurance101_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-image-row-7541")))
    yourguidetojewelryinsurance = driver.find_element_by_id('text-image-row-7541')
    print(yourguidetojewelryinsurance.text)
    yourguidetojewelryinsuranceimage = driver.find_element_by_xpath('//img[@alt="jewelry icon"]')
    print(yourguidetojewelryinsuranceimage, "Image is displayed")
    whatscoveredbyjewelryinsurance = driver.find_element_by_id('related-content-7696')
    print(whatscoveredbyjewelryinsurance.text)
    doineedajewelryappraisal = driver.find_element_by_id('related-content-8221')
    print(doineedajewelryappraisal.text)
    howdoestheclaimsprocessworktitle = driver.find_element_by_id('title-7581')
    print(howdoestheclaimsprocessworktitle.text)
    howdoestheclaimsprocessworktext = driver.find_element_by_id('feature-row-8511')
    print(howdoestheclaimsprocessworktext.text)
    myjewelrystoryvideo = driver.find_element_by_id('text-block-7601').is_displayed()
    print(myjewelrystoryvideo, "Video is displayed")
    quotewidget = driver.find_element_by_id('quote-widget-6401')
    print(quotewidget.text)
    stillhavequestions = driver.find_element_by_id('cta-group-7576')
    print(stillhavequestions.text)
    herocontent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    print(herocontent.text)
    pagenavigationlinks = driver.find_element_by_xpath("//div[contains(@class, 'navigation__secondary-sticky--links text-center')]")
    print(pagenavigationlinks.text)
    element = driver.find_element_by_id('cta-group-7576')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('JewelryInsurance101_Body - verified')
    return True
def answers_FAQ_body_validation(driver):
    print('verifying FAQ_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "views-exposed-form-acquia-search-faq-search")))
    searchbox = driver.find_element_by_id('views-exposed-form-acquia-search-faq-search').is_displayed()
    print(searchbox, "Search box is displayed")
    coverageblock = driver.find_element_by_id('text-block-11376')
    print(coverageblock.text)
    allcoveragequestionsbutton = driver.find_element_by_id('cta-group-9216')
    print(allcoveragequestionsbutton.text)
    appraisalsblock = driver.find_element_by_id('text-block-11391')
    print(appraisalsblock.text)
    allappraisalsquestionsbutton = driver.find_element_by_id('cta-group-9226')
    print(allappraisalsquestionsbutton.text)
    gettingstartedblock = driver.find_element_by_id('text-block-11381')
    print(gettingstartedblock.text)
    allgettingstrtedquestionsbutton = driver.find_element_by_id('cta-group-9221')
    print(allgettingstrtedquestionsbutton.text)
    mypolicyblock = driver.find_element_by_id('text-block-11396')
    print(mypolicyblock.text)
    allpolicyquestions = driver.find_element_by_id('cta-group-9231')
    print(allpolicyquestions.text)
    claimsblock = driver.find_element_by_id('text-block-11386')
    print(claimsblock.text)
    allclaimsquestions = driver.find_element_by_id('cta-group-9236')
    print(allclaimsquestions.text)
    popularquestions = driver.find_element_by_id('info-grid-9246')
    print(popularquestions.text)
    actions = ActionChains(driver)
    actions.move_to_element(allcoveragequestionsbutton).perform()
    actions.click(allcoveragequestionsbutton).perform()
    time.sleep(6)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "block-jewelers-mutual-content")))
    faqcoveragequestions = driver.find_element_by_id('block-jewelers-mutual-content')
    print(faqcoveragequestions.text)
    print('FAQ_Body - verified')
    return True

def login_Personal_Jewelry_body_validation(driver):
    print('verifying Personal_Jewelry_Body containers')
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "jm-logo")))
    print(driver.find_element_by_id('page-body').text)

    time.sleep(3)
    print('Personal_Jewelry_Body - verified')
    return True
def login_agent_body_validation(driver):
    print('verifying agent_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "jm-logo")))
    upperLinks = driver.find_element_by_id('utility')
    print(upperLinks.text)
    lowerLinks = driver.find_element_by_id('utility-nav-contain')
    print(lowerLinks.text)
    siteNavigation = driver.find_element_by_id('site-nav')
    print(siteNavigation.text)
    pageBody = driver.find_element_by_id('page-body')
    print(pageBody.text)
    footerLinks = driver.find_element_by_id('footer-utility-links')
    print(footerLinks.text)
    element = driver.find_element_by_id('footer-utility-links')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('agent_Body - verified')
    return True
def login_ZingPlatform_body_validation(driver):
    print('verifying Zing Platform_Body containers')
    time.sleep(3)

    zingLogo = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[1]/img').is_displayed()
    print(zingLogo, "Zing logo is displayed.")

    registerButton = driver.find_element_by_class_name('form-container')
    print(registerButton.text, "form-container")

    loginButton = driver.find_element_by_id('loginbutton')
    print(loginButton.text, "loginbutton")

    raisingTheTide = driver.find_element_by_id('Email')
    print(raisingTheTide.text, "Email")

    backgroundVideo = driver.find_element_by_id('pwdInput').is_displayed()
    print(backgroundVideo, "pwdInput")

    time.sleep(3)
    print('Zing Platform_Body - verified')
    return True

def embedded_quote_Estimatemyrate(driver):
    print('verifying embedded_quote_Body containers')
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "step2")))
    print(driver.find_element_by_id('step2').text)

    # quote content box
    print(driver.find_element_by_xpath("//div[contains(@class, 'estimate content-container--margin-bottom')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'quote-cards-container quote-flex-wrapper')]").text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'summary-total content-container row-quote')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'premium-warning content-container row-quote')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'button-container row-buttons')]").text)

    time.sleep(3)
    print('embedded_quote_Body - verifyied')
    return True

def soapUI(url, body):
    url = "http://jmtsvc04.jewelersnt.local/ExternalPaymentService/ExternalPayment.svc?singleWsdl"
    headers = {"SOAPAction": "http://tempuri.org/IExternalPayment/PaymentNotification",
               "Content-Type": "text/xml; charset=UTF-8"}
    data = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/" xmlns:ns="http://jewelersmutual.com/externalpayment/2016/01">
       <soapenv:Header/>
       <soapenv:Body>
          <tem:PaymentNotification>
             <!--Optional:-->
             <tem:request>
                <!--Optional:-->
                <ns:AccountNumber>3000000013</ns:AccountNumber>
                <!--Optional:-->
                <ns:Amount>254.00</ns:Amount>
                <!--Optional:-->
                <ns:ApplicationName>NEW_BUSINESS</ns:ApplicationName>
                <!--Optional:-->
                <ns:AuthorizationCode>123958783</ns:AuthorizationCode>
                <!--Optional:-->
                <ns:CardInfo>
                   <!--Optional:-->
                   <ns:AutoPay>false</ns:AutoPay>
                 
                   <ns:CreditCardExpDate>2018-04-01T00:00:00</ns:CreditCardExpDate>
                   <!--Optional:-->
                   <ns:CreditCardIssuer>Mastercard</ns:CreditCardIssuer>
                   <!--Optional:-->
                   <ns:IsActive>true</ns:IsActive>
                   <!--Optional:-->
                   <ns:LastFourDigits>5454</ns:LastFourDigits>
                </ns:CardInfo>
                <!--Optional:-->
                <ns:PayeeContactInfo>
                   <!--Optional:-->
                   <ns:AddressLine1>safv</ns:AddressLine1>
                   <!--Optional:-->
                   <ns:AddressLine2>vsdavfsad</ns:AddressLine2>
                   <!--Optional:-->
                   <ns:BillingPostalCode>54956</ns:BillingPostalCode>
                   <!--Optional:-->
                   <ns:City>Neenah</ns:City>
                   <!--Optional:-->
                   <ns:Country>US</ns:Country>
                   <!--Optional:-->
                   <!--Optional:-->
                   <ns:EmailAddress>test@test.com</ns:EmailAddress>
                   <!--Optional:-->
                   <ns:FirstName>TEST</ns:FirstName>
                   <!--Optional:-->
                   <ns:LastName>TEST</ns:LastName>
                   <!--Optional:-->
                   <ns:PayeeName>TEST</ns:PayeeName>
                   <!--Optional:-->
                   <ns:PhoneNumber>470-424-7194</ns:PhoneNumber>
                   <!--Optional:-->
                   <ns:State>WI</ns:State>
                </ns:PayeeContactInfo>
                <!--Optional:-->
                <ns:PaymentStatus>ACCEPTED</ns:PaymentStatus>
                <!--Optional:-->
                <ns:ReferenceNumber>578b456A5S3AKKA35965</ns:ReferenceNumber>
                <!--Optional:-->
                <ns:TxnRefNumber>538D85F6J0v5KKK83</ns:TxnRefNumber>
             </tem:request>
          </tem:PaymentNotification>
       </soapenv:Body>
     </soapenv:Envelope>
    """
    resp = requests.post(url, headers=headers, data=data)
    print(resp.status_code)
    print(resp.text)
    return resp.text
def application(driver, value, zipcode, rand_name, rand_name_last, addr, city, phone, email, itemtest):
    time.sleep(2)
    print('Start new application')
    driver.find_element_by_id('QuoteZipCode').click()
    time.sleep(1)
    driver.find_element_by_id('QuoteZipCode').send_keys(zipcode)
    time.sleep(1)
    driver.find_element_by_id(itemtest).click()
    time.sleep(2)
    print('Value & Item')
    driver.find_element_by_xpath('//*[@id="jewelry-itemType-1"]/option[2]').click()
    time.sleep(2)
    driver.find_element_by_id('jewelry-itemValue-1').click()
    time.sleep(1)
    driver.find_element_by_id('jewelry-itemValue-1').send_keys(value)
    time.sleep(2)
    driver.find_element_by_id('quoteInfoNext').click()
    try:
        driver.find_element_by_id('quoteInfoNext').click()
    except:
        print('button not found')
    time.sleep(3)
    driver.find_element_by_id('quoteResultsNext').click()
    time.sleep(3)
    driver.find_element_by_id('noThanks').click()
    time.sleep(2)
    driver.find_element_by_id('customerNext').click()
    time.sleep(3)
    print(rand_name)
    print(rand_name_last)
    driver.find_element_by_id('ApplicantFirstName').click()
    driver.find_element_by_id('ApplicantFirstName').send_keys(rand_name)
    time.sleep(1)
    driver.find_element_by_id('ApplicantLastName').click()
    driver.find_element_by_id('ApplicantLastName').send_keys(rand_name_last)
    time.sleep(1)
    driver.find_element_by_id('ApplicantAddress').click()
    driver.find_element_by_id('ApplicantAddress').send_keys(addr)
    time.sleep(1)
    driver.find_element_by_id('ApplicantCity').click()
    driver.find_element_by_id('ApplicantCity').send_keys(city)
    time.sleep(1)
    driver.find_element_by_id('ApplicantState').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="ApplicantState"]/option[51]').click()
    time.sleep(1)
    driver.find_element_by_id('ApplicantPhoneNumber').click()
    driver.find_element_by_id('ApplicantPhoneNumber').send_keys(phone)
    time.sleep(1)
    driver.find_element_by_id('ApplicantEmailAddress').click()
    driver.find_element_by_id('ApplicantEmailAddress').send_keys(email)
    time.sleep(1)
    driver.find_element_by_id('applicantDOBMonth').click()
    driver.find_element_by_xpath('//*[@id="applicantDOBMonth"]/option[6]').click()
    time.sleep(1)
    driver.find_element_by_id('applicantDOBDay').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="applicantDOBDay"]/option[2]').click()
    time.sleep(1)
    driver.find_element_by_id('applicantDOBYear').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="applicantDOBYear"]/option[28]').click()
    time.sleep(1)
    driver.find_element_by_id('ApplicantGender-Female').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="mainform"]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/label[1]/i').click()
    time.sleep(3)
    print('start of application completed')
def section3(driver):
    print('section 3')
    driver.find_element_by_id('ConvictedOfCrime-Misdemeanor').click()
    time.sleep(1)
    driver.find_element_by_id('SentenceCompletionDate').click()
    time.sleep(1)
    today = date.today()
    d1 = today.strftime("%m/%d/2014")
    print(d1)
    driver.find_element_by_id('SentenceCompletionDate').send_keys(d1)
    time.sleep(3)
    driver.find_element_by_id('ConvictionType').click()
    driver.find_element_by_xpath('//*[@id="ConvictionType"]/option[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="mainform"]/div[3]/div[2]/div[2]/div/div[1]/div/label[1]/i').click()
    time.sleep(1)
    driver.find_element_by_id('HasAgreedToTerms').click()
    time.sleep(100)
    driver.find_element_by_id('applicantNext').click()
    time.sleep(3)

    print('Jewelry Details')
    driver.find_element_by_xpath(
        '//*[@id="jmnfJewelryDetailsForm"]/div[1]/div[2]/div[1]/div/div/div/label[2]/i').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="jmnfJewelryDetailsForm"]/div[1]/div[2]/div[2]/div/div/div/label[1]/i').click()
    time.sleep(1)
    driver.find_element_by_id('AppraisalDate-JI-1').click()
    driver.find_element_by_id('AppraisalDate-JI-1').send_keys('11/11/2021')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="HasAlarm-No"]').click()
    time.sleep(1)
    print('The effective date is the current date')
    driver.find_element_by_id('EffectiveDate').click()
    driver.find_element_by_id('EffectiveDate').send_keys(d1)
    time.sleep(1)
    driver.find_element_by_id('jewelryDetailsNext').click()
    time.sleep(3)
    app_num = ""
def additionalquestions(driver):
    print('Additional Questions')
    driver.find_element_by_id('DeniedCoverage-No').click()
    time.sleep(1)
    driver.find_element_by_id('SafeDeposit-No').click()
    time.sleep(1)
    driver.find_element_by_id('GatedCommunity-No').click()
    time.sleep(1)
    driver.find_element_by_id('EmploysDomesticHelp-No').click()
    time.sleep(1)
    driver.find_element_by_id('HomeHasOtherResidents-No').click()
    time.sleep(1)
    driver.find_element_by_id('JewelryWearFrequency').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="JewelryWearFrequency"]/option[2]').click()
    time.sleep(1)
    driver.find_element_by_id('OvernightTravelFrequency').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="OvernightTravelFrequency"]/option[2]').click()
    time.sleep(1)
    driver.find_element_by_id('additionalQuestionsNext').click()
    time.sleep(7)
    print('There is no payment')
    print('---------- Review Your Application')
    driver.find_element_by_id('HasAcknowledgedLegalTerms').click()
    time.sleep(3)
    driver.find_element_by_id('SignAndSubmit').click()
    time.sleep(20)
    app_num = driver.find_element_by_xpath(
        '//*[@id="confirmationContainer"]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]').text
    print('account number is: {}'.format(app_num))
    eff_date = driver.find_element_by_xpath(
        '//*[@id="confirmationContainer"]/div/div/div[2]/div[2]/div[2]/div/div[2]').text
    print('effective date is: {}'.format(eff_date))
    time.sleep(3)
    return app_num
def gwpolicycenter(driver, env, appnum):
    print('Opening GW policy center')
    driver.get(env)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="Login:LoginScreen:LoginDV:username-inputEl"]').click()
    driver.find_element_by_xpath('//*[@id="Login:LoginScreen:LoginDV:username-inputEl"]').send_keys('su')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="Login:LoginScreen:LoginDV:password-inputEl"]').click()
    driver.find_element_by_xpath('//*[@id="Login:LoginScreen:LoginDV:password-inputEl"]').send_keys('gw')
    time.sleep(1)
    driver.find_element_by_id('Login:LoginScreen:LoginDV:submit-btnInnerEl').click()
    driver.maximize_window()  # driver.maximize_window()
    time.sleep(3)
    driver.find_element_by_id('TabBar:SearchTab').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="Search:MenuLinks:Search_AccountSearch"]/div/span').click()
    time.sleep(2)
    driver.find_element_by_id('AccountSearch:AccountSearchScreen:AccountSearchDV:AccountNumber-inputEl').click()
    time.sleep(1)
    driver.find_element_by_id('AccountSearch:AccountSearchScreen:AccountSearchDV:AccountNumber-inputEl').send_keys(
        appnum)
    time.sleep(1)
    driver.find_element_by_id(
        'AccountSearch:AccountSearchScreen:AccountSearchDV:SearchAndResetInputSet:SearchLinksInputSet:Search').click()
    time.sleep(2)
    driver.find_element_by_id('AccountSearch:AccountSearchScreen:AccountSearchResultsLV:0:AccountNumber').click()
    time.sleep(3)
