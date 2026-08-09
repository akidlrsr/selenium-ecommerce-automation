import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from data.test_data import VALID_USER


@allure.feature("Shopping Cart")
@allure.story("Add Product to Cart")
@allure.severity(allure.severity_level.NORMAL)
def test_add_to_cart(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    with allure.step("Open SauceDemo login page"):
        login_page.open()

    with allure.step("Login with valid user"):
        login_page.login(
            VALID_USER["username"],
            VALID_USER["password"]
        )

    with allure.step("Add first product to cart"):
        inventory_page.add_first_item_to_cart()

    with allure.step("Navigate to shopping cart"):
        inventory_page.go_to_cart()

    with allure.step("Verify product is in cart"):
        assert cart_page.is_item_in_cart()