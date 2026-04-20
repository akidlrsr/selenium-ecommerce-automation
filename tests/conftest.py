import pytest
from utils.driver_setup import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        driver = item.funcargs.get("driver")
        if driver:
            driver.save_screenshot("failure.png")