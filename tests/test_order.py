import pytest
import allure
from selenium import webdriver

from page_objects.base_page import BasePage
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from test_data import *


@allure.feature("Тесты: Заказ самоката")
class TestOrder:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.base_page = BasePage(cls.driver)
        cls.main_page = MainPage(cls.driver)
        cls.order_page = OrderPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title("Процесс заказа самоката через верхнюю кнопку")
    def test_order_via_top_button(self):
        self.main_page.open()
        order_data = ORDER_DATA[0]
        self._perform_order_flow(order_data)

    @allure.title("Процесс заказа самоката через нижнюю кнопку")
    def test_order_via_bottom_button(self):
        self.main_page.open()
        order_data = ORDER_DATA[1]
        self._perform_order_flow(order_data)

    def _perform_order_flow(self, order_data):
        order_button_locator = self.main_page.locators.ORDER_BUTTON_TOP if order_data["order_button_locator"] == "top" else self.main_page.locators.ORDER_BUTTON_BOTTOM

        with allure.step(f"Клик по кнопке Заказать - {order_data["order_button_locator"]}"):
            self.main_page.click_order_button(order_button_locator)

        with allure.step("Заполнение формы заказа"):
            self.order_page.fill_order_form(
                order_data["name"],
                order_data["surname"],
                order_data["address"],
                order_data["metro_station"],
                order_data["phone"]
            )
            self.order_page.fill_rental_details(
                order_data["rental_period"],
                order_data["color"],
                order_data["comment"]
            )

        with allure.step("Клик на кнопке Заказать в конце формы заказа"):
            self.order_page.click_order_button()

        with allure.step("Проверка подтверждения заказа"):
            self.order_page.click_confirmation_button()

        with allure.step("Подтверждение заказа и переход на следующую страницу"):
            self.order_page.click_check_status_button()

        with allure.step("Переход на главную через логотип Самокат"):
            self.base_page.click_scooter_logo()
            self.base_page.wait_for_url(URL)
            assert self.driver.current_url == URL

        with allure.step("Переход на Дзен через логотип Яндекс"):
            self.base_page.click_yandex_logo()
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.base_page.wait_for_url('dzen.ru')
            assert "dzen.ru" in self.driver.current_url
