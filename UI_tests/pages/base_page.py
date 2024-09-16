from .utils import log_message
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

class BasePage:
    def __init__(self,  browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        log_message(f"Открытие страницы:{self.url}")
        self.browser.get(self.url)

    def is_element_present(self, locator, time=10, retry=3):
        for i in range(retry):
            try:
                element = WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator))
                return element
            except StaleElementReferenceException as e:
                log_message(f'Попытка {i+1} из {retry} .Не удалось найти элемент из-за ошибки StaleElementReferenceException... ', 'warning')
            except Exception as e:
                log_message(f'Попытка {i + 1} из {retry} .Не удалось найти элемент из-за  ошибки Exception - {e} ', 'warning')
            except TimeoutException as e:
                log_message("Не удалось за отведенное время найти элемент... Error", 'error')
                return False

    def is_not_element_present(self, locator, time=3):
        try:
             WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator))
        except TimeoutException as e:
            return True
        return False

    def is_disappeared(self, locator, time=2):
        try:
            WebDriverWait(self.browser, time).until_not(EC.presence_of_element_located(locator))
        except TimeoutException as e:
            return False
        return True


    def find_element_and_click_with_retry(self, locator, time=10, retry=3):
        for i in range(retry):
            try:
                WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator)).click()
                return True
            except StaleElementReferenceException as e:
                log_message(f'Попытка {i+1} из {retry} .Не удалось кликнуть на элемент из-за ошибки StaleElementReferenceException... ', 'warning')
            except Exception as e:
                log_message(f'Попытка {i + 1} из {retry} .Не удалось кликнуть на элемент  из-за  ошибки Exception - {e} ', 'warning')
            except TimeoutException as e:
                log_message("Не удалось за отведенное время найти элемент... Error", 'error')
                return False
        # raise TimeoutException("Не удалось за отведенное время найти элемент и кликнуть...")