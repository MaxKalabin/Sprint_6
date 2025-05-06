from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from test_data import URL
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = BasePageLocators()

    @allure.step('Открытие страницы по {url}')
    def open(self, url=URL):
        self.teardown_method()
        self.driver.get(url)

    @allure.step('Переход через лого Самокат')
    def click_scooter_logo(self):
        scooter_logo = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.locators.SCOOTER_LOGO)
        )
        scooter_logo.click()

    @allure.step('Переход через лого Яндекса')
    def click_yandex_logo(self):
        yandex_logo = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.locators.YANDEX_LOGO)
        )
        yandex_logo.click()

    @allure.step('Ожидание загрузки страницы по URL')
    def wait_for_url(self, expected_url, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(expected_url)
        )

    @allure.step('Получение текущего URL')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Проверка и закрытие дополнительных вкладок')
    def teardown_method(self):
        if len(self.driver.window_handles) > 1:
            self.driver.close()
            self.switching_tabs(0)

    @allure.step('Переключение вкладок в браузере')
    def switching_tabs(self, tab):
        if len(self.driver.window_handles) <= (tab + 1):
            self.driver.switch_to.window(self.driver.window_handles[tab])

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_element_to_be_clickable(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step('Ожидание видимости элемента')
    def wait_for_visibility_of_element(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Проверка видимости элемента")
    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    @allure.step('Прокрутка элемента в область видимости')
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Клик на элемент с прокруткой')
    def click_element(self, locator):
        element = self.wait_for_element_to_be_clickable(locator)
        self.scroll_into_view(element)
        element.click()

    @allure.step('Получение текста элемента')
    def get_element_text(self, locator):
        return self.wait_for_visibility_of_element(locator).text

    @allure.step('Заполнение поля {field_name}')
    def fill_input(self, field_name, locator, text):
        element = self.wait_for_visibility_of_element(locator)
        element.clear()
        element.send_keys(text)