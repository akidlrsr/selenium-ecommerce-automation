# Selenium E-Commerce Automation Framework

## Overview

This project is a Selenium automation framework built using Python and PyTest for testing core e-commerce workflows on the SauceDemo website.

The framework follows the Page Object Model design pattern to improve maintainability, readability, and scalability of automated test scripts.

## Features

* Automated login testing
* Add to cart functionality testing
* Page Object Model structure
* PyTest framework integration
* Explicit waits for stable execution
* HTML test reporting
* Logging support
* Screenshot capture on test failure
* Reusable browser setup using fixtures

## Tech Stack

* Python
* Selenium WebDriver
* PyTest
* PyTest HTML Reports
* Git
* GitHub

## Project Structure

```text
selenium-ecommerce-project/
│
├── data/
│   └── test_data.py
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   └── test_cart.py
│
├── utils/
│   ├── driver_setup.py
│   └── logger.py
│
├── report.html
├── requirements.txt
└── README.md
```

## Test Scenarios

### Login Test

* Opens SauceDemo website
* Enters valid credentials
* Verifies successful login

### Cart Test

* Logs into application
* Adds product to cart
* Navigates to cart page
* Verifies item exists in cart

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/selenium-ecommerce-automation.git
```

Navigate to the project folder:

```bash
cd selenium-ecommerce-project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:

```bash
pytest -v
```

Run tests with HTML report:

```bash
pytest --html=report.html --self-contained-html
```

## Reporting

The framework generates an HTML execution report after test execution.

Example report file:

```text
report.html
```

## Future Improvements

* CI/CD integration using GitHub Actions
* Parallel test execution
* Cross-browser testing
* API automation integration
* Docker support

## Author

Created by Aireen Kate as part of a QA Automation portfolio project.
