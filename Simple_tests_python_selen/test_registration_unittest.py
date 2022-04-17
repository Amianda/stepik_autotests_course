from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


def link_t(link):
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Kesa')
    browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Lisa')
    browser.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys('KL@google.com')

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(1)
    return browser.find_element(By.TAG_NAME, "h1").text


class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")

    def test_reg2(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")


if __name__ == "__main__":
    unittest.main()
    print("All tests passed!")

