from Generic_functions_modules import *

def business_insurance_body_validation(driver):
    print('verifying business_insurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-4416")))

    heroimage = driver.find_element_by_xpath("//div[contains(@class, 'hero__content-wrapper hero-scheme-blue-black')]")
    print(heroimage.text)

    corepolicies = driver.find_element_by_id('title-4416')
    print(corepolicies.text)

    corepoliciesinfogid = driver.find_element_by_id('info-grid-4436')
    print(corepoliciesinfogid.text)

    addonstitle = driver.find_element_by_id('title-4441')
    print(addonstitle.text)

    addonscontent1 = driver.find_element_by_id('info-grid-4481')
    print(addonscontent1.text)

    addonsimage1 = driver.find_element_by_id('image-container-8286').is_displayed()
    print(addonsimage1, "Image is displayed")

    addonsimage2 = driver.find_element_by_id('image-container-8311').is_displayed()
    print(addonsimage2, "Image is displayed")

    addonscontent2 = driver.find_element_by_id('info-grid-8306')
    print(addonscontent2.text)

# driver.find_element(by=By.XPATH, value="//div[contains(@class, 'title-bar content-lg spacing clearfix')]")
    customerstoriestitle = driver.find_element_by_css_selector("[class*='title-bar']")
    print(customerstoriestitle.text)

    customerstories = driver.find_element_by_id('text-block-4406')
    print(customerstories.text)

    customerstoriesvideomodal = driver.find_element_by_id('video-modal-4411').is_displayed()
    print(customerstoriesvideomodal, "Video modal is displayed")

    toolsforbusiness = driver.find_element_by_id('feature-row-4486')
    print(toolsforbusiness.text)

    jewelerresourcestitle = driver.find_element_by_id('title-8321')
    print(jewelerresourcestitle .text)

    jewelerresourcesrelatedcontent = driver.find_element_by_id('related-content-9086')
    print(jewelerresourcesrelatedcontent.text)

    contactanagenttitle = driver.find_element_by_id('title-8316')
    print(contactanagenttitle.text)

    salesforceiframe = driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-inline-blocksalesforce-form')]")
    print(salesforceiframe.text)

    navigationlinks = driver.find_element_by_xpath("//div[contains(@class, 'navigation__secondary-sticky--links text-center')]")
    print(navigationlinks.text)

    element = driver.find_element_by_id('title-8316')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('claims_Body - verified')
    return True
def business_claims_body_validation(driver):
    print('verifying business_insurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-image-row-4596")))

    # herocontent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    # print(herocontent.text)

    startyourclaim = driver.find_element_by_id('text-image-row-4596')
    print(startyourclaim.text)

    minimizefurtherdamage = driver.find_element_by_id('text-image-row-4601')
    print(minimizefurtherdamage.text)

    meetyourclaimsexpert = driver.find_element_by_id('text-image-row-4606')
    print(meetyourclaimsexpert.text)

    backtobusiness = driver.find_element_by_id('text-image-row-4611')
    print(backtobusiness.text)

    claimssatisfactionrate = driver.find_element_by_id('feature-row-4616')
    print(claimssatisfactionrate.text)

    themostcommonclaims = driver.find_element_by_id('title-4646')
    print(themostcommonclaims.text)

    themostcommonclaimsinfogrid = driver.find_element_by_id('info-grid-4641')
    print(themostcommonclaimsinfogrid .text)

    faqaccordion = driver.find_element_by_id('accordion-4661')
    print(faqaccordion.text)

    startaclaimblock = driver.find_element_by_id('feature-row-4666')
    print(startaclaimblock.text)

    element = driver.find_element_by_id('feature-row-4666')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('claims_Body - verified')
    return True
def business_paymybill_body_validation(driver):
    print('verifying paymybill containers')
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'lookupForm')))
    jmlogo = driver.find_element_by_class_name('jm-logo').is_displayed()
    print(jmlogo, "JM Logo is displayed")

    quickbillpaybody = driver.find_element_by_id('lookupForm')
    print(quickbillpaybody.text)

    element = quickbillpaybody
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    print(driver.find_element_by_id('continueButton').text)
    print(driver.find_element_by_id('recaptcha').text)
    print(driver.find_element_by_class_name('navbar').text)

    footer = driver.find_element_by_xpath("//div[contains(@class, 'col-md-8 col-sm-6 col-xs-12')]")
    print(footer.text)

    element = footer
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    privacyandterms = driver.find_element_by_xpath("//div[contains(@class, 'col-md-4 col-sm-6 col-xs-12')]")
    print(privacyandterms.text)

    time.sleep(3)
    print('Pay_My_Bill_Body - verified')
    return True
