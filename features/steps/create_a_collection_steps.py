from behave import *
from hamcrest import *
from helper.collection_helper import CollectionHelper


@when('the user send a post request to create a collection with below params')
def send_request_create_a_collection(context):
    context.expected_result_create_collection = dict()

    for row in context.table:
        context.expected_result_create_collection = {
            "title": str(row["title"]),
            "description": str(row["description"]),
            "private": str(row["private"]),
        }

    context.response = CollectionHelper.create_a_collection(context.expected_result_create_collection)


@step('the information of new created collection is the same as input data')
def assert_correct_col_info(context):
    response = context.response
    expected_result = context.expected_result_create_collection

    actual_result = {
        'title': str(response.json()["title"]),
        'description': str(response.json()["description"]),
        'private': str(response.json()["private"])
    }

    assert_that(actual_result, equal_to(expected_result),
                "Assert that the information of collection is correct!")
