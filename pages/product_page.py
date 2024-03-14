from selenium.webdriver.common.by import By
from selenium import webdriver
from .base_page import BasePage
from .main_page import MainPage
from selenium import webdriver
browser = webdriver.Chrome()

class ProductPage(BasePage):
   
    def should_be_add_to_basket_button(self):
        basket = browser.find_element(*BasketLocators.ADD_BASKET)
        #login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        basket.click()
        print(basket.text)
        time.sleep(5)
        assert self.is_element_present(*BasketLocators.ADD_BASKET), "Add to basket is not presented"
        ADD_BASKET = (By.CSS_SELECTOR, "btn.btn-lg.btn-primary.btn-add-to-basket")

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


   