def business_zingplatform_body_validation(driver):
    print('Verifying Zing Platform containers')
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-8466")))
    herocontainer = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    print(herocontainer.text)

    maximizingyourbusinesspotentialtitle = driver.find_element_by_id('title-8466')
    print(maximizingyourbusinesspotentialtitle.text)

    maximizingyourbusinesspotentialtext = driver.find_element_by_id('title-8471')
    print(maximizingyourbusinesspotentialtext.text)

    zingvideomodal = driver.find_element_by_id('video-modal-8476').is_displayed()
    print(zingvideomodal, 'Video modal is displayed')

    benefitsforyourjewelrybusiness = driver.find_element_by_id('title-8366')
    print(benefitsforyourjewelrybusiness.text)

    benefitsinfogrid = driver.find_element_by_id('info-grid-7956')
    print(benefitsinfogrid.text)

    benefitsimage = driver.find_element_by_id('image-container-8541').is_displayed()
    print(benefitsimage, 'Image is displayed')

    toolsforyourbusinesstitle = driver.find_element_by_id('title-8371')
    print(toolsforyourbusinesstitle.text)

    toolsforyourbusinessinfogrid = driver.find_element_by_id('info-grid-7981')
    print(toolsforyourbusinessinfogrid.text)

    howitworks = driver.find_element_by_id('related-content-9036')
    print(howitworks.text)

    seetheplatforminaction = driver.find_element_by_id('feature-row-8461')
    print(seetheplatforminaction.text)

    faq = driver.find_element_by_id('accordion-9066')
    print(faq.text)

    registernow = driver.find_element_by_id('feature-row-7986')
    print(registernow.text)

    element = driver.find_element_by_id('feature-row-7986')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('Zing Platform - verified')
    return True
def business_jm_shipping_solution_body_validation(driver):
    print('verifying business_insurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-image-row-9266")))

    herocontent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]")
    print(herocontent.text)

    shipjewelryonzingplatform = driver.find_element_by_id('text-image-row-9266')
    print(shipjewelryonzingplatform.text)

    howitworksvideomodal = driver.find_element_by_id('video-modal-12281').is_displayed()
    print(howitworksvideomodal, "Video modal is displayed")

    howitworksinfogrid = driver.find_element_by_id('info-grid-6906')
    print(howitworksinfogrid.text)

    benefitsforyourbusinessinfogrid = driver.find_element_by_id('info-grid-2291')
    print(benefitsforyourbusinessinfogrid.text)

    putthewholejewelryindustryatyourfingertips = driver.find_element_by_id('feature-row-9276')
    print(putthewholejewelryindustryatyourfingertips.text)

    getstarted = driver.find_element_by_id('title-2341')
    print(getstarted .text)

    salesforceiframe = driver.find_element_by_id('title-4191').is_displayed()
    print(salesforceiframe, "Salesforce iframe is displayed")

    element = driver.find_element_by_id('title-4191')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('jm_shipping_solution_Body - verified')
    return True
