from pages.home.mainpage.main_page_tabs_wrappers import MainPageTabsWrappers
from selenium import webdriver
import unittest

class TestWrappers(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="C:\\TestFiles\\chromedriver.exe")
        baseURL = 'https://www.solwit.com/'
        self.driver.get(baseURL)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.mptw = MainPageTabsWrappers(self.driver)
        self.driver.execute_script("window.scrollBy(0,900);")

    def test_validation_softwareDevelopmentWrapper(self):
        print('****' * 10 + "SOFTWARE DEVELOPMENT WRAPPER TEST" + '****' * 10)
        self.mptw.softwareDevelopmentWrapper()
        self.mptw.verifyPageName()

    def test_validation_testsServicesWrapper(self):
        print('****' * 10 + "TESTS SERVICES WRAPPER TEST" + '****' * 10)
        self.mptw.testsServicesWrapper()
        self.mptw.verifyPageName()

    def test_validation_cloudTransformationWrapper(self):
        print('****' * 10 + "CLOUD TRANSFORMATION WRAPPER TEST" + '****' * 10)
        self.mptw.cloudTransformationWrapper()
        self.mptw.verifyPageName()

    def test_validation_labInfrastructureManagementWrapper(self):
        print('****' * 10 + "LAB INFRASTRUCTURE MANAGEMENT WRAPPER TEST" + '****' * 10)
        self.mptw.labInfrastructureManagementWrapper()
        self.mptw.verifyPageName()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()



