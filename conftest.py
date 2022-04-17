import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="None",
        help="Chose the language that you want to test in the command line"
    )


@pytest.fixture
def language(request):
    return request.config.getoption("--language")