def business_jmcareplan_body_validation(driver):
    print('Verifying JM Care Plan - Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-image-row-11741")))

    jmcareplanlogo = driver.find_element_by_xpath('//img[@alt="JM Care Plan logo"]').is_displayed()
    print(jmcareplanlogo, "JM Care Plan image is displayed")

    carePlans = driver.find_element_by_id('text-image-row-11741')
    print(carePlans.text)

    careplansyoucantrusttext = driver.find_element_by_id('title-5396')
    print(careplansyoucantrusttext.text)

    careplansyoucantrustvideomodal = driver.find_element_by_id('video-modal-6706').is_displayed()
    print(careplansyoucantrustvideomodal, "Care plans video modal is displayed")

    whyjmcarelansproductsinfogrid = driver.find_element_by_id('info-grid-5416')
    print(whyjmcarelansproductsinfogrid.text)

    whatscoveredinfogrid = driver.find_element_by_id('info-grid-5431')
    print(whatscoveredinfogrid.text)

    whatscovereddetails = driver.find_element_by_id('details-block-5876')
    print(whatscovereddetails.text)

    howtheclaimsprocessworksinfogrid = driver.find_element_by_id('info-grid-5446')
    print(howtheclaimsprocessworksinfogrid.text)

    element = driver.find_element_by_id('info-grid-5446')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('JM Care Plan Body - Verified')
    return True
def business_appraisalsolution_body_validation(driver):
    print('verifying business_insurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-11061")))

    herocontent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content-wrapper hero-scheme-blue-black  ')]")
    print(herocontent.text)

    pagenavigationlinks = driver.find_element_by_xpath("//div[contains(@class, 'navigation__secondary-sticky--links text-center')]")
    print(pagenavigationlinks.text)

    jewelryappraisalsmadeeasy = driver.find_element_by_id('title-11061')
    print(jewelryappraisalsmadeeasy.text)

    zinglogo = driver.find_element_by_id('text-block-11056').is_displayed()
    print(zinglogo, "Zing logo is displayed")

    benefitsofthejewelryappraisaltitle = driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]")
    print(benefitsofthejewelryappraisaltitle.text)

    benefitsofthejewelryappraisalinfogrid1 = driver.find_element_by_id('info-grid-11081')
    print(benefitsofthejewelryappraisalinfogrid1.text)

    benefitsiamge = driver.find_element_by_id('image-container-11066').is_displayed()
    print(benefitsiamge, "Image is displayed")

    benefitsofthejewelryappraisalinfogrid2 = driver.find_element_by_id('info-grid-11101')
    print(benefitsofthejewelryappraisalinfogrid2.text)

    seethejewelryappraisalvideomodal = driver.find_element_by_id('video-modal-11111').is_displayed()
    print(seethejewelryappraisalvideomodal, "Video modal is displayed")

    seethejewelryappraisalsolution = driver.find_element_by_id('title-11116')
    print(seethejewelryappraisalsolution.text)

    getstarted = driver.find_element_by_id('title-11126')
    print(getstarted.text)

    getstartediframe = driver.find_element_by_id('title-11131').is_displayed()
    print(getstartediframe, "Get started iframe is displayed")

    whatisthezingplatform = driver.find_element_by_id('feature-row-11121')
    print(whatisthezingplatform.text)

    element = driver.find_element_by_id('feature-row-11121')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('Appraisal Solution Body - Verified')
    return True
def business_jewelerprograms_body_validation(driver):
    print('verifying business_insurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-2751")))

    herocontent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]")
    print(herocontent.text)

    whatsinitforyou = driver.find_element_by_id('title-2751')
    print(whatsinitforyou.text)

    # whatsinitforyouinfogrid = driver.find_element_by_id('info-grid-2776')
    # print(whatsinitforyouinfogrid.text)

    # customercareicon = driver.find_element_by_xpath('//img[@alt="customer care graphic"]').is_displayed()
    # print(customercareicon, "Icon customer care is displayed")

    # easyclaimpaymenticon = driver.find_element_by_xpath('//img[@alt="chart graphic"]')
    # print(easyclaimpaymenticon, "Icon easy claim payments care is displayed")

    # flexibilityicon = driver.find_element_by_xpath('//img[@alt="flexibility graphic"]')
    # print(flexibilityicon, "Icon flexibility care is displayed")

    # growyourbusinessicon = driver.find_element_by_xpath('//img[@alt="trophy graphic"]')
    # print(growyourbusinessicon, "Icon grow your business care is displayed")

    strengthencustomerrelationsimage = driver.find_element_by_id('image-container-9251').is_displayed()
    print(strengthencustomerrelationsimage, "Image is displayed")

    strengthencustomerrelations = driver.find_element_by_id('feature-row-2786')
    print(strengthencustomerrelations.text)

    # therearemoreadvantages = driver.find_element_by_id('feature-row-2791')
    # print(therearemoreadvantages.text)

    requesttobepartoftheprogram = driver.find_element_by_id('title-9256')
    print(requesttobepartoftheprogram.text)

    requestiframe = driver.find_element_by_id('title-4246').is_displayed()
    print(requestiframe, "Request to be part of the program iframe is displayed")

    element = driver.find_element_by_id('title-4246')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('jewelerprograms_Body - verified')
    return True
def business_pawnbrokers_body_validation(driver):
    print('verifying Pawnbrokers_Body containers')
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-4546")))

    herocontent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    print(herocontent.text)

    protectyourbusinesstitle = driver.find_element_by_id('title-4546')
    print(protectyourbusinesstitle.text)

    protectyourbusinessleftblock = driver.find_element_by_id('details-block-4571')
    print(protectyourbusinessleftblock.text)

    comprehensivecoverageicon = driver.find_element_by_xpath('//img[@alt="Coverage Icon"]').is_displayed()
    print(comprehensivecoverageicon, "Icon comprehensive coverage is displayed")

    jmshippingsolutionicon = driver.find_element_by_xpath('//img[@alt="Shipping Icon"]').is_displayed()
    print(jmshippingsolutionicon, "Icon JM shipping solution is displayed")

    personaljewelryinsuranceicon = driver.find_element_by_xpath('//img[@alt="Money Icon"]').is_displayed()
    print(personaljewelryinsuranceicon, "Icon personal jewelry insurance is displayed")

    getapersonalizedrisk = driver.find_element_by_id('feature-row-4551')
    print(getapersonalizedrisk.text)

    getapersonalizedriskform = driver.find_element_by_id('basic-code-block-hubspot-form-for-pawnbrokers-page').is_displayed()
    print(getapersonalizedriskform, "Form is displayed")

    element = driver.find_element_by_id('basic-code-block-hubspot-form-for-pawnbrokers-page')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('Pawnbrokers_Body - verified')
    return True