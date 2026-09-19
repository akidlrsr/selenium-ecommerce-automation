import pytest
import allure

from pages.login_page import LoginPage
from data.test_data import LOGIN_TEST_DATA
from utils.logger import get_logger


@allure.feature("Authentication")
@allure.story("Login Validation")
@pytest.mark.parametrize(
    "test_case",
    LOGIN_TEST_DATA,
    ids=[
        "valid_user",
        "locked_user",
        "invalid_user",
        "empty_credentials"
    ]
)
def test_login(driver, test_case):

    logger = get_logger()

    username = test_case["username"]
    password = test_case["password"]
    expected = test_case["expected"]

    allure.dynamic.title(
        f"Login Test - {username if username else 'Empty Credentials'}"
    )

    allure.dynamic.description(
        f"Verify login behavior for username: "
        f"{username if username else 'empty'}"
    )

    allure.dynamic.severity(
        allure.severity_level.CRITICAL
        if expected
        else allure.severity_level.NORMAL
    )

    allure.dynamic.parameter("username", username)
    allure.dynamic.parameter("expected", expected)

    logger.info(f"Testing login for: {username}")

    login_page = LoginPage(driver)

    with allure.step("Open SauceDemo login page"):
        login_page.open()

    with allure.step("Enter login credentials"):
        login_page.login(username, password)

    with allure.step("Verify login result"):
        success = "inventory" in driver.current_url

        assert success == expected