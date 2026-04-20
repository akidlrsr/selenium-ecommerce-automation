from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.type(By.ID, "user-name", username)
        self.type(By.ID, "password", password)
        self.click(By.ID, "login-button")