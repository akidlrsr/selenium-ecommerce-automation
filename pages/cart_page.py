from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def is_item_in_cart(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return len(items) > 0

    def remove_item(self):
        self.driver.find_element(By.CLASS_NAME, "cart_button").click()