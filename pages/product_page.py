from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_name(self):
        return self.browser.find_element(By.CSS_SELECTOR, '.product_main > h1').text

    def get_price(self):
        return self.browser.find_element(By.CSS_SELECTOR, '.product_main > p.price_color').text

    def good_was_added(self):
        self.should_be_message_of_success()
        self.product_name_should_be_in_message(self.get_product_name())
        self.should_be_message_basket_total()
        self.price_in_basket_matches_product_price(self.get_price())

    def should_be_message_of_success(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is missing"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def product_name_should_be_in_message(self, product_name):
        assert product_name == self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text, "Wrong product name in the message"

    def should_be_message_basket_total(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_BASKET_TOTAL), "Basket total message is missing"

    def price_in_basket_matches_product_price(self, price):
        assert price == self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL).text, "The price doesn't match"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message wasn't disappeared"
