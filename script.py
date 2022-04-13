from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "span[id=input_value]")
    x = int(x_element.text)
    y = calc(x)
    result = browser.find_element(By.CSS_SELECTOR, "input[id=answer]")
    result.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "input[type=checkbox]")
    checkbox.click()

    radio_elem = browser.find_element(By.CSS_SELECTOR, "input[id=robotsRule]")

    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_elem)
    radio_elem.click()

    # radio = browser.find_element(By.CSS_SELECTOR, "input[id=robotsRule]")
    # radio.click()
    submit = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
