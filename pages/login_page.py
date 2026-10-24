
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.type(By.ID, "user-name", username)
        self.type(By.ID, "password", password)
        self.click(By.ID, "login-button")

    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)

    def is_error_message_displayed(self):
        elements = self.driver.find_elements(*self.ERROR_MESSAGE)
        return any(element.is_displayed() for element in elements)

    def is_login_successful(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.INVENTORY_CONTAINER)
        ).is_displayed()
