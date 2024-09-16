from .home_page import HomePage
from .locators import BasketPageLocators, HomePageLocators
from .utils import log_message

class BasketPage(HomePage):
    def should_be_check_product_in_basket(self, name:str, price:str, desc:str):
        assert self.is_element_present(BasketPageLocators.ITEM_BASKET), "Товар не был добавлен в корзину!"
        element_name = self.is_element_present(BasketPageLocators.NAME_PRODUCT_IN_BASKET).text
        assert element_name==name, "Название товара в корзине не соответствует названию из списка товаров!"
        element_price = self.is_element_present(BasketPageLocators.PRICE_PRODUCT_IN_BASKET).text
        assert element_price==price, "Цена товара в корзине не соответствует цене товара из списка товаров!"
        element_desc = self.is_element_present(BasketPageLocators.DESC_PRODUCT_IN_BASKET).text.strip()
        assert element_desc==desc, "Описание товара в корзине не соответствует описанию товара из списка товаров!"
        log_message("Товар успешно добавлен в корзину! ОК.")

    def should_be_click_checkout(self):
        element_checkout = self.find_element_and_click_with_retry(BasketPageLocators.BUTTON_CHECKOUT)
        assert element_checkout, "Кнопка для проверки не найдена или не кликабельна!"
        log_message("Кнопка для проверки кликнута! ОК.")

    def checkout_product(self):
        first_name = self.is_element_present(BasketPageLocators.FIRST_NAME)
        assert first_name, "Поле first_name не найдено!"
        first_name.send_keys('Ilya')
        log_message("Поле first_name заполнено! ОК.")
        last_name = self.is_element_present(BasketPageLocators.LAST_NAME)
        assert last_name, "Поле last_name не найдено!"
        last_name.send_keys("Nikolaev")
        log_message("Поле last_name заполнено! ОК.")
        postal_code = self.is_element_present(BasketPageLocators.POSTAL_CODE)
        assert postal_code, "Поле postal_code не найдено!"
        postal_code.send_keys('465291')
        log_message("Поле postal code успешно заполнено! ОК.")
        element_continue = self.find_element_and_click_with_retry(BasketPageLocators.BUTTON_CONTINUE)
        assert element_continue, "Кнопка для продолжения не найдена или не кликабельна!"
        assert self.is_not_element_present(BasketPageLocators.ERROR_CHECK), "Ошибка.Проверьте заполнены ли поля успешно!"
        log_message('Поля успешно заполнены, кнопка для продолжения кликнута! ОК.')

    def after_checkout(self):
        element_price = self.is_element_present(BasketPageLocators.PRICE_PRODUCT_IN_BASKET).text
        item_total =self.is_element_present(BasketPageLocators.ITEM_TOTAL).text.strip()
        price=item_total.split()
        assert element_price==price[-1], "Цена товара не соответствет после оформления его!"
        element_total = self.is_element_present(BasketPageLocators.TOTAL).text.strip()
        price_total = element_total.split('$')
        element_tax = self.is_element_present(BasketPageLocators.ITEM_TAX).text.strip()
        tax = element_tax.split('$')[-1]
        itog = float(tax) + float(price[-1][1:])
        assert float(price_total[-1])==itog, "Итоговая сумма не совпадает!"
        log_message("Проверка оформления выполнена! ОК.")
        finish_button = self.find_element_and_click_with_retry(BasketPageLocators.BUTTON_FINISH)
        assert finish_button, "Кнопка для завершения finish не найдена или не кликабельна!"
        log_message('Кнопка для завершения finish успешно кликнута! ОК.')
        #  print(element_total)
        # print(element_price==price[-1])

    def should_be_complete_checkout(self):
        assert self.is_disappeared(HomePageLocators.MARK_PRODUCT_IN_BASKET), "Марка того что товар в корзине не исчез!"
        element_mark_complete = self.is_element_present(BasketPageLocators.MARK_COMPLETE)
        assert element_mark_complete, "Знак того что покупка завершена не обнаружен"
        element_text_complete = self.is_element_present(BasketPageLocators.TEXT_COMPLETE)
        assert element_text_complete, "Текст того что покупка завершена не обнаружен!"
        self.should_be_go_to_basket()
        assert self.is_disappeared(BasketPageLocators.ITEM_BASKET), "Товар остался в корзине!"
        log_message("Покупка завершена успешно. ОК.")
