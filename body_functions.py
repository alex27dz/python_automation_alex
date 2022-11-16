from Generic_functions_modules import *;

def body_ToRegisterForAnOnlineAccount(driver):
    print('verifying Personal_Jewelry_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "jm-logo")))
    print(driver.find_element_by_id('page-body').text)
    time.sleep(3)
    print('Personal_Jewelry_Body - verified')
    return True
def body_startaclaim(driver):
    print('verifying startaclaim_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lookupForm")))
    startAClaimbody = driver.find_element_by_id('lookupForm')
    print(startAClaimbody.text)
    helpIcon = driver.find_element_by_id('helpLookupPolicyNumber').is_displayed()
    print(helpIcon, "Help icon is displayed.")
    continueButton = driver.find_element_by_id('continueButton').is_displayed()
    print(continueButton, "Continue button is displayed.")
    print(driver.find_element_by_xpath("//div[contains(@class, 'container')]").text)
    time.sleep(3)
    print('startaclaim_Body - verified')
    return True
def body_jmuniversity(driver):
    print('verifying jmuniversity_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-3071")))
    heroContent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    print(heroContent.text)
    heresWhatYoullGet = driver.find_element_by_id('title-3071')
    print(heresWhatYoullGet.text)
    heresWhatYoullGetInfogrid = driver.find_element_by_id('info-grid-3096')
    print(heresWhatYoullGetInfogrid.text)
    getStarted = driver.find_element_by_id('title-3101')
    print(getStarted.text)
    buttons = driver.find_element_by_id('cta-group-3106')
    print(buttons.text, "Buttons are displayed.")
    time.sleep(3)
    print('jmuniversity_Body - verified')
    return True
def body_COVIDResources(driver):
    print('verifying COVIDResources_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-6611")))
    coronaVirusInformationTitle = driver.find_element_by_id('title-6611')
    print(coronaVirusInformationTitle.text)
    informationBlock = driver.find_element_by_id('text-block-6616')
    print(informationBlock.text)
    buttons = driver.find_element_by_id('cta-group-6586')
    print(buttons.text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    time.sleep(3)
    print('COVIDResources_Body - verified')
    return True
def body_ContactUs(driver):
    print('verifying ContactUs_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "info-grid-2741")))
    heroContent = driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-field-blocknodecore-pagefield-hero')]")
    print(heroContent.text)
    contactInformationTitle = driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]")
    print(contactInformationTitle.text)
    contactInformationInfogrid = driver.find_element_by_id('info-grid-2741')
    print(contactInformationInfogrid .text)
    map = driver.find_element_by_id('feature-row-2746').is_displayed()
    print(map, "Map is displayed.")
    time.sleep(3)
    print('ContactUs_Body - verified')
    return True
def body_ShareYourConcerns(driver):
    print('verifying ShareYourConcerns_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-2721")))
    heroContent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    print(heroContent.text)
    shareYourConcernsTitle = driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]")
    print(shareYourConcernsTitle.text)
    shareYourConcernsTextBlock = driver.find_element_by_id('text-block-2721')
    print(shareYourConcernsTextBlock.text)
    time.sleep(3)
    print('ShareYourConcerns_Body - verified')
    return True
def body_Homuchdoesitcosttoresizearing(driver):
    print('verifying Homuchdoesitcosttoresizearing_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sidebar-2181")))
    checkYourRate = driver.find_element_by_id('sidebar-2181')
    print(checkYourRate.text)
    postImage = driver.find_element_by_xpath('//img[@alt="How much does it cost to resize a ring?"]').is_displayed()
    print(postImage, "Post image is displayed")
    heroContent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    print(heroContent.text)
    content = driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-field-blocknodeblog-articlebody')]")
    print(content.text)
#    mostPopularPosts = driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-sidebars-most-popular-posts-block')]")
#    print(mostPopularPosts.text)
    postsByTopic = driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-topics-blog-detail-topics-list')]")
    print(postsByTopic.text)
    time.sleep(3)
    print('Homuchdoesitcosttoresizearing_Body - verified')
    return True
def body_Howtocleangoldjewelry(driver):
    print('verifying Howtocleangoldjewelry_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sidebar-2181")))
    checkYourRate = driver.find_element_by_id('sidebar-2181')
    print(checkYourRate.text)
    postImage = driver.find_element_by_xpath('//img[@alt="How to Clean Gold Jewelry"]').is_displayed()
    print(postImage, "Post image is displayed")
    heroContent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    print(heroContent.text)
    content = driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-field-blocknodeblog-articlebody')]")
    print(content.text)
#    mostPopularPosts = driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-sidebars-most-popular-posts-block')]")
#    print(mostPopularPosts.text)
    postsByTopic = driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-topics-blog-detail-topics-list')]")
    print(postsByTopic.text)
    time.sleep(3)
    print('Howtocleangoldjewelry_Body - verified')
    return True
def body_Howmuchshouldcost(driver):
    print('verifying Howmuchshouldcost_Body containers')
    time.sleep(3)

    # side bar
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sidebar-2181")))
    print(driver.find_element_by_id('cta_button_413440_8c15d489-2ed8-41c5-a448-e7e1fa60e414').text)
    print(driver.find_element_by_id('sidebar-2181').text)

    # content in the middle
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-field-blocknodeblog-articlebody')]").text)
#    print(driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-sidebars-most-popular-posts-block')]").text)

    button = driver.find_element_by_xpath('//*[@id="hs-cta-img-faa1df2a-d1f9-4ed1-80b1-61c73d711ed0"]')
    print(button, "button located")

    # images
    # image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    # print(image, "site-log")

    #image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div[3]/div/p[1]/img').is_displayed()
    #print(image, "image in the middle")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    comprehensivecoverageicon = driver.find_element_by_xpath('//img[@alt="Youtube icon"]').is_displayed()
    print(comprehensivecoverageicon, "Icon comprehensive coverage is displayed")

    time.sleep(3)
    print('Howmuchshouldcost_Body - verified')
    return True
def body_Howtomakearing(driver):
    print('verifying Howtomakearing_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sidebar-2181")))
    print(driver.find_element_by_id('quick-quote').text)
    print(driver.find_element_by_id('sidebar-2181').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'layout__region layout__region--first')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-field-blocknodeblog-articlebody')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-topics-blog-detail-topics-list')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'quote-widget')]").text)

    # images
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")
    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")
    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")
    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")
    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")
    time.sleep(3)
    print('Howtomakearing_Body - verified')
    return True
def body_Moreblogarticles(driver):
    print('verifying Moreblogarticles_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "block-jewelers-mutual-content")))

    # content in the middle
    print(driver.find_element_by_id('block-jewelers-mutual-content').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-sidebars-personal-popular-posts')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-topics-jewelry-box-topics')]").text)

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/a/picture/img').is_displayed()
    print(image, "image in the middle")
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div/div/div/div/div[2]/div/div[1]/a/picture/img').is_displayed()
    print(image, "image in the middle")
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div/div/div/div/div[3]/div/div[1]/a/picture/img').is_displayed()
    print(image, "image in the middle")
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div/div/div/div/div[4]/div/div[1]/a/picture/img').is_displayed()
    print(image, "image in the middle")
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div/div/div/div/div[5]/div/div[1]/a/picture/img').is_displayed()
    print(image, "image in the middle")

    time.sleep(3)
    print('Moreblogarticles_Body - verified')
    return True
def body_PrivacyPolicy(driver):
    print('verifying PrivacyPolicy_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-9491")))

    # content in the middle
    print(driver.find_element_by_id('text-block-9491').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)
    time.sleep(3)

    # images
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    # image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div[3]/div/p[1]/img').is_displayed()
    # print(image, "image in the middle")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")


    print('PrivacyPolicy_Body - verified')
    return True
def body_TermsofUse(driver):
    print('verifying PrivacyPolicy_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-9486")))

    # content in the middle
    print(driver.find_element_by_id('text-block-9486').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)

    # images
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    # image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div[3]/div/p[1]/img').is_displayed()
    # print(image, "image in the middle")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('PrivacyPolicy_Body - verified')
    return True
def body_engagementringinsurance(driver):
    print('verifying engagementringinsurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-3496")))

    # content in the middle including questions and table and description
    print(driver.find_element_by_id('title-3496').text)
    print(driver.find_element_by_id('title-3436').text)
    print(driver.find_element_by_id('info-grid-3466').text)
#    print(driver.find_element_by_id('info-grid-3491').text)
    print(driver.find_element_by_id('basic-code-block-what-our-policyholders-say').text)
    print(driver.find_element_by_id('accordion-3516').text)
    print(driver.find_element_by_id('feature-row-5201').text)
#    print(driver.find_element_by_id('feature-row-3521').text)
#    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]").text)
#    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__tout hero__tout--grey no-flex')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'comparison-table__center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'table-footer')]").text)
#    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)


    # body page images
    # image = driver.find_element_by_xpath('//*[@id="feature-row-3521"]/style/text()').is_displayed()
    # print(image, "image")
#    image = driver.find_element_by_xpath('//*[@id="feature-row-5201"]/div/div[1]/img').is_displayed()
#    print(image, "image")
#    image = driver.find_element_by_xpath('//*[@id="info-grid-3491"]/div[4]/img[2]').is_displayed()
#    print(image, "image")
#    image = driver.find_element_by_xpath('//*[@id="info-grid-3491"]/div[3]/img[2]').is_displayed()
#    print(image, "image")
#    image = driver.find_element_by_xpath('//*[@id="info-grid-3491"]/div[2]/img[2]').is_displayed()
#    print(image, "image")
#    image = driver.find_element_by_xpath('//*[@id="info-grid-3491"]/div[1]/img[2]').is_displayed()
#    print(image, "image")
#    image = driver.find_element_by_xpath('//*[@id="info-grid-3466"]/div[5]/img[2]').is_displayed()
#    print(image, "image")
#    image = driver.find_element_by_xpath('//*[@id="info-grid-3466"]/div[4]/img[2]').is_displayed()
#    print(image, "image")
#    image = driver.find_element_by_xpath('//*[@id="info-grid-3466"]/div[3]/img[2]').is_displayed()
#    print(image, "image")
#    image = driver.find_element_by_xpath('//*[@id="info-grid-3466"]/div[2]/img[2]').is_displayed()
#    print(image, "image")
#    image = driver.find_element_by_xpath('//*[@id="info-grid-3466"]/div[1]/img[2]').is_displayed()
#    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[3]/div/div/div/div/div/div[2]/div/img').is_displayed()
    print(image, "image")
#    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[1]/div/div[2]/div/img[7]').is_displayed()
#    print(image, "image")

#    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[1]/div/div[2]/div/img[6]').is_displayed()
#    print(image, "image")
#    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[1]/div/div[2]/div/img[5]').is_displayed()
#    print(image, "image")
#    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[1]/div/div[2]/div/img[4]').is_displayed()
#    print(image, "image")
#    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[1]/div/div[2]/div/img[3]').is_displayed()
#    print(image, "image")
#    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[1]/div/div[2]/div/img[2]').is_displayed()
#    print(image, "image")
#    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[1]/div/div[2]/div/img[1]').is_displayed()
#    print(image, "image")

    # images
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    # image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div[3]/div/p[1]/img').is_displayed()
    # print(image, "image in the middle")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('engagementringinsurance_Body - verifyied')
    return True
def body_comparejewelryinsurancetohomeowners(driver):
    print('verifying comparejewelryinsurancetohomeowners_Body containers')
    time.sleep(3)
    print(driver.find_element_by_xpath("//div[contains(@class, 'comparison-table__center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-inline-blockinfo-grid block--info-grid background-color-')]").text)

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('comparejewelryinsurancetohomeowners_Body - verifyied')
    return True
def body_personaljewelryinsurancecollections(driver):
    print('verifying personaljewelryinsurancecollections_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-image-row-3361")))

    # content in the middle + table + info
    print(driver.find_element_by_id('text-image-row-3361').text)
    print(driver.find_element_by_id('title-3366').text)
    print(driver.find_element_by_id('info-grid-3391').text)
    print(driver.find_element_by_id('feature-row-3396').text)
    print(driver.find_element_by_id('feature-row-3401').text)
    print(driver.find_element_by_id('title-8326').text)
    print(driver.find_element_by_id('timeline-row-3406').text)
    print(driver.find_element_by_id('timeline-row-3411').text)
    print(driver.find_element_by_id('timeline-row-3416').text)
    print(driver.find_element_by_id('timeline-row-3421').text)
    print(driver.find_element_by_id('basic-code-block-trustpilot-horizontal---no-tags').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)

    # images
    image = driver.find_element_by_xpath('//*[@id="timeline-row-3421"]/div[1]/div/img').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="timeline-row-3416"]/div[1]/div/img').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="timeline-row-3411"]/div[1]/div/img').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="timeline-row-3406"]/div[1]/div/img').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3391"]/div[2]/div[2]/div/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3391"]/div[2]/div[1]/div/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3391"]/div[1]/div[1]/div/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3391"]/div[1]/div[2]/div/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="text-image-row-3361"]/div[1]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    # image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div[3]/div/p[1]/img').is_displayed()
    # print(image, "image in the middle")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('personaljewelryinsurancecollections_Body - verifyied')
    return True
def body_crownandcaliber(driver):
    print('verifying crownandcaliber_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-12466")))

    # content in the middle
    print(driver.find_element_by_id('text-block-12466').text)
    print(driver.find_element_by_id('feature-row-12476').text)

    # Images
    image = driver.find_element_by_xpath('//*[@id="image-container-12461"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('crownandcaliber_Body - verifyied')
    return True
def body_adiamor(driver):
    print('verifying adiamor_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-12426")))

    # content in the middle + button
    print(driver.find_element_by_id('text-block-12426').text)
    print(driver.find_element_by_id('feature-row-12436').text)
    print(driver.find_element_by_id('text-block-12431').text)
    print(driver.find_element_by_xpath("//*[@id='feature-row-12436']/div/div[2]/a").text)

    # Images
    image = driver.find_element_by_xpath('//*[@id="image-container-12501"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="image-container-12421"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('adiamor_Body - verifyied')
    return True
def body_briangavindiamonds(driver):
    print('verifying briangavindiamonds_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-12446")))

    # content in the middle + button
    print(driver.find_element_by_id('text-block-12446').text)
    print(driver.find_element_by_id('feature-row-12451').text)
    print(driver.find_element_by_id('text-block-12456').text)
    print(driver.find_element_by_xpath("//*[@id='feature-row-12451']/div/div[2]/a").text)

    # Images
    image = driver.find_element_by_xpath('//*[@id="image-container-12506"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="image-container-12441"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('briangavindiamonds_Body - verifyied')
    return True
def body_jamesallen(driver):
    print('verifying jamesallen_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-12406")))

    # content in the middle + button
    print(driver.find_element_by_id('text-block-12406').text)
    print(driver.find_element_by_id('feature-row-12411').text)
    print(driver.find_element_by_id('text-block-12416').text)
    print(driver.find_element_by_xpath("//*[@id='feature-row-12411']/div/div[2]/a").text)

    # Images
    image = driver.find_element_by_xpath('//*[@id="image-container-12521"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="image-container-12401"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('jamesallen_Body - verifyied')
    return True
def body_bluenile(driver):
    print('verifying bluenile_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-12386")))

    # content in the middle + button
    print(driver.find_element_by_id('text-block-12386').text)
    print(driver.find_element_by_id('feature-row-12391').text)
    print(driver.find_element_by_id('text-block-12396').text)

    # Images
    image = driver.find_element_by_xpath('//*[@id="image-container-12526"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="image-container-12381"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('bluenile_Body - verifyied')
    return True
def body_whiteflash(driver):
    print('verifying whiteflash_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-12486")))

    # content in the middle + button
    print(driver.find_element_by_id('text-block-12486').text)
    print(driver.find_element_by_id('feature-row-12496').text)
    print(driver.find_element_by_id('text-block-12491').text)

    # Images
    image = driver.find_element_by_xpath('//*[@id="image-container-12481"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="image-container-12511"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('whiteflash_Body - verifyied')
    return True
def body_earringinsurance(driver):
    print('verifying earringinsurance_Body containers')
    time.sleep(3)

    # content in the middle + table
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-3971")))
    print(driver.find_element_by_id('title-3971').text)
    print(driver.find_element_by_id('title-3746').text)
    print(driver.find_element_by_id('info-grid-3911').text)
    print(driver.find_element_by_id('info-grid-3966').text)
    print(driver.find_element_by_id('basic-code-block-what-our-policyholders-say').text)
    print(driver.find_element_by_id('accordion-4106').text)
    print(driver.find_element_by_id('feature-row-5196').text)
    print(driver.find_element_by_id('feature-row-4111').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'comparison-table__center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__image-container')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)

    # Images
    image = driver.find_element_by_xpath('//*[@id="feature-row-5196"]/div/div[1]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="info-grid-3966"]/div[4]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3966"]/div[3]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3966"]/div[2]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3966"]/div[1]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3911"]/div[5]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3911"]/div[4]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3911"]/div[3]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3911"]/div[2]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3911"]/div[1]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[3]/div/div/div/div/div/div[2]/div/img').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[1]/div/div/div[1]/picture/source[4]').is_displayed()
    print(image, "image")




    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('earringinsurance_Body - verifyied')
    return True
def body_watchinsurance(driver):
    print('verifying watchinsurance_Body containers')
    time.sleep(3)

    # Content in the middle
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-3941")))
    print(driver.find_element_by_id('title-3741').text)
    print(driver.find_element_by_id('info-grid-3791').text)
    print(driver.find_element_by_id('info-grid-3936').text)
    print(driver.find_element_by_id('accordion-4081').text)
    print(driver.find_element_by_id('feature-row-5191').text)
    print(driver.find_element_by_id('feature-row-4086').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content-wrapper hero-scheme-blue-black')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'comparison-table etb spacing')]").text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'basic-code-block-what-our-policyholders-say')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)

    # Images
    image = driver.find_element_by_xpath('//*[@id="feature-row-5191"]/div/div[1]/img').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3936"]/div[4]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3936"]/div[3]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3936"]/div[2]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3936"]/div[1]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3791"]/div[5]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3791"]/div[4]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3791"]/div[3]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3791"]/div[2]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3791"]/div[1]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[3]/div/div/div/div/div/div[2]/div/img').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[1]/div/div/div[1]/picture/source[5]').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('watchinsurance_Body - verifyied')
    return True
def body_necklaceinsurance(driver):
    print('verifying necklaceinsurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "info-grid-3881")))
    print(driver.find_element_by_id('info-grid-3881').text)
    print(driver.find_element_by_id('info-grid-3996').text)
    print(driver.find_element_by_id('basic-code-block-what-our-policyholders-say').text)
    print(driver.find_element_by_id('accordion-4131').text)
    print(driver.find_element_by_id('feature-row-5186').text)
    print(driver.find_element_by_id('feature-row-4136').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__image-container')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]").text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'title-4001')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'comparison-table etb spacing')]").text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'title-3751')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)
    time.sleep(3)
    print('necklaceinsurance_Body - verifyied')
    return True
def body_braceletinsurance(driver):
    print('verifying braceletinsurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-4061")))
    print(driver.find_element_by_id('title-4061').text)
    print(driver.find_element_by_id('info-grid-3821').text)
    print(driver.find_element_by_id('info-grid-4056').text)
    print(driver.find_element_by_id('basic-code-block-what-our-policyholders-say').text)
    print(driver.find_element_by_id('accordion-4181').text)
    print(driver.find_element_by_id('feature-row-5181').text)
    print(driver.find_element_by_id('feature-row-4186').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'comparison-table__center')]").text)
    time.sleep(3)
    print('braceletinsurance_Body - verifyied')
    return True
def body_smartwatchinsurance(driver):
    print('verifying smartwatchinsurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-4031")))
    print(driver.find_element_by_id('title-4031').text)
    print(driver.find_element_by_id('title-3761').text)
    print(driver.find_element_by_id('info-grid-3851').text)
    print(driver.find_element_by_id('info-grid-4026').text)
    print(driver.find_element_by_id('basic-code-block-what-our-policyholders-say').text)
    print(driver.find_element_by_id('quote-widget-11416').text)
    print(driver.find_element_by_id('feature-row-4161').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'comparison-table etb spacing')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-block-content block--type-block-content13310d8b-6ea7-46ff-8378-d84a47f524f9')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-inline-blockaccordion')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'content-lg text-left')]").text)
    time.sleep(3)
    print('smartwatchinsurance_Body - verifyied')
    return True
def body_howtocleanandcareforyourdiamondring(driver):
    print('verifying howtocleanandcareforyourdiamondring_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-image-row-5206")))
    print(driver.find_element_by_id('text-image-row-5206').text)
    print(driver.find_element_by_id('title-9146').text)
    print(driver.find_element_by_id('info-grid-5236').text)
    print(driver.find_element_by_id('title-5251').text)
    print(driver.find_element_by_id('info-grid-5281').text)
    print(driver.find_element_by_id('title-9151').text)
    print(driver.find_element_by_id('info-grid-5271').text)
    print(driver.find_element_by_id('title-9156').text)
    print(driver.find_element_by_id('info-grid-4776').text)
    print(driver.find_element_by_id('title-5241').text)
    print(driver.find_element_by_id('info-grid-4836').text)
    print(driver.find_element_by_id('feature-row-5246').text)
    print(driver.find_element_by_id('title-9161').text)
    print(driver.find_element_by_id('related-content-9181').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    time.sleep(3)
    print('howtocleanandcareforyourdiamondring_Body - verifyied')
    return True
def body_weinsurejewelry(driver):
    print('verifying weinsurejewelry_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-5551")))
    print(driver.find_element_by_id('title-5551').text)
    print(driver.find_element_by_id('text-image-row-5556').text)
    print(driver.find_element_by_id('title-5561').text)
    print(driver.find_element_by_id('info-grid-5586').text)
    print(driver.find_element_by_id('title-5591').text)
    print(driver.find_element_by_id('basic-code-block-trustpilot-quote').text)
    print(driver.find_element_by_id('image-container-8481').text)
    print(driver.find_element_by_id('info-grid-4886').text)
    print(driver.find_element_by_id('image-container-8486').text)
    print(driver.find_element_by_id('feature-row-8491').text)
    print(driver.find_element_by_id('feature-row-5636').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'navigation__secondary-sticky--links text-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'comparison-table-wrapper')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)
    time.sleep(3)
    print('weinsurejewelry_Body - verifyied')
    return True
def body_coronavirusBusiness(driver):
    print('verifying coronavirusBusiness_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-6626")))
    print(driver.find_element_by_id('text-block-6626').text)
    print(driver.find_element_by_id('text-block-6631').text)
    print(driver.find_element_by_id('text-block-6686').text)
    print(driver.find_element_by_id('text-block-6636').text)
    print(driver.find_element_by_id('cta-group-9496').text)
    print(driver.find_element_by_id('text-block-6861').text)
    print(driver.find_element_by_id('text-block-7411').text)
    print(driver.find_element_by_id('text-block-7526').text)
    print(driver.find_element_by_id('title-7736').text)
    print(driver.find_element_by_id('text-block-7761').text)
    print(driver.find_element_by_id('text-block-6851').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'navigation__secondary-sticky--links text-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)
    time.sleep(3)
    print('coronavirusBusiness_Body - verifyied')
    return True
def body_GuidetoJewelryInsurance(driver):
    print('verifying GuidetoJewelryInsurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-image-row-6926")))
    print(driver.find_element_by_id('text-image-row-6926').text)
    print(driver.find_element_by_id('title-6931').text)
    print(driver.find_element_by_id('info-grid-6971').text)
    print(driver.find_element_by_id('title-7011').text)
    print(driver.find_element_by_id('title-7021').text)
    print(driver.find_element_by_id('quote-widget-6401').text)
    # print(driver.find_element_by_id('feature-row-7031').text)
    print(driver.find_element_by_id('title-7036').text)
    print(driver.find_element_by_id('title-7066').text)
    # print(driver.find_element_by_id('text-block-7151').text)
    print(driver.find_element_by_id('info-grid-7061').text)
    print(driver.find_element_by_id('title-7136').text)
    # print(driver.find_element_by_id('title-7131').text)
    print(driver.find_element_by_id('feature-row-7126').text)
    print(driver.find_element_by_id('title-7141').text)
    # print(driver.find_element_by_id('text-block-7146').text)
    print(driver.find_element_by_id('info-grid-4886').text)
    # print(driver.find_element_by_id('text-block-7166').text)
    # print(driver.find_element_by_id('text-block-7841').text)
    # print(driver.find_element_by_id('feature-row-7171').text)
    print(driver.find_element_by_id('title-7176').text)
    # print(driver.find_element_by_id('text-block-7181').text)
    # print(driver.find_element_by_id('text-block-7191').text)
    print(driver.find_element_by_id('text-image-row-7186').text)
    print(driver.find_element_by_id('text-image-row-7196').text)
    print(driver.find_element_by_id('text-image-row-7201').text)
    print(driver.find_element_by_id('text-image-row-7206').text)
    print(driver.find_element_by_id('title-7211').text)
    # print(driver.find_element_by_id('text-block-7216').text)
    print(driver.find_element_by_id('info-grid-7236').text)
    print(driver.find_element_by_id('feature-row-7246').text)
    # print(driver.find_element_by_id('text-block-7251').text)
    # print(driver.find_element_by_id('text-block-7256').text)
    print(driver.find_element_by_id('basic-code-block-what-our-policyholders-say').text)
    # print(driver.find_element_by_id('feature-row-7266').text)
    # print(driver.find_element_by_id('feature-row-7311').text)
    print(driver.find_element_by_id('info-grid-7306').text)
    print(driver.find_element_by_id('feature-row-7316').text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'navigation__secondary-sticky--links text-center')]").text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-inline-blockinfo-grid block--info-grid background-color-gray')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-inline-blockfeature')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'comparison-table etb spacing')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)
    time.sleep(3)
    print('GuidetoJewelryInsurance_Body - verifyied')
    return True
def body_homepage(driver):
    print('verifying homepage_Body containers')
    time.sleep(3)
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, '//*[@id="block-jewelers-mutual-branding"]/a[1]')))

    # claimsatisfactionratecontent = driver.find_element_by_id('feature-row-2861')
    # print(claimsatisfactionratecontent.text)
    # claimsatisfactionrateimage = driver.find_element_by_id('image-container-8276').is_displayed()
    # print(claimsatisfactionrateimage, " Image is displayed")
    image_whatourpolicyholderssay = driver.find_element_by_id('image-container-8266').is_displayed()
    print(image_whatourpolicyholderssay, " Image is displayed")
    customercareicon = driver.find_element_by_xpath('//img[@alt="customer care graphic"]').is_displayed()
    print(customercareicon, "Icon customer care is displayed")
    print(driver.find_element_by_id('title-46').text)
    print(driver.find_element_by_id('info-grid-8871').text)
    print(driver.find_element_by_id('quote-widget-6401').text)
    print(driver.find_element_by_id('title-151').text)
    print(driver.find_element_by_id('info-grid-136').text)
    print(driver.find_element_by_id('image-container-8251').text)
    print(driver.find_element_by_id('feature-row-141').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]").text)
    time.sleep(3)
    print('homepage_Body - verifyied')
    return True