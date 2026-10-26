
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):

    def get_item_names(self):
        items = self.wait_for_elements(
            By.CLASS_NAME,
            "inventory_item_name"
        )

        return [item.text for item in items]

    def is_item_in_cart(self):
        return len(self.get_item_names()) > 0

    def remove_item(self):
        self.click(
            By.CLASS_NAME,
            "cart_button"
        )
