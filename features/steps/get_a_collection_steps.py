from behave import *
from hamcrest import *
from helper.collection_helper import CollectionHelper


@when('the user get information of collection "{col_id}"')
def send_request_get_a_collection(context, col_id):
    context.response = CollectionHelper.get_a_collection_response(col_id)


@step('the information of collection "{col_id}" is shown as below')
def assert_correct_col_info(context, col_id):
    response = context.response
    expected_result = dict()

    for row in context.table:
        expected_result = {
            "title": row["title"],
            "total_photos": row["total_photos"],
            "description": row["description"],
            "published_at": row["published_at"],
            "updated_at": row["updated_at"],
        }

    actual_result = {
        "title": str(response.json()["title"]),
        "total_photos": str(response.json()["total_photos"]),
        "description": str(response.json()["description"]),
        "published_at": str(response.json()["published_at"]),
        "updated_at": str(response.json()["updated_at"])
    }

    assert_that(actual_result, equal_to(expected_result),
                "Assert information is correct!")
