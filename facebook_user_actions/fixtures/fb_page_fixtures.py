import random
import string
import pytest


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@pytest.fixture(scope="session")
def page_data():
    return {
        "page_name": randomword(9),
        "page_desc": "Community",
        "page_post": "This is the first post"
    }