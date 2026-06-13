VALID_USER = {
    "username": "standard_user",
    "password": "secret_sauce"
}

LOGIN_TEST_DATA = [
    {
        "username": "standard_user",
        "password": "secret_sauce",
        "expected": True
    },
    {
        "username": "locked_out_user",
        "password": "secret_sauce",
        "expected": False
    },
    {
        "username": "invalid_user",
        "password": "wrong_password",
        "expected": False
    },
    {
        "username": "",
        "password": "",
        "expected": False
    }
]