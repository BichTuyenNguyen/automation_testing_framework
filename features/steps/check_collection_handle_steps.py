from behave import *
from hamcrest import *
from config.env_setup import EnvSetup
import pageobjects.constants
from helper.collection_helper import CollectionHelper
from pageobjects.collection_page import CollectionPage


@step("the user creates a new collection using API with below params")
def create_collection(context):
    data_create_collection = dict()

    for row in context.table:
        data_create_collection = {
            "title": row["title"],
            "description": row["description"],
            "private": row["private"],
        }

    response = CollectionHelper.create_a_collection(data_create_collection)

    actual_result = {
        "title": str(response.json()["title"]),
        "description": str(response.json()["description"]),
        "private": str(response.json()["private"]),
    }

    context.collection_id = str(response.json()["id"])
    assert_that(actual_result,
                equal_to(data_create_collection),
                "The information of create data must be correct")


@step("the user add a photo with {photo_id} into the added collection using API")
def add_photo_to_collection(context, photo_id):
    data_add_photo_to_collection = {
        "collection_id": str(context.collection_id),
        "photo_id": photo_id
    }

    response = CollectionHelper.add_photo_to_collection(context.collection_id, data_add_photo_to_collection)
    context.photo_id = response.json()["photo"]["id"]
    actual_result = {
        "collection_id": str(response.json()["collection"]["id"]),
        "photo_id": context.photo_id
    }
    assert_that(actual_result,
                equal_to(data_add_photo_to_collection),
                "The photo id and collection id must be correct")


@when("the user clicks on the added photo to the collection")
def click_added_photo(context):
    url = pageobjects.constants.COLLECTION_PAGE["PHOTO_URL"].format(
        site=EnvSetup.SITE, collection_id=context.collection_id)
    CollectionPage(context.driver).navigate(url)
    CollectionPage(context.driver).select_photo(pageobjects.constants.COLLECTION_PAGE["EXIST_PHOTOS"])


@then("the user notices that the ID of photo in URL is correct")
def check_photo_id(context):
    expected_result = context.photo_id
    actual_result = CollectionPage(context.driver).get_current_url().split("/")[-1]
    assert_that(actual_result, equal_to(expected_result), "Photo is must be matched with URL")
