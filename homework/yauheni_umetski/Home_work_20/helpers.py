
import pytest
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
