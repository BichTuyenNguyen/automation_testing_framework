from behave import *
from hamcrest import *
from helper.photo_helper import PhotoHelper


@when('the user like a photo "{photo_id}"')
def send_request_like_a_photo(context, photo_id):
    context.response = PhotoHelper.like_a_photo(photo_id)


@step('the Likes field of photo "{photo_id}" is increased!')
def assert_likes_increase(context, photo_id):
    previous_likes = PhotoHelper.unlike_a_photo(photo_id).json()["photo"]["likes"]
    current_likes = context.response.json()["photo"]["likes"]

    assert_that(current_likes, greater_than(previous_likes),
                "Assert that the Likes field is increased!")
