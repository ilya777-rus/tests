from selenium.webdriver.common.by  import By

class LoginPageLocators:
    USER_NAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')
    ERROR_LOGIN = (By.CSS_SELECTOR, "[data-test='error']")

class HomePageLocators:
    MARK_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    BUTTON_BASKET = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

class ProductsPageLocators:
    NAME_PRODUCT_FIRST = (By.CSS_SELECTOR, ".inventory_list .inventory_item:nth-child(1) .inventory_item_name")
    PRICE_PRODUCT_FIRST = (By.CSS_SELECTOR, ".inventory_list .inventory_item:nth-child(1) .inventory_item_price")
    DESC_PRODUCT_FIRST = (By.CSS_SELECTOR, ".inventory_list .inventory_item:nth-child(1) .inventory_item_desc")
    BUTTON_ADD_FIRST_PRODUCT = (By.ID, "add-to-cart-sauce-labs-backpack")
    BUTTON_REMOVE_FIRST_PRODUCT = (By.ID, "remove-sauce-labs-backpack")

class BasketPageLocators:
    NAME_PRODUCT_IN_BASKET = (By.XPATH, "//div[@class='cart_list']/div[@class='cart_item'][1]//div[@class='inventory_item_name']")
    DESC_PRODUCT_IN_BASKET = (By.XPATH, "//div[@class='cart_list']/div[@class='cart_item'][1]//div[@class='inventory_item_desc']")
    PRICE_PRODUCT_IN_BASKET = (By.XPATH, "//div[@class='cart_list']/div[@class='cart_item'][1]//div[@class='inventory_item_price']")
    ITEM_BASKET = (By.XPATH, "//div[@class='cart_list']/div[@class='cart_item'][1]")

    BUTTON_CHECKOUT = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    BUTTON_CONTINUE = (By.ID, "continue")
    ERROR_CHECK = (By.CSS_SELECTOR, ".error-message-container.error h3[data-test='error']")

    ITEM_TOTAL = (By.CSS_SELECTOR, ".summary_subtotal_label")
    ITEM_TAX = (By.CSS_SELECTOR, ".summary_tax_label")
    TOTAL = (By.CSS_SELECTOR, ".summary_total_label")

    BUTTON_FINISH = (By.ID, "finish")

    MARK_COMPLETE = (By.CSS_SELECTOR, ".pony_express")
    TEXT_COMPLETE = (By.CSS_SELECTOR, ".complete-header")

