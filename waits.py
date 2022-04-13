from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5[id=price]"), "$100"))
    button = browser.find_element(By.CSS_SELECTOR, "button[id=book]")
    button.click()

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