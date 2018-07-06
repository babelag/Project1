from selenium import webdriver
from pages.home.mainpage.main_page_navigation import MainPageNavigation
import unittest

class TestMenuNavigation(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        baseURL = 'https://www.solwit.com/'
        self.driver.get(baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.mpm = MainPageNavigation(self.driver)


    def test_validation_home_button(self):
        print('****'*10 + "HOME BUTTON TEST" +'****'*10)
        self.mpm.home()

    def test_validation_offer_button(self):
        print('****' * 10 + "OFFER BUTTON TEST" + '****' * 10)
        self.mpm.offer()

    def test_validation_caseStudies_button(self):
        print('****' * 10 + "STUDY BUTTON TEST" + '****' * 10)
        self.mpm.case_studies()

    def test_validation_career_button(self):
        print('****' * 10 + "CAREER BUTTON TEST" + '****' * 10)
        self.mpm.career()

    def test_validation_aboutUs_button(self):
        print('****' * 10 + "ABOUT US BUTTON TEST" + '****' * 10)
        self.mpm.aboutUs()

    def test_validation_Contact_button(self):
        print('****' * 10 + "CONTACT BUTTON TEST" + '****' * 10)
        self.mpm.contact()


    @classmethod
    def tearDownClass(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()



