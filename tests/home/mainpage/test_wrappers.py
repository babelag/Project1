from selenium import webdriver
from pages.home.mainpage.main_page_wrappers import MainPageWrappers
import unittest

class TestWrappers(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        baseURL = 'https://www.solwit.com/'
        self.driver.get(baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.mpw = MainPageWrappers(self.driver)

    def test_validation_englishFlagWrapper(self):
        print('****' * 10 + "ENGLISH FLAG WRAPPER TEST" + '****' * 10)
        self.mpw.englishFlagWrapper()

    def test_validation_swedishFlagWrapper(self):
        print('****' * 10 + "SWEDISH FLAG WRAPPER TEST" + '****' * 10)
        self.mpw.swedishFlagWrapper()

    def test_validation_facebookWrapper(self):
        print('****' * 10 + "FACEBOOK WRAPPER TEST" + '****' * 10)
        self.mpw.facebookWrapper()

    def test_validation_twitterWrapper(self):
        print('****' * 10 + "TWITTER WRAPPER TEST" + '****' * 10)
        self.mpw.twitterWrapper()

    def test_validation_linkedinWrapper(self):
        print('****' * 10 + "LINKEDIN WRAPPER TEST" + '****' * 10)
        self.mpw.linkedinWrapper()

    def test_validation_instagramWrapper(self):
        print('****' * 10 + "INSTAGRAM WRAPPER TEST" + '****' * 10)
        self.mpw.instagramWrapper()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()



