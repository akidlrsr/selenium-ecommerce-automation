from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, by, value):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def type(self, by, value, text):
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        element.clear()
        element.send_keys(text)

    def get_text(self, by, value):
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        return element.text

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)