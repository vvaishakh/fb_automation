import pytest


@pytest.fixture
def invalid_login_data():
    return {
        "username": "invalid",
        "password": "invalid"}
