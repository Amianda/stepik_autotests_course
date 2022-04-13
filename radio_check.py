from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "img[id=treasure]")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    result = browser.find_element(By.CSS_SELECTOR, "input[id=answer]")
    result.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "input[type=checkbox]")
    checkbox.click()
    radio = browser.find_element(By.CSS_SELECTOR, "input[id=robotsRule]")
    radio.click()
    submit = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
