import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('number', ["895", "896", "897", "898", "899", "903", "904", "905", "905"])
def test_enter_the_answer(browser, number):
    link = f"https://stepik.org/lesson/236{number}/step/1/"
    browser.get(link)
    answer = math.log(int(time.time()))
    answer_input = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".textarea")))
    answer_input.send_keys(answer)

    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()

    correct_mark = WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    assert correct_mark.text == "Correct!", "The answer is not correct"

    time.sleep(3)

import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('number', ["895", "896", "897", "898", "899", "903", "904", "905", "905"])
def test_enter_the_answer(browser, number):
    link = f"https://stepik.org/lesson/236{number}/step/1/"
    browser.get(link)
    answer = math.log(int(time.time()))
    answer_input = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".textarea")))
    answer_input.send_keys(answer)

    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()

    correct_mark = WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    assert correct_mark.text == "Correct!", "The answer is not correct"

    time.sleep(3)

