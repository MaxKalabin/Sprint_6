from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_DROPDOWN = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION_TEMPLATE = (By.XPATH, "//div[@class='select-search__select']//button[{}]")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_PICKER_TODAY = (By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-control']")
    RENTAL_PERIOD_OPTION_TEMPLATE = (By.XPATH, "//div[@class='Dropdown-menu']/div[{}]")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    CONFIRMATION_POPUP = (By.XPATH, "//div[text()='Хотите оформить заказ?']")
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    MODAL_CHECK_STATUS = (By.XPATH, "//div[text()='Заказ оформлен')]")
    CHECK_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")


