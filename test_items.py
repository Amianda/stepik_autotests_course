import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_get_countries_list(browser):
    list_of_languages = []
    internet_shop = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    browser.get(internet_shop)
    languages = browser.find_elements(By.CSS_SELECTOR, "option[value]")
    for i in range(1, len(languages) + 1):
        element = browser.find_element(By.XPATH, f"//option[{i}]")
        language_value = element.get_attribute("value")
        list_of_languages.append(language_value)
    return list_of_languages


@pytest.mark.parametrize('language', test_get_countries_list)
def test_languages(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    add_button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#add_to_basket_form button")))
    checking_element = browser.find_element(By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    assert checking_element.text == "Coders at Work"
