import pytest
import allure
from test_data import *

@allure.feature('Тесты: Заказ самоката')
class TestOrder:


    @allure.title("Процесс заказа самоката через {button_type} кнопку")
    @pytest.mark.parametrize("order_data, button_type", [
        (ORDER_DATA[0], "top"),
        (ORDER_DATA[1], "bottom")
    ])
    def test_order_via_button(self, base_page, main_page, order_page, order_data, button_type):
        with allure.step("Открытие главной страницы"):
            base_page.open(URL)

        with allure.step(f"Клик по кнопке Заказать ({button_type})"):
            main_page.click_order_button(button_type)

        with allure.step("Заполнение первой страницы формы заказа"):
            order_page.fill_order_form(
                order_data["name"],
                order_data["surname"],
                order_data["address"],
                order_data["metro_station"],
                order_data["phone"]
            )
            assert order_page.is_second_page_opened(), "Не перешли на вторую страницу"

        with allure.step("Заполнение второй страницы формы заказа"):
            order_page.fill_rental_details(
                order_data["rental_period"],
                order_data["color"],
                order_data["comment"]
            )

        with allure.step("Подтверждение заказа"):
            order_page.click_order_button()
            assert order_page.is_confirmation_popup_opened(), "Окно подтверждения не появилось"
            order_page.click_confirmation_button()
            assert order_page.is_status_page_opened(), "Не перешли на страницу статуса заказа"
            order_page.click_check_status_button()

        with allure.step("Переход на главную через лого Самокат"):
            base_page.click_scooter_logo()
            base_page.wait_for_url(URL)
            assert base_page.current_url() == URL, f"Ожидался URL '{URL}', но получен '{base_page.current_url()}'"

        with allure.step("Переход на Дзен через лого Яндекса"):
            base_page.click_yandex_logo()
            base_page.switching_tabs(1)
            base_page.wait_for_url(DZEN_URL)
            assert DZEN_URL in base_page.current_url(), f"Не перешли на Дзен. Текущий URL: {base_page.current_url()}"
