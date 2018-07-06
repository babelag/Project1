from base.selenium2 import SeleniumDriver

class MainPageTabsWrappers(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locator
    _software_development_wrapper = "//div[@class='tabs-menu w-tab-menu']/a[1]"
    _test_services_wrapper = "//div[@class='tabs-menu w-tab-menu']/a[2]"
    _cloud_transformation_wrapper = "//div[@class='tabs-menu w-tab-menu']/a[3]"
    _lab_infrastructure_management_wrapper = "//div[@class='tabs-menu w-tab-menu']/a[4]"

    #Verify locators
    _software_development_wrapper_verify1 = "//div[@data-w-tab = 'SOFTWARE DEVELOPMENT']"
    _software_development_wrapper_verify2 = "//div[@class='offer-tabs w-tabs']//div[contains(text(), 'DEPLOYMENT')]"
    _test_services_wrapper_verify1 = "//div[@data-w-tab = 'TEST SERVICES']"
    _test_services_wrapper_verify2 = "//div[@class='white-project-name'][contains(text(), 'graphics card.')]"
    _cloud_transformation_wrapper_verify1 = "//div[@data-w-tab = 'CLOUD TRANSFORMATION']"
    _cloud_transformation_wrapper_verify2 = "//div[@class='main-subtext-tab'][contains(text(), 'OPERACJE W CHMURZE')]"
    _lab_infrastructure_management_wrapper_verify1 = "//div[@data-w-tab = 'LAB INFRASTRUCTURE MANAGEMENT']"
    _lab_infrastructure_management_wrapper_verify2 = "//div[contains(text(), 'LAB SPACE LEASE')]"

    def clickSoftwareDevelopmentWrapper(self):
        return self.elementClick(self._software_development_wrapper)

    def clickTestServicesWrapper(self):
        return self.elementClick(self._test_services_wrapper)

    def clickCloudTransformationWrapper(self):
        return self.elementClick(self._cloud_transformation_wrapper)

    def clickLabInfrastructureManagementWrapper(self):
        return self.elementClick(self._lab_infrastructure_management_wrapper)

    def verifySoftwareDeveloperWrapper(self):
        result1 = self.isElementPresent(self._software_development_wrapper_verify1)
        result2 = self.isElementPresent(self._software_development_wrapper_verify2)
        return result1, result2

    def verifyTestServicesWrapper(self):
        result1 = self.isElementPresent(self._test_services_wrapper_verify1)
        result2 = self.isElementPresent(self._test_services_wrapper_verify2)
        return result1, result2

    def verifyCloudTransformationWrapper(self):
        result1 = self.isElementPresent(self._cloud_transformation_wrapper_verify1)
        result2 = self.isElementPresent(self._cloud_transformation_wrapper_verify2)
        return result1, result2

    def verifyLabInfrastructureManagementWrapper(self):
        result1 = self.isElementPresent(self._lab_infrastructure_management_wrapper_verify1)
        result2 = self.isElementPresent(self._lab_infrastructure_management_wrapper_verify2)
        return result1, result2

    def verifyPageName(self):
        result = self.driver.title
        if result == "Home":
            print(f"Correct Page Name : {result}")
        else:
            print(f"Incorrect Page Name : {result}")
        return result



    def softwareDevelopmentWrapper(self):
        self.clickSoftwareDevelopmentWrapper()
        self.verifySoftwareDeveloperWrapper()

    def testsServicesWrapper(self):
        self.clickTestServicesWrapper()
        self.verifyTestServicesWrapper()

    def cloudTransformationWrapper(self):
        self.clickCloudTransformationWrapper()
        self.verifyCloudTransformationWrapper()

    def labInfrastructureManagementWrapper(self):
        self.clickLabInfrastructureManagementWrapper()
        self.verifyLabInfrastructureManagementWrapper()