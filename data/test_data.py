
VALID_USER = {
    "username": "standard_user",
    "password": "secret_sauce"
}

LOGIN_TEST_DATA = [
    {
        "username": "standard_user",
        "password": "secret_sauce",
        "expected": True,
        "expected_error": None
    },
    {
        "username": "locked_out_user",
        "password": "secret_sauce",
        "expected": False,
        "expected_error": (
            "Epic sadface: Sorry, this user has been locked out."
        )
    },
    {
        "username": "invalid_user",
        "password": "wrong_password",
        "expected": False,
        "expected_error": (
            "Epic sadface: Username and password do not match any user in this service"
        )
    },
    {
        "username": "",
        "password": "",
        "expected": False,
        "expected_error": "Epic sadface: Username is required"
    }
]
