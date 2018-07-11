from pages.home.mainpage.main_footer_flex import MainFooterFlex
from selenium import webdriver
import unittest
import time

class TestWrappers(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="C:\\TestFiles\\chromedriver.exe")
        baseURL = 'https://www.solwit.com/'
        self.driver.get(baseURL)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.mff = MainFooterFlex(self.driver)
        self.mff.webScroll()

    def test_validation_message_sending(self):
        self.mff.message("Test", "Test Company", "123456789", "test@test.pl", "Test Content")
        self.mff.clickAgreementElement()
        self.mff.verifyAgreementElementDisplayed()
        self.mff.clickSubmitButton()
        time.sleep(5)
        self.mff.verifyMessageSuccessText()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
