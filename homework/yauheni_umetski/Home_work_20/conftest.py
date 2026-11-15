
import pytest
from helpers import post_object, delete_object


@pytest.fixture()
def post_object_fixture():
    response = post_object()
    yield response
    delete_object(response.json().get("id"))


@pytest.fixture(scope="session")
def session_fixture():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture()
def scope_fixture():
    print("\nbefore test")
    yield
    print("\nafter test")
