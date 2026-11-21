
import allure
import pytest


@allure.feature('Objects')
@allure.story('Get Objects')
@allure.title('Get all objects')
def test_get_objects(api_client, assertions):
    response = api_client.get_objects()
    assertions.assert_status_code_is(response, 200)
    assertions.assert_response_not_empty(response)


@allure.feature('Objects')
@allure.story('Get Objects')
@allure.title('Get object by')
def test_get_object_by_id(api_client, assertions, create_base_object):
    _, object_id = create_base_object
    response = api_client.get_object(object_id)
    assertions.assert_status_code_is(response, 200)
    assertions.assert_response_not_empty(response)
    assertions.assert_object_id_equal(response, object_id)


@allure.feature('Objects')
@allure.story('Post Object')
@allure.title('Post object with params: name')
@pytest.mark.parametrize("name", ["OBJECT_1", "OBJECT_2", "OBJECT_3"])
def test_post_object(name, api_client, assertions):
    response = api_client.post_object(name=name)
    assertions.assert_status_code_is(response, 200)
    assertions.assert_object_name_equal(response, name)


@allure.feature('Objects')
@allure.story('Put Object')
@allure.title('Put object by id: update object name')
def test_put_object(api_client, create_base_object, assertions, generate_test_string_value):
    _, object_id = create_base_object
    put_test_name = generate_test_string_value

    put_response = api_client.put_object(object_id, put_test_name)

    assertions.assert_status_code_is(put_response, 200)
    assertions.assert_object_id_equal(put_response, object_id)
    assertions.assert_object_name_equal(put_response, put_test_name)


@allure.feature('Objects')
@allure.story('Patch Object')
@allure.title('Patch Object by id: update object color')
def test_patch_object(api_client, create_base_object, assertions, generate_test_string_value):
    _, object_id = create_base_object
    patch_test_name = generate_test_string_value

    patch_response = api_client.patch_object(object_id, name=patch_test_name)

    assertions.assert_status_code_is(patch_response, 200)
    assertions.assert_object_id_equal(patch_response, object_id)
    assertions.assert_object_name_equal(patch_response, patch_test_name)


@allure.feature('Objects')
@allure.story('Delete Object')
@allure.title('Delete Object by id')
def test_delete_object(api_client, create_base_object, assertions):
    _, object_id = create_base_object

    delete_response = api_client.delete_object(object_id)
    assertions.assert_status_code_is(delete_response, 200)
