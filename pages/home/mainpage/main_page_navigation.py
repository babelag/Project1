from base.selenium2 import SeleniumDriver

class MainPageNavigation(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _home_button = "//nav[@role='navigation']/a[@href='/en/home']"
    _offer_button = "//a[@href='#'][contains(text(), 'Offer')]"
    _caseStudies_button = "//a[@href='#']/div[.='Case StudieS']"
    _carrer_button = "//a[@href='#'][contains(text(),'Career')]"
    _aboutUs_button = "//a[@href='#']/div[.='About us']"
    _contact_button = "//div[@class='nav-container w-container']//a[@href='/en/contact']"
    
    #Locators to verify
    _home_button_verify1 = "//video"
    _home_button_verify2 = "//div[@class='header-section']//div[@class='slide-mid-section']"
    _offer_button_verify1 = "//a[@href='/en/services/software-development']/img"
    _offer_button_verify2 = "//div[@class='header-section']//div[@class='slide-mid-section']"
    _caseStudy_button_verify1 = "//h3[@class='career-heading'][contains(text(),'Case studies')]"
    _caseStudy_button_verify2 = "//div[@class='dynamic-case-wrapper w-dyn-list']"
    _career_button_verify1 = "//h3[@class='career-heading'][contains(text(), 'Career')]"
    _career_button_verify2 = "//h4[@class='latest-offers-text']"
    _aboutUs_button_verify1 = "//h3[@class='career-heading'][contains(text(),'About us')]"
    _aboutUs_button_verify2 = "//div[@class='news-menu-heading'][contains(text(),'Solwit')]"
    _contact_button_verify1 = "//h1[@class='service-heading']"
    _contact_button_verify2 = "//h3[@class='service-heading']"

    #methods
    def clickHomeButton(self):
        return self.elementClick(self._home_button)

    def clickOfferButton(self):
        return self.elementClick(self._offer_button)

    def clickCaseStudyButton(self):
        return self.elementClick(self._caseStudies_button)

    def clickCarrerButton(self):
        return self.elementClick(self._carrer_button)

    def clickAboutUsButton(self):
        return self.elementClick(self._aboutUs_button)

    def clickContactButton(self):
        return self.elementClick(self._contact_button)

    def verifyHomeButton(self):
        result = self.isElementPresent(self._home_button_verify1)
        result1 = self.isElementPresent(self._home_button_verify2)
        return result, result1

    def verifyOfferButton(self):
        result = self.isElementPresent(self._offer_button_verify1)
        result1 = self.isElementPresent(self._offer_button_verify2)
        return result, result1

    def verifyCaseStudyButton(self):
        result = self.isElementPresent(self._caseStudy_button_verify1)
        result1 = self.isElementPresent(self._caseStudy_button_verify2)
        return result, result1

    def verifyCareerButton(self):
        result = self.isElementPresent(self._career_button_verify1)
        result1 = self.isElementPresent(self._career_button_verify2)
        return result, result1

    def verifyAboutUsButton(self):
        result = self.isElementPresent(self._aboutUs_button_verify1)
        result1 = self.isElementPresent(self._aboutUs_button_verify2)
        return result, result1

    def verifyContactButton(self):
        result = self.isElementPresent(self._contact_button_verify1)
        result1 = self.isElementPresent(self._contact_button_verify2)
        return result, result1

    def scrollDown(self):
        result = self.driver.execute_script("window.scrollTo(0,1000);")
        return result

    def scrollUp(self):
        result = self.driver.execute_script("window.scrollTo(0,-1000);")
        return result


    #functionality
    def home(self):
        self.clickHomeButton()
        self.verifyHomeButton()
        self.scrollUp()
        self.getTitle()


    def offer(self):
        self.clickOfferButton()
        self.verifyOfferButton()
        self.scrollUp()

    def case_studies(self):
        self.clickCaseStudyButton()
        self.verifyCaseStudyButton()
        self.scrollUp()

    def career(self):
        self.clickCaseStudyButton()
        self.verifyCareerButton()
        self.scrollUp()

    def aboutUs(self):
        self.clickAboutUsButton()
        self.verifyAboutUsButton()
        self.scrollUp()

    def contact(self):
        self.clickContactButton()
        self.verifyContactButton()
        self.scrollUp()





