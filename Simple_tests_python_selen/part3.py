from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    num_1 = browser.find_element(By.CSS_SELECTOR, "span[id=num1]")
    num_1_needed = int(num_1.text)
    num_2 = browser.find_element(By.CSS_SELECTOR, "span[id=num2]")
    num_2_needed = int(num_2.text)
    result = str(num_1_needed + num_2_needed)
    my_select = Select(browser.find_element(By.TAG_NAME, "select"))
    my_select.select_by_value(result)
    button = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

