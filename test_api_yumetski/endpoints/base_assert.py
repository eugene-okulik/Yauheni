import allure
from requests import Response


class BaseAssert:

    @staticmethod
    @allure.step("Assert status code is {expected_status_code}")
    def assert_status_code_is(response: Response, expected_status_code: int) -> None:
        assert response.status_code == expected_status_code, (
            f"Expected status code {expected_status_code}, but got status code {response.status_code}"
        )

    @staticmethod
    @allure.step("Assert response is not empty")
    def assert_response_not_empty(response: Response) -> None:
        assert response.json(), (
            f"Expected not empty response, but got {response.json()}"
        )

    @staticmethod
    @allure.step("Assert response object id is equal to created object id: {expected_object_id}")
    def assert_object_id_equal(response: Response, expected_object_id: int):
        response_id = response.json().get("id")
        assert int(response_id) == expected_object_id, (
            f"Expected object id {expected_object_id}, but got object id {response_id}"
        )

    @staticmethod
    @allure.step("Assert response object name is equal to created object name: {expected_object_name}")
    def assert_object_name_equal(response: Response, expected_object_name: str):
        response_name = response.json().get("name")
        assert response_name == expected_object_name, (
            f"Expected object name {expected_object_name}, but got object name {response_name}"
        )
