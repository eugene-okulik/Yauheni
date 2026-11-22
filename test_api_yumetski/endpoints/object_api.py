from test_api_yumetski.endpoints.base_api import BaseAPI
import random
import allure
from requests import Response


class Object:
    def __init__(self) -> None:
        base_url = "http://objapi.course.qa-practice.com"
        self.endpoint = "object"
        self.api = BaseAPI(base_url=base_url)

    def _build_body(
            self,
            name: str | None = None,
            color: str | None = None,
            size: str | None = None
    ) -> dict:
        if name is None:
            name = f"API_NAME_{random.randint(1, 100)}"
        if color is None:
            color = f"API_COLOR_{random.randint(1, 100)}"
        if size is None:
            size = f"API_SIZE_{random.randint(1, 100)}"
        body: dict = {
            "data": {
                "color": color,
                "size": size
            },
            "name": name
        }
        return body

    @allure.step("Create a new object")
    def post_object(
            self,
            name: str | None = None,
            color: str | None = None,
            size: str | None = None
    ) -> Response:
        body: dict = self._build_body(name=name, color=color, size=size)
        return self.api.post(self.endpoint, json=body)

    @allure.step("Put object by id: {id_}")
    def put_object(
            self,
            id_: int,
            name: str | None = None,
            color: str | None = None,
            size: str | None = None
    ) -> Response:
        body: dict = self._build_body(name=name, color=color, size=size)
        return self.api.put(f"{self.endpoint}/{id_}", json=body)

    @allure.step("Patch object by id: {id_}")
    def patch_object(
            self,
            id_: int,
            name: str | None = None,
            color: str | None = None,
            size: str | None = None
    ) -> Response:

        body = {}
        if name is not None:
            body["name"] = name
        if color is not None or size is not None:
            body["data"] = {}
            if color is not None:
                body["data"]["color"] = color
            if size is not None:
                body["data"]["size"] = size

        return self.api.patch(f"{self.endpoint}/{id_}", json=body)

    @allure.step("Delete object by id: {id_}")
    def delete_object(self, id_: int) -> Response:
        return self.api.delete(f"{self.endpoint}/{id_}")

    @allure.step("Get objects")
    def get_objects(self) -> Response:
        return self.api.get(self.endpoint)

    @allure.step("Get a object by id: {id_}")
    def get_object(self, id_: int) -> Response:
        return self.api.get(f"{self.endpoint}/{id_}")

    @staticmethod
    @allure.step("Get object {key} value from response")
    def get_object_value_from_response(response: Response, key: str):
        return response.json().get(key)
