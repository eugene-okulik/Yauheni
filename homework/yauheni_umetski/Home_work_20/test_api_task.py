
import allure
import pytest
import random
from helpers import get_objects, get_object_by_id, post_object, put_object, patch_object_color, delete_object


@allure.feature('Objects')
@allure.story('Get Objects')
@allure.title('Get all objects')
@pytest.mark.medium
def test_get_objects(scope_fixture, session_fixture, post_object_fixture):
    with allure.step('Get all Objects'):
        response = get_objects()
    with allure.step('Assert status code is 200'):
        assert response.status_code == 200, f"Expected 200 status code, but got: {response.status_code}"
    with allure.step('Assert responce is not empty'):
        assert response.json()["data"]


@allure.feature('Objects')
@allure.story('Get Objects')
@allure.title('Get object by')
def test_get_object_by_id(scope_fixture, session_fixture, post_object_fixture):
    post_response = post_object_fixture
    object_id = post_response.json().get("id")
    response = get_object_by_id(object_id)
    response_id = int(response.json().get("id"))
    assert response.status_code == 200, f"Expected 200 status code, but got: {response.status_code}"
    assert response.json()["data"]
    assert response_id == object_id, f"Expected id: {object_id}, but got: {response_id}"


@allure.feature('Objects')
@allure.story('Post Object')
@allure.title('Post object with params: name')
@pytest.mark.critical
@pytest.mark.parametrize("name", ["OBJECT_1", "OBJECT_2", "OBJECT_3"])
def test_post_object(name, session_fixture, scope_fixture):
    response = post_object(name)
    response_name = response.json().get("name")
    assert response.status_code == 200, f"Expected 200 status code, but got: {response.status_code}"
    assert response_name == name, f"Expected name: {name}, but got: {response_name}"


@allure.feature('Objects')
@allure.story('Put Object')
@allure.title('Put object by id: update object name')
def test_put_object(post_object_fixture, session_fixture, scope_fixture):
    put_test_name = f"API_TEST_PUT_{random.randint(1, 100)}"
    post_response = post_object_fixture
    object_id = post_response.json().get("id")

    put_response = put_object(object_id, put_test_name)
    put_response_name = put_response.json().get("name")
    put_response_id = int(put_response.json().get("id"))

    assert put_response.status_code == 200, f"Expected 200 status code, but got: {put_response.status_code}"
    assert put_response_name == put_test_name, f"Expected name: {put_test_name}, but got: {put_response_name}"
    assert put_response_id == object_id, f"Expected id: {object_id}, but got: {put_response_id}"


@allure.feature('Objects')
@allure.story('Patch Object')
@allure.title('Patch Object by id: update object color')
def test_patch_object(post_object_fixture, session_fixture, scope_fixture):
    patch_color = f"API_TEST_COLOR{random.randint(1, 100)}"
    post_response = post_object_fixture
    object_id = post_response.json().get("id")

    patch_response = patch_object_color(object_id, patch_color)
    patch_response_color = patch_response.json().get("data").get("color")
    patch_responce_id = patch_response.json().get("id")

    assert patch_response.status_code == 200, f"Expected 200 status code, but got: {patch_response.status_code}"
    assert patch_color == patch_response_color, f"Expected color: {patch_color}, but got: {patch_response_color}"
    assert patch_responce_id == object_id, f"Expected name: {object_id}, but got: {patch_responce_id}"


@allure.feature('Objects')
@allure.story('Delete Object')
@allure.title('Delete Object by id')
def test_delete_object(post_object_fixture, session_fixture, scope_fixture):
    post_response = post_object_fixture
    object_id = post_response.json().get("id")
    delete_response = delete_object(object_id)

    assert delete_response.status_code == 200, f"Expected 200 status code, but got: {delete_response.status_code}"
