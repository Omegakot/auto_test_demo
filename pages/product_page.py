
from .base_page import BasePage
from .locators import MainPageLocators

class Page_Object(BasePage): 
    def add_to_basket(self):
        link = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET)
        link.click()
        