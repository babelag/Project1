from base.selenium2 import SeleniumDriver

class MainPageOfferTabLinkHover(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _navigation_offer_button = "//div/a[@href='#']/div[.='OFerta']"
    _software_development = "//a[@class = 'offer-tab-link w-inline-block']//div[contains(text(), 'SOFTWARE')]"
    _test_services = "//a[@class = 'offer-tab-link w-inline-block']//div[contains(text(), 'TEST')]"
    _cloud_transformation = "//a[@class = 'offer-tab-link w-inline-block']//div[contains(text(), 'CLOUD')]"
    _lab_infrastructure = "//a[@class = 'offer-tab-link w-inline-block']//div[contains(text(), 'LAB')]"

    #methods

    def clickOfferButton(self):
        self.elementClick(self._navigation_offer_button)


    def hoverSoftwareDevelopment(self):
        self.mouseHover(self._software_development)
        self.screenShot('softwareHoverd')

    def hoverTestServices(self):
        self.mouseHover(self._test_services)
        self.screenShot('testHovered')

    def hoverCloudTransformation(self):
        self.mouseHover(self._cloud_transformation)
        self.screenShot('loudHovered')

    def hoverLabInfrastructure(self):
        self.mouseHover(self._lab_infrastructure)
        self.screenShot('labHovered')

    #funkctionality
    def main_offer_hovered(self):
        self.clickOfferButton()
        self.hoverTestServices()
        self.hoverSoftwareDevelopment()
        self.hoverCloudTransformation()
        self.hoverLabInfrastructure()

