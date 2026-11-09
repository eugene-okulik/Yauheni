import random

import requests

BASE_URL: str = "http://objapi.course.qa-practice.com/object"
BASE_HEADERS = {"Content-Type": "application/json"}


def get_objects():
    response = requests.get(BASE_URL, headers=BASE_HEADERS)
    return response


def get_object_by_id(id_: int):
    response = requests.get(f"{BASE_URL}/{id_}", headers=BASE_HEADERS)
    return response


def post_object(name: str | None = None):
    if name is None:
        name = f"API_TEST_{random.randint(1, 100)}"
    body = {
        "data": {
            "color": "white",
            "size": "big"
        },
        "name": name
    }
    response = requests.post(
        BASE_URL,
        json=body,
        headers=BASE_HEADERS
    )
    return response


def put_object(id_: int, name: str):
    body = {
        "data": {
            "color": "white",
            "size": "big"
        },
        "name": name
    }
    response = requests.put(
        f"{BASE_URL}/{id_}",
        json=body,
        headers=BASE_HEADERS
    )
    return response


def patch_object_color(id_: int, color: str):
    body = {
        "data": {
            "color": color,
        }
    }
    response = requests.patch(
        f"{BASE_URL}/{id_}",
        json=body,
        headers=BASE_HEADERS
    )
    return response


def delete_object(id_: int):
    response = requests.delete(f"{BASE_URL}/{id_}", headers=BASE_HEADERS)
    return response


def test_get_objects():
    post_object()
    response = get_objects()
    assert response.status_code == 200, f"Expected 200 status code, but got: {response.status_code}"
    assert response.json()["data"]


def test_post_object():
    test_name = f"API_TEST_{random.randint(1, 100)}"
    response = post_object(test_name)
    response_name = response.json().get("name")
    assert response.status_code == 200, f"Expected 200 status code, but got: {response.status_code}"
    assert response_name == test_name, f"Expected name: {test_name}, but got: {response_name}"


def test_put_object():
    put_test_name = f"API_TEST_PUT_{random.randint(1, 100)}"
    post_response = post_object()
    object_id = post_response.json().get("id")

    put_response = put_object(object_id, put_test_name)
    put_response_name = put_response.json().get("name")
    put_response_id = int(put_response.json().get("id"))

    assert put_response.status_code == 200, f"Expected 200 status code, but got: {put_response.status_code}"
    assert put_response_name == put_test_name, f"Expected name: {put_test_name}, but got: {put_response_name}"
    assert put_response_id == object_id, f"Expected id: {object_id}, but got: {put_response_id}"


def test_patch_object():
    patch_color = f"API_TEST_COLOR{random.randint(1, 100)}"
    post_response = post_object()
    object_id = post_response.json().get("id")

    patch_response = patch_object_color(object_id, patch_color)
    patch_response_color = patch_response.json().get("data").get("color")
    patch_responce_id = patch_response.json().get("id")

    assert patch_response.status_code == 200, f"Expected 200 status code, but got: {patch_response.status_code}"
    assert patch_color == patch_response_color, f"Expected color: {patch_color}, but got: {patch_response_color}"
    assert patch_responce_id == object_id, f"Expected name: {object_id}, but got: {patch_responce_id}"


def test_delete_object():
    post_response = post_object()
    object_id = post_response.json().get("id")
    delete_response = delete_object(object_id)

    assert delete_response.status_code == 200, f"Expected 200 status code, but got: {delete_response.status_code}"


test_delete_object()
test_put_object()
test_patch_object()
test_get_objects()
test_post_object()
