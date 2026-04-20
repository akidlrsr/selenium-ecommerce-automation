from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from data.test_data import VALID_USER

def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.open()
    login_page.login(VALID_USER["username"], VALID_USER["password"])

    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    assert cart_page.is_item_in_cart()