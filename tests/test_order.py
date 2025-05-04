import pytest
import allure
from selenium import webdriver
from page_objects.base_page import BasePage
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from test_data import *

@allure.feature('Тесты: Заказ самоката')
class TestOrder:

    @classmethod
    def setup_class(cls):
        with allure.step('Открываем браузер Firefox'):
            cls.driver = webdriver.Firefox()
            cls.base_page = BasePage(cls.driver)
            cls.main_page = MainPage(cls.driver)
            cls.order_page = OrderPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        with allure.step('Открываем браузер Firefox'):
            cls.driver.quit()

    @allure.title('Процесс заказа самоката через верхнюю кнопку')
    @pytest.mark.parametrize("order_data", [ORDER_DATA[0]])
    def test_order_via_top_button(self, order_data):
        self._run_test(order_data, "top")

    @allure.title('Процесс заказа самоката через нижнюю кнопку')
    @pytest.mark.parametrize("order_data", [ORDER_DATA[1]])
    def test_order_via_bottom_button(self, order_data):
        self._run_test(order_data, "bottom")

    def _run_test(self, order_data, button_type):
        self.base_page.open(URL)
        self.main_page.click_order_button(button_type)
        self.order_page.fill_order_form(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro_station"],
            order_data["phone"]
        )
        assert self.order_page.is_second_page_opened(), "Не перешли на вторую страницу"

        self.order_page.fill_rental_details(
            order_data["rental_period"],
            order_data["color"],
            order_data["comment"]
        )
        self.order_page.click_order_button()
        assert self.order_page.is_confirmation_popup_opened(), "Окно подтверждения не появилось"

        self.order_page.click_confirmation_button()
        assert self.order_page.is_status_page_opened(), "Не перешли на страницу статуса заказа"
        self.order_page.click_check_status_button()

        self.base_page.click_scooter_logo()
        self.base_page.wait_for_url(URL)
        assert self.base_page.current_url() == URL, f"Ожидался URL '{URL}', но получен '{self.base_page.current_url()}'"

        self.base_page.click_yandex_logo()
        self.base_page.switching_tabs(1)
        self.base_page.wait_for_url(DZEN_URL)
        assert DZEN_URL in self.base_page.current_url(), f"Не перешли на Дзен. Текущий URL: {self.base_page.current_url()}"
