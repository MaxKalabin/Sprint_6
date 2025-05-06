import allure
from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step ("Клик на вопрос в футтере")
    def click_question(self, question_number):
        question_locator = (
            self.locators.QUESTION_BUTTON_TEMPLATE[0],
            self.locators.QUESTION_BUTTON_TEMPLATE[1].format(question_number)
        )
        element = self.wait_for_element_to_be_clickable(question_locator)
        self.scroll_into_view(element)
        self.click_element(question_locator)

    @allure.step ("Получение текста ответа")
    def get_answer_text(self, question_number):
        answer_locator = (
            self.locators.ANSWER_TEXT_TEMPLATE[0],
            self.locators.ANSWER_TEXT_TEMPLATE[1].format(question_number)
        )
        return self.get_element_text(answer_locator)

    @allure.step ("Начать заказ через {button_type} кнопку")
    def click_order_button(self, button_type):
        if button_type == "top":
            order_button_locator = self.locators.ORDER_BUTTON_TOP
        else:
            order_button_locator = self.locators.ORDER_BUTTON_BOTTOM

        self.click_element(order_button_locator)
