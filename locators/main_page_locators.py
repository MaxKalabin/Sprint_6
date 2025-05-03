from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTION_BUTTON_TEMPLATE = (By.ID, "accordion__heading-{}")
    ANSWER_TEXT_TEMPLATE = (By.ID, "accordion__panel-{}")
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")