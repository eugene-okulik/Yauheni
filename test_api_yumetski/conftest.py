import pytest
import allure
import random
from collections.abc import Generator
from requests import Response
from test_api_yumetski.endpoints.object_api import Object
from test_api_yumetski.endpoints.base_assert import BaseAssert


@pytest.fixture()
def api_client() -> Object:
    return Object()


@pytest.fixture()
def create_base_object(api_client) -> Generator[tuple[Response, int | None], None, None]:
    with allure.step("Create a new base object"):
        response = api_client.post_object()

        object_id = response.json().get("id")

    yield response, object_id

    if object_id:
        with allure.step(f"Delete base object {object_id}"):
            api_client.delete_object(object_id)


@pytest.fixture()
def assertions() -> BaseAssert:
    return BaseAssert()


@pytest.fixture()
@allure.step("Generate test value for string data type value")
def generate_test_string_value() -> str:
    return f"API_TEST_STR_{random.randint(1, 100)}"
