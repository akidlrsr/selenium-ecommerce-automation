
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    LOGIN_URL = "https://www.saucedemo.com/"

    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def open(self):
        self.driver.get(self.LOGIN_URL)

    def login(self, username, password):
        self.type(*self.USERNAME_FIELD, username)
        self.type(*self.PASSWORD_FIELD, password)
        self.click(*self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)

    def is_error_message_displayed(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return True
        except Exception:
            return False

    def is_login_successful(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.INVENTORY_CONTAINER)
        ).is_displayed()
