from .base_page import BasePage
from selenium.webdriver.common.by import By
from .login_page import LoginPage
import time

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        time.sleep(3)
        login_link.click()
        #alert = self.browser.switch_to.alert
        #alert.accept()
        return LoginPage(browser=self.browser, url=self.browser.current_url) 
        
    def should_be_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")
