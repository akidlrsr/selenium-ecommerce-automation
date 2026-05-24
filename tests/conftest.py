import pytest
from utils.driver_setup import get_driver
from datetime import datetime


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

        driver = item.funcargs["driver"]

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        screenshot_name = f"screenshots/FAILED_{item.name}_{timestamp}.png"

        driver.save_screenshot(screenshot_name)

        print(f"\nScreenshot saved: {screenshot_name}")