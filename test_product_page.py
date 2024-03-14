import pytest
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators
import time
import math

def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    page = MainPage(browser, link)    
    page.open()
    time.sleep(7)
    addToBasket = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    addToBasket.click()
    time.sleep(5)   
    alert = browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    print(answer)
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")
        time.sleep(5)
        browser.quit()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    page = MainPage(browser, link)    
    page.open()
    time.sleep(7)
    page.go_to_login_page()
    time.sleep(7)
    mail = browser.find_element(By.CSS_SELECTOR, "#id_registration-email")
    mail.send_keys("testmail@mail.com")
    pass1 = browser.find_element(By.CSS_SELECTOR, "#id_registration-password1")
    pass1.send_keys("123QWE!@#")
    pass1 = browser.find_element(By.CSS_SELECTOR, "#id_registration-password2")
    pass1.send_keys("123QWE!@#")
    btn = browser.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/button")
    btn.click()

def test_user_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    page = MainPage(browser, link)    
    page.open()
    time.sleep(7)
    page.go_to_login_page()
    time.sleep(7)
    mail2 = browser.find_element(By.CSS_SELECTOR, "#id_login-username")
    mail2.send_keys("testmail@mail.com")
    pass3 = browser.find_element(By.CSS_SELECTOR, "#id_login-password")
    pass3.send_keys("123QWE!@#")
    btn = browser.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/div[1]/form/button")
    btn.click()
    linkBook = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    page = MainPage(browser, linkBook)    
    page.open()
    time.sleep(7)
    addToBasket = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    addToBasket.click()
    time.sleep(5)   
    alert = browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    print(answer)
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")
        time.sleep(5)
        browser.quit()
    
    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    page = MainPage(browser, link)    
    page.open()
    time.sleep(7)
    addToBasket = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    addToBasket.click()
    time.sleep(5)   
    alert = browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    print(answer)
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")
        time.sleep(5)
        book = browser.find_element(By.CSS_SELECTOR, "h1")
    basket = browser.find_element(By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    basket.click()
    time.sleep(10)
    browser.quit()
    
