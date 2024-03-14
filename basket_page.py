from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in browser.current_url, "Login is absent in the URL"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

