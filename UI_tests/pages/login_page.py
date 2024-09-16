from .base_page import BasePage
from .locators import LoginPageLocators
from .utils import log_message
class LoginPage(BasePage):

    def shoul_be_login_link(self, user_name:str, password:str):
        user_name_element = self.is_element_present(LoginPageLocators.USER_NAME)
        assert user_name_element, "Элемент user_name не был найден"
        user_name_element.send_keys(user_name)
        log_message("Поле user_name успешно заполнено. ОК.")

        password_element = self.is_element_present(LoginPageLocators.PASSWORD)
        assert password_element, "Элемент password_element не был найден"
        password_element.send_keys(password)
        log_message("Поле password успешно заполнено. ОК.")
        login_button = self.find_element_and_click_with_retry(LoginPageLocators.LOGIN_BUTTON)
        assert login_button, "Кнопка для авторизации не была найдена или не кликабельна!"
        log_message("Кнопка для авторизации была кликнута! OK.")
        assert self.is_not_element_present(LoginPageLocators.ERROR_LOGIN), "Авторизация не удалась!"
        log_message("Авторизация прошла успешно! ОК.")