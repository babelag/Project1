from pages.home.mainpage.main_page_navigation_tab_link import MainPageOfferTabLinkHover
import unittest
from selenium import webdriver

class TestHover(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="C:\\TestFiles\\chromedriver.exe")
        baseURL = "https://www.solwit.com/"
        self.driver.get(baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.mpotlh = MainPageOfferTabLinkHover(self.driver)

    def test_mouse_hover_offer_tab_link(self):
        self.mpotlh.main_offer_hovered()


    @classmethod
    def tearDownClass(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
