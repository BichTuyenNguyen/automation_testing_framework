from behave import *
from hamcrest import *
from helper.photo_helper import PhotoHelper


@when('the user get information of photo "{photo_id}"')
def send_request_get_a_photo(context, photo_id):
    context.response = PhotoHelper.get_a_photo(photo_id)


@step('the information of photo "{photo_id}" is shown as below')
def assert_correct_info(context, photo_id):
    response = context.response
    expected_result = dict()

    for row in context.table:
        expected_result = {
            "width": row["width"],
            "height": row["height"],
            "description": row["description"],
            "focal_length": row["focal_length"],
            "iso": row["iso"],
        }

    actual_result = {
        "width": str(response.json()["width"]),
        "height": str(response.json()["height"]),
        "description": str(response.json()["description"]),
        "focal_length": str(response.json()["exif"]["focal_length"]),
        "iso": str(response.json()["exif"]["iso"]),
    }

    assert_that(actual_result, equal_to(expected_result),
                "Assert that the information of photo {photo_id} is correct!".format(photo_id=photo_id))
