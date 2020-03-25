from behave import *
from hamcrest import *
from config.env_setup import EnvSetup
from pageobjects import constants
from pageobjects.collection_page import CollectionPage
from pageobjects.edit_profile_page import EditProfilePage


@when("the user goes to Collection page")
def navigate_collection_page(context):
    username = context.username
    CollectionPage(context.driver).navigate(
        constants.COLLECTION_PAGE["NAVIGATE_COLLECTION_PAGE"].format(
            site=EnvSetup.SITE, username=username))


@then("the user able to see {full_name} is displayed")
def check_user_full_name(context, full_name):
    expected_result = full_name
    actual_result = EditProfilePage(context.driver).get_user_full_name(constants.EDIT_PROFILE_PAGE["USER_NAME"])
    assert_that(actual_result, equal_to(expected_result), "User's full name must be correct.")


@given("the user goes to Edit Profile page")
def navigate_edit_profile_page(context):
    EditProfilePage(context.driver).navigate(
        constants.EDIT_PROFILE_PAGE["NAVIGATE_EDIT_PROFILE_PAGE"].format(site=EnvSetup.SITE))


@when("the user enters {location} in the location input")
def edit_location(context, location):
    EditProfilePage(context.driver).edit_location(constants.EDIT_PROFILE_PAGE["USER_LOCATION"], location)


@step("the user clicks on the Update account button")
def click_update_button(context):
    EditProfilePage(context.driver).click_element(constants.EDIT_PROFILE_PAGE["UPDATE_PROFILE_BUTTON"])


@then("the user should see the updated location is {location}")
def check_user_location(context, location):
    expected_result = location
    actual_result = EditProfilePage(context.driver).get_user_location(constants.EDIT_PROFILE_PAGE["USER_LOCATION"])
    assert_that(actual_result, equal_to(expected_result), "User's location must be correct.")
