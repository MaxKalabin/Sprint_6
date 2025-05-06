import allure
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    @allure.step('Заполнение первой страницы формы заказа')
    def fill_order_form(self, name, surname, address, metro_station, phone):
        self.fill_input("Имя", self.locators.NAME_FIELD, name)
        self.fill_input("Фамилия", self.locators.SURNAME_FIELD, surname)
        self.fill_input("Адрес", self.locators.ADDRESS_FIELD, address)

        with allure.step('Выбор метро {metro_station} в дропдауне'):
            self.click_element(self.locators.METRO_DROPDOWN)
            self.click_element(self._get_metro_option_locator(metro_station))

        self.fill_input("Телефон", self.locators.PHONE_FIELD, phone)

        with allure.step('Клик по кнопке далее на первой странице формы'):
            self.click_element(self.locators.NEXT_BUTTON)

    @allure.step('Заполнение второй страницы формы заказа')
    def fill_rental_details(self, rental_period, color, comment):
        with allure.step('Выбор даты доставки в дропдауне'):
            self.click_element(self.locators.DATE_FIELD)
            self.click_element(self.locators.DATE_PICKER_TODAY)

        with allure.step('Выбор срока аренды = {rental_period} в дропдауне'):
            self.click_element(self.locators.RENTAL_PERIOD_DROPDOWN)
            self.click_element(self._get_rental_period_locator(rental_period))

        with allure.step('Выбор цвета самоката = {color} в дропдауне'):
            self.click_element((By.ID, color))

        self.fill_input("Коммент", self.locators.COMMENT_FIELD, comment)

    @allure.step('Клик на кнопке Заказать в конце формы заказа')
    def click_order_button(self):
        self.click_element(self.locators.ORDER_BUTTON)

    @allure.step('Клик на кнопке Да для подтверждения заказа')
    def click_confirmation_button(self):
        self.click_element(self.locators.CONFIRM_YES_BUTTON)

    @allure.step('Клик на кнопке Посмотреть статус после подтверждения заказа')
    def click_check_status_button(self):
        self.click_element(self.locators.CHECK_STATUS_BUTTON)

    @allure.step("Проверка открытия второй страницы заказа")
    def is_second_page_opened(self):
        return self.is_element_visible(self.locators.DATE_FIELD)

    @allure.step("Проверка открытия окна подтверждения заказа")
    def is_confirmation_popup_opened(self):
        return self.is_element_visible(self.locators.CONFIRMATION_POPUP)

    @allure.step("Проверка открытия страницы статуса заказа")
    def is_status_page_opened(self):
        return self.is_element_visible(self.locators.CHECK_STATUS_BUTTON)

    def _get_metro_option_locator(self, station_name):
        return ("xpath", f"//div[text()='{station_name}']")

    def _get_rental_period_locator(self, period_name):
        return ("xpath", f"//div[text()='{period_name}']")