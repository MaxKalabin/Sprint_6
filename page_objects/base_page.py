from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from test_data import URL


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = BasePageLocators()

    def open(self):
        self.teardown_method()
        self.driver.get(URL)

    def click_scooter_logo(self):
        scooter_logo = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.locators.SCOOTER_LOGO)
        )
        scooter_logo.click()

    def click_yandex_logo(self):
        yandex_logo = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.locators.YANDEX_LOGO)
        )
        yandex_logo.click()

    def wait_for_url(self, expected_url, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(expected_url)
        )

    def teardown_method(self):
        if len(self.driver.window_handles) > 1:
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])