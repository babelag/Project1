from base.selenium2 import SeleniumDriver

class MainFooterFlex(SeleniumDriver):

     def __init__(self, driver):
          super().__init__(driver)
          self.driver = driver

     #Locators
     _name = "//input[@id='name']"
     _company_name= "//input[@id='Nazwa-firmy']"
     _telephon_number = "//input[@id='Numer-telefonu']"
     _email_adress = "//input[@id='Email-3']"
     _content = "//textarea[@id='Tre']"
     _agreement = "//input[@id='Zgoda']"
     _submit_button = "//form[@id='wf-form-Kontakt']//input[@value='Wyślij']"
     _success_message_element = "//div[@class='footer-wrapper']//div[@class='success-message w-form-done']"


     def clickNameElement(self):
          self.elementClick(self._name)

     def enterName(self, name):
          self.sendKeys(name, self._name)

     def clickCompanyNameElement(self):
          self.elementClick(self._company_name)

     def enterCompanyName(self, companyname):
          self.sendKeys(companyname, self._company_name)

     def clickTelephonNumberElement(self):
          self.elementClick(self._telephon_number)

     def enterTelephonNumber(self, telephon):
          self.sendKeys(telephon, self._telephon_number)

     def clickEmailAdressElement(self):
          self.elementClick(self._email_adress)

     def enterEmailAdress(self, email):
          self.sendKeys(email, self._email_adress)

     def clickContentElement(self):
          self.elementClick(self._content)

     def enterContent(self, content):
          self.sendKeys(content, self._content)

     def clickAgreementElement(self):
          self.elementClick(self._agreement)

     def clickSubmitButton(self):
          self.elementClick(self._submit_button)

     def verifyAgreementElementDisplayed(self):
          result = self.isElementDisplayed(self._agreement)
          return result

     def verifyMessageSuccessText(self):
          result = self.isElementPresent(self._success_message_element)
          return result


     def message(self, name, companyname, telephon, email, content):
          self.clickNameElement()
          self.enterName(name)
          self.clickCompanyNameElement()
          self.enterCompanyName(companyname)
          self.clickTelephonNumberElement()
          self.enterTelephonNumber(telephon)
          self.clickEmailAdressElement()
          self.enterEmailAdress(email)
          self.clickContentElement()
          self.enterContent(content)

