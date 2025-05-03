import pytest
import allure
from selenium import webdriver
from page_objects.main_page import MainPage

@allure.feature("Тесты: Вопросы о важном")
class TestQuestions:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.main_page = MainPage(cls.driver)
        cls.main_page.open()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.mark.parametrize("question_number, expected_text", [
        (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (1,
         "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (2,
         "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ])
    @allure.title("Проверка вопроса {question_number}")
    def test_question(self, question_number, expected_text):
        self.main_page.click_question(question_number)
        answer_text = self.main_page.get_answer_text(question_number)
        assert answer_text == expected_text