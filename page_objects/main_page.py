from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = MainPageLocators()

    def click_question(self, question_number):
        question_locator = (
            self.locators.QUESTION_BUTTON_TEMPLATE[0],
            self.locators.QUESTION_BUTTON_TEMPLATE[1].format(question_number)
        )
        element = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(question_locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def get_answer_text(self, question_number):
        answer_locator = (
            self.locators.ANSWER_TEXT_TEMPLATE[0],
            self.locators.ANSWER_TEXT_TEMPLATE[1].format(question_number)
        )
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(answer_locator)
        ).text

    def click_order_button(self, button_locator):
        element = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(button_locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

