import pytest
from selenium import webdriver
from page_objects.base_page import BasePage
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def base_page(driver):
    return BasePage(driver)

@pytest.fixture(scope="function")
def main_page(driver):
    return MainPage(driver)

@pytest.fixture(scope="function")
def order_page(driver):
    return OrderPage(driver)