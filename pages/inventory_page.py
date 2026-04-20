from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):

    def add_first_item_to_cart(self):
        self.click(By.CLASS_NAME, "btn_inventory")

    def go_to_cart(self):
        self.click(By.CLASS_NAME, "shopping_cart_link")