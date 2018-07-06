from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time
import os
from selenium.webdriver import ActionChains

class SeleniumDriver():


    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            print("Screenshot save to directory: " + destinationFile)
        except:
            print("### Exception Occurred when taking screenshot")
            print_stack()

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "xpath":
            return By.XPATH
        elif locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def getElement(self, locator, locatorType="xpath"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            print("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def getElementList(self, locator, locatorType="xpath"):
        """
        NEW METHOD
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            print("Element list found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            print("Element list not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def elementClick(self, locator="", locatorType="xpath", element=None):
        """
        Click on an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.click()
            print("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            print("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def mouseHower(self, locator="", locatorType="xpath", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            self.actions = ActionChains(self.driver)
            self.actions.move_to_element(element).perform()
            print("Mouse Hovered on element " + locator +
                            " locatorType: " + locatorType)
        except:
            print("Cannot mouse hover on element " + locator +
                    " locatorType: " + locatorType)
            print_stack()



    def sendKeys(self, data, locator="", locatorType="xpath", element=None):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            print("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            print("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def getText(self, locator="", locatorType="xpath", element=None, info=""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator: # This means if locator is not empty
                print("In locator condition")
                element = self.getElement(locator, locatorType)
            print("Before finding text")
            text = element.text
            print("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                print("Getting text on element :: " +  info)
                printo("The text is :: '" + text + "'")
                text = text.strip()
        except:
            print("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="xpath", element=None):
        """
        Check if element is present -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                print("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                print("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="xpath", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                print("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                print("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        """
        Check if element is present
        """
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                print("Element present with locator: " + locator +
                              " locatorType: " + str(byType))
                return True
            else:
                print("Element not present with locator: " + locator +
                              " locatorType: " + str(byType))
                return False
        except:
            print("Element not found")
            return False

    def waitForElement(self, locator, locatorType="xpath",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element

    def webScroll(self, direction="down"):
        """
        NEW METHOD
        """
        if direction == "down":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, 1000);")
        if direction == "medium":
            # Scroll Medium
            self.driver.execute_script("window.scrollBy(0, 500);")

        if direction == "up":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, -1000);")