import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver():
    chrome_options = Options()

    headless = os.getenv("HEADLESS", "true").lower() == "true"

    if headless:
        chrome_options.add_argument("--headless")

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)

    return driver