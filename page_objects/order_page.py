from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = OrderPageLocators()

    def fill_order_form(self, name, surname, address, metro_station, phone):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators.NAME_FIELD)).send_keys(name)
        self.driver.find_element(*self.locators.SURNAME_FIELD).send_keys(surname)
        self.driver.find_element(*self.locators.ADDRESS_FIELD).send_keys(address)

        self.driver.find_element(*self.locators.METRO_DROPDOWN).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{metro_station}']"))).click()

        self.driver.find_element(*self.locators.PHONE_FIELD).send_keys(phone)

        self.driver.find_element(*self.locators.NEXT_BUTTON).click()

    def fill_rental_details(self, rental_period, color, comment):
        self.driver.find_element(*self.locators.DATE_FIELD).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.locators.DATE_PICKER_TODAY)).click()

        self.driver.find_element(*self.locators.RENTAL_PERIOD_DROPDOWN).click()

        self.driver.find_element(By.XPATH, f"//div[text()='{rental_period}']").click()
        self.driver.find_element(By.ID, color).click()

        self.driver.find_element(*self.locators.COMMENT_FIELD).send_keys(comment)

    def click_order_button(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.locators.ORDER_BUTTON)).click()

    def click_confirmation_button(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.locators.CONFIRM_YES_BUTTON)).click()

    def click_check_status_button(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.locators.CHECK_STATUS_BUTTON)).click()