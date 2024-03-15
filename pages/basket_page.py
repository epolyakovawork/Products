from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_text_that_basket_is_empty(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPY_MESSAGE) and "Your basket is empty" in self.browser.find_element(
            *BasketPageLocators.BASKET_EMPY_MESSAGE).text, "There is no message that basket is empty"

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty, but should be"
