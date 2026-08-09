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

    allure.dynamic.title(
        f"Login Test - {test_case['username']}"
    )

    allure.dynamic.description(
        "Validates login behavior using different authentication scenarios."
    )

    allure.dynamic.severity(allure.severity_level.CRITICAL)

    allure.dynamic.parameter(
        "username",
        test_case["username"]
    )

    allure.dynamic.parameter(
        "expected",
        test_case["expected"]
    )

    login_page = LoginPage(driver)

    with allure.step("Open SauceDemo login page"):
        logger.info("Opening login page")
        login_page.open()

    with allure.step("Enter login credentials"):
        logger.info(
            f"Testing {test_case['username']}"
        )

        login_page.login(
            test_case["username"],
            test_case["password"]
        )

    with allure.step("Verify login result"):
        success = "inventory" in driver.current_url

        logger.info(
            f"Expected result: {test_case['expected']}"
        )

        logger.info(
            f"Actual login success: {success}"
        )

        assert success == test_case["expected"]