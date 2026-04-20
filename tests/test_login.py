from pages.login_page import LoginPage
from data.test_data import VALID_USER
from utils.logger import get_logger

def test_login(driver):
    logger = get_logger()
    logger.info("Starting login test")

    login_page = LoginPage(driver)
    login_page.open()

    logger.info("Entering credentials")
    login_page.login(VALID_USER["username"], VALID_USER["password"])

    logger.info("Verifying login")
    assert "inventory" in driver.current_url

    logger.info("Test passed")