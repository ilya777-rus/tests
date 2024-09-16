from .home_page import HomePage
from .locators import ProductsPageLocators, HomePageLocators
from .utils import log_message

class ProductPage(HomePage):
    def should_be_add_first_product_in_basket(self):
        element_add = self.find_element_and_click_with_retry(ProductsPageLocators.BUTTON_ADD_FIRST_PRODUCT)
        assert element_add, "Кнопка для добавления не кликабельна или не найдена!"
        assert self.is_element_present(ProductsPageLocators.BUTTON_REMOVE_FIRST_PRODUCT), "Кнопка для удаления не отобразилась!"
        self.should_be_mark_product_in_basket()
        name_product = self.is_element_present(ProductsPageLocators.NAME_PRODUCT_FIRST).text
        print('name:', name_product)
        price_product = self.is_element_present(ProductsPageLocators.PRICE_PRODUCT_FIRST).text
        print('price:',price_product)
        desc = self.is_element_present(ProductsPageLocators.DESC_PRODUCT_FIRST).text
        print(desc)
        log_message('Кнопка для добавления товара успешно кликнута! OK.')
        return name_product, price_product, desc