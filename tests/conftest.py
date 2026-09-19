import os
from datetime import datetime

import pytest
import allure

from utils.driver_setup import get_driver


@pytest.fixture
def driver():
    driver = get_driver()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver is None:
            return

        # Make sure the screenshots directory exists
        os.makedirs("screenshots", exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        screenshot_name = (
            f"screenshots/FAILED_{item.name}_{timestamp}.png"
        )

        # Save screenshot to disk
        driver.save_screenshot(screenshot_name)

        # Attach screenshot to Allure report
        with open(screenshot_name, "rb") as image_file:
            allure.attach(
                image_file.read(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )