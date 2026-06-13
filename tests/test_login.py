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

    logger.info(
        f"Testing {test_case['username']}"
    )

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        test_case["username"],
        test_case["password"]
    )

    success = "inventory" in driver.current_url

    assert success == test_case["expected"]