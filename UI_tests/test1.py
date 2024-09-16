import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductPage
from pages.basket_page import BasketPage
from pages.utils import log_message
import time
LINK = "https://www.saucedemo.com/"

def test_login(browser):
    log_message("Start test_login")
    login_page = LoginPage(browser, LINK)
    login_page.open()
    login_page.shoul_be_login_link("standard_user", "secret_sauce")
    product_page = ProductPage(browser, browser.current_url)
    name, price, desc = product_page.should_be_add_first_product_in_basket()
    product_page.should_be_go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_check_product_in_basket(name, price, desc)
    basket_page.should_be_click_checkout()
    basket_page.checkout_product()
    basket_page.after_checkout()
    basket_page.should_be_complete_checkout()
    time.sleep(5)
    log_message("End test_login\n")