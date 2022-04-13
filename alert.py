from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = " http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.CSS_SELECTOR, "span[id=input_value]")
    x = int(x_element.text)
    y = calc(x)
    result = browser.find_element(By.CSS_SELECTOR, "input[id=answer]")
    result.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    submit.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
