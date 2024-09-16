from .base_page import BasePage
from .locators import HomePageLocators
from .utils import log_message

class HomePage(BasePage):
    def should_be_mark_product_in_basket(self):
        element_mark = self.is_element_present(HomePageLocators.MARK_PRODUCT_IN_BASKET)
        assert element_mark, "Знак того, что продукт в корзине не обнаружен!"
        log_message("Знак того, что продукт в корзине  обнаружен. ОК.")

    def should_be_go_to_basket(self):
        element_basket = self.find_element_and_click_with_retry(HomePageLocators.BUTTON_BASKET)
        assert element_basket, "Кнопка для просмотра корзины не была найдена или не кликабельна!"
        log_message("Кнопка для просмотра корзины кликнута. ОК.")