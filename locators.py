from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators():
    LOGIN_URL = browser.current_url
    #assert "login" in LOGIN_URL, "Login is absent in the URL"
    LOGIN_FORM = (By.CSS_SELECTOR, ".col-sm-6.login_form")
    #assert self.is_element_present(By.CSS_SELECTOR, "#login_form"), "Login form is not presented"
    REGISTER_FORM = (By.CSS_SELECTOR, ".col-sm-6.register_form")
    #assert self.is_element_present(By.CSS_SELECTOR, "#register_form"), "Register form is not presented"

