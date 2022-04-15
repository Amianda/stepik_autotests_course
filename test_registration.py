from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link_1 = "http://suninjuly.github.io/registration1.html"
link_2 = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()  # поменять, если не используется chromedriver!
    browser.get(link_2)

    browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Lilia')
    browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Vas')
    browser.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys('vas@google.com')

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    time.sleep(5)
    browser.quit()