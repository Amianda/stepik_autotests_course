from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element(By.CSS_SELECTOR, "input[name=firstname]")
    input_name.send_keys("Ivan")
    input_lastname = browser.find_element(By.CSS_SELECTOR, "input[name=lastname]")
    input_lastname.send_keys("Petrov")

    input_email = browser.find_element(By.CSS_SELECTOR, "input[name=email]")
    input_email.send_keys("lil888@mail.ru")

    input_file = browser.find_element(By.CSS_SELECTOR, "input[type=file]")
    input_file.send_keys("/Users/liliavasileva/Desktop/text_file.txt")
    # current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    # file_path = os.path.join(current_dir, 'text_file.txt')  # добавляем к этому пути имя файла
    # input_file.send_keys(file_path)

    # input3 = browser.find_element(By.CSS_SELECTOR, "input[class='form-control city']")
    # input3.send_keys("Smolensk")
    # input4 = browser.find_element(By.ID, "country")
    # input4.send_keys("Russia")

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

