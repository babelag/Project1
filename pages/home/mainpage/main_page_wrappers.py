from base.HandyWrappers import SeleniumDriver
import time

class MainPageWrappers(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    # _polish_flag_button = "//a[@href='/']"
    _english_flag_button = "//div[@class='languages-wrapper']/a[@href='/en/home']"
    _swedish_flag_button = "//div[@class='nav-container w-container']//a[@href='http://solwit.se']"
    _facebook_wrapper = "//div[@class='navbar w-nav']//a[@href='https://www.facebook.com/Solwit/?fref=ts']"
    _twitter_wrapper = "//div[@class='navbar w-nav']//a[@href='https://twitter.com/solwit_team']"
    _linkedin_wrapper = "//div[@class='navbar w-nav']" \
                        "//a[@href='https://www.linkedin.com/company-beta/2341343/?pathWildcard=2341343']"
    _instagram_wrapper = "//div[@class='navbar w-nav']//a[@href='https://www.instagram.com/solwit_team/']"

    #Verify Locators
    # _polish_flag_button_verify1 =
    # _polish_flag_button_verify2 =
    _english_flag_button_verify1 = "//a[@href='#']/div[.='Offer']"
    _english_flag_button_verify2 = "//div[@class='what-we-do-section']//div[@class='offer-subline']"
    _swedish_flag_button_verify1 = "//h1[@class='hero-heading'][contains(text(), 'Nearshore IT-tjänster')]"
    _swedish_flag_button_verify2 = "//a[@href='#Komplett-erbjudande']"
    _facebook_wrapper_verify1 = "//i[@class='fb_logo img sp_lQnvSzqUkvK sx_b7adef']"
    _facebook_wrapper_verify2 = "//div[@id='u_0_d']//img[@alt='']"
    _twitter_wrapper_verify1 = "//input[@id='search-query']"
    _twitter_wrapper_verify2 = "//li[@id='global-nav-home']/a[@href='/']"
    _linkedin_wrapper_verify1 = "//div[@id='control_gen_1']//div[@class='logo_container']"
    _linkedin_wrapper_verify2 = "//input[@id='session_key-login']"
    _instagram_wrapper_verify1 = "//h1[@title='solwit_team']"
    _instagram_wrapper_verify2 = "//div[@class='aU2HW']/a[1]"


    # def clickPolishFlagWrapper(self):
    #     result = self.elementClick(self._polish_flag_button)
    #     return result

    def clickEnglishFlagWrapper(self):
        return self.elementClick(self._english_flag_button)


    def clickSwedishFlagWrapper(self):
        return self.elementClick(self._swedish_flag_button)


    def clickFacebookWrapper(self):
        return self.elementClick(self._facebook_wrapper)


    def clickTwitterWrapper(self):
        return self.elementClick(self._twitter_wrapper)


    def clickLinkedinWrapper(self):
        return self.elementClick(self._linkedin_wrapper)


    def clickInstagramWrapper(self):
        return self.elementClick(self._instagram_wrapper)


    def verifyEnglishFlagWrapper(self):
        result1 = self.isElementPresent(self._english_flag_button_verify1)
        result2 = self.isElementPresent(self._english_flag_button_verify1)
        return result1,result2

    def verifySwedishFlagWrapper(self):
        result1 = self.isElementPresent(self._swedish_flag_button_verify1)
        result2 = self.isElementPresent(self._swedish_flag_button_verify2)
        return result1,result2

    def verifyFacebookWrapper(self):
        result1 = self.isElementPresent(self._facebook_wrapper_verify1)
        result2 = self.isElementPresent(self._facebook_wrapper_verify2)
        return result1, result2

    def verifyTwitterWrapper(self):
        result1 = self.isElementPresent(self._twitter_wrapper_verify1)
        result2 = self.isElementPresent(self._twitter_wrapper_verify2)
        return result1, result2

    def verifyLinkedinWrapper(self):
        result1 = self.isElementPresent(self._linkedin_wrapper_verify1)
        result2 = self.isElementPresent(self._linkedin_wrapper_verify2)
        return result1, result2


    def verifyInstagramWrapper(self):
        result1 = self.isElementPresent(self._instagram_wrapper_verify1)
        result2 = self.isElementPresent(self._instagram_wrapper_verify2)
        return result1, result2

    def englishFlagWrapper(self):
        self.clickEnglishFlagWrapper()
        self.verifyEnglishFlagWrapper()

    def swedishFlagWrapper(self):
        self.clickSwedishFlagWrapper()
        time.sleep(3)
        parentHandle = self.driver.current_window_handle
        print("Parent Handle: " + parentHandle)
        handles = self.driver.window_handles

        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                print("Switched to window: " + handle)
                self.verifySwedishFlagWrapper()
                time.sleep(2)
                self.driver.close()
                self.driver.switch_to.window(parentHandle)
                break

    def facebookWrapper(self):
        self.clickFacebookWrapper()
        time.sleep(2)
        parentHandle = self.driver.current_window_handle
        print("Parent Handle: " + parentHandle)
        handles = self.driver.window_handles

        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                self.verifyFacebookWrapper()
                time.sleep(2)
                self.driver.close()
                self.driver.switch_to.window(parentHandle)
                break

    def twitterWrapper(self):
        self.clickTwitterWrapper()
        time.sleep(2)
        parentHandle = self.driver.current_window_handle
        print("Parent Handle: " + parentHandle)
        handles = self.driver.window_handles

        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                self.verifyTwitterWrapper()
                time.sleep(2)
                self.driver.close()
                self.driver.switch_to.window(parentHandle)
                break

    def linkedinWrapper(self):
        self.clickLinkedinWrapper()
        time.sleep(2)
        parentHandle = self.driver.current_window_handle
        print("Parent Handle: " + parentHandle)
        handles = self.driver.window_handles

        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                self.verifyLinkedinWrapper()
                time.sleep(2)
                self.driver.close()
                self.driver.switch_to.window(parentHandle)
                break

    def instagramWrapper(self):
        self.clickInstagramWrapper()
        time.sleep(2)
        parentHandle = self.driver.current_window_handle
        print("Parent Handle: " + parentHandle)
        handles = self.driver.window_handles

        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                self.verifyInstagramWrapper()
                time.sleep(2)
                self.driver.close()
                self.driver.switch_to.window(parentHandle)
                break
