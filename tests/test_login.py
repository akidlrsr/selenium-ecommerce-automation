
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
    expected_error = test_case["expected_error"]

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
        if expected:
            assert login_page.is_login_successful(), (
                "Expected the inventory page to be displayed after login."
            )
            assert not login_page.is_error_message_displayed(), (
                "An error message appeared after a successful login."
            )
        else:
            assert login_page.is_error_message_displayed(), (
                "Expected a login error message, but none was displayed."
            )

            actual_error = login_page.get_error_message()

            assert actual_error == expected_error, (
                f"Expected error: '{expected_error}', "
                f"but received: '{actual_error}'"
            )
