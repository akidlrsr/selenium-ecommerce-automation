
import os
from datetime import datetime

import pytest
import allure

from utils.driver_setup import get_driver


@pytest.fixture
def driver():
    driver = get_driver()

    try:
        yield driver
    finally:
        driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver is None:
            return

        try:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime(
                "%Y-%m-%d_%H-%M-%S"
            )

            screenshot_name = (
                f"screenshots/FAILED_{item.name}_{timestamp}.png"
            )

            screenshot_saved = driver.save_screenshot(
                screenshot_name
            )

            if screenshot_saved and os.path.isfile(screenshot_name):
                with open(screenshot_name, "rb") as image_file:
                    allure.attach(
                        image_file.read(),
                        name="Failure Screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )
            else:
                print(
                    f"Warning: Screenshot could not be saved "
                    f"for test '{item.name}'."
                )

        except Exception as exc:
            print(
                f"Warning: Could not capture or attach screenshot "
                f"for test '{item.name}': {exc}"
            )
