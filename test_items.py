import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_languages(browser, language):
    list_of_languages = []  # for collect the list of languages existing for this website
    internet_shop = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    browser.get(internet_shop)
    languages = browser.find_elements(By.CSS_SELECTOR, "option[value]")
    for i in range(1, len(languages) + 1):
        element = browser.find_element(By.XPATH, f"//option[{i}]")
        language_value = element.get_attribute("value")
        list_of_languages.append(language_value)

    if language in list_of_languages:  # for testing interface language
        link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
        browser.get(link)
        add_button = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#add_to_basket_form button")))
        assert len(add_button) == 1, "The selector mush be unique!"
        time.sleep(10)  # time needed for visual checking the name of the button
    else:
        raise AssertionError("The command must be correct")
