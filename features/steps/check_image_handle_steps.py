import hashlib
import requests
from behave import *
from hamcrest import *
from config.env_setup import EnvSetup
from pageobjects import constants
from helper.photo_helper import PhotoHelper
from pageobjects.image_page import ImagePage
import urllib.request
import os


@when("the user opens an image with ID using this {url}")
def open_image_with_url(context, url):
    context.photo_id = url.split("/")[-1]
    ImagePage(context.driver).navigate(url)


@step("the user clicks on Info button")
def click_info_button(context):
    ImagePage(context.driver).navigate(constants.IMAGE_PAGE["NAVIGATE_INFO_IMAGE_PAGE"].format(
        site=EnvSetup.SITE, photo_id=context.photo_id))


@step("the user should see the image's camera model {camera_model}")
def check_image_camera_model(context, camera_model):
    actual_result = ImagePage(context.driver).get_camera_model(constants.IMAGE_PAGE["CAMERA_MODEL"])
    expected_result = camera_model
    assert_that(actual_result, expected_result, "the image's camera model must be correct.")


@step("the user should see the image's focal length {focal_length}")
def check_image_focal_length(context, focal_length):
    actual_result = ImagePage(context.driver).get_focal_length(constants.IMAGE_PAGE["FOCAL_LENGTH"])
    expected_result = focal_length
    assert_that(actual_result, expected_result, "the image's focal length must be correct.")


@then("the user should see the image's info as below")
def check_image_info(context):
    camera_model = ""
    focal_length = ""
    for row in context.table:
        camera_model = row["camera_model"]
        focal_length = row["focal_length"]

    context.execute_steps('''
            then the user should see the image's camera model {camera_model}
            then the user should see the image's focal length {focal_length}
            '''.format(camera_model=camera_model, focal_length=focal_length))


@then("the user should see all related tags of the image")
def get_related_tags(context):
    expected_result = []
    response = PhotoHelper.get_a_photo(context.photo_id)
    for tag in response.json()["tags"]:
        expected_result.append(tag["title"].title())
    actual_result = ImagePage(context.driver).get_related_tags(constants.IMAGE_PAGE["RELATED_TAGS"])
    assert_that(actual_result, equal_to(expected_result), "The related tags of image must be correct")


@when("the user downloads image")
def download_image(context):
    context.save_image_location = './resource/image.jpg'
    image = ImagePage(context.driver).download_image(constants.IMAGE_PAGE["DOWNLOADABLE_IMAGE"])
    urllib.request.urlretrieve(image, context.save_image_location)


@then("the user notices that the image is downloadable and the correct image has been saved")
def check_image_downloadable(context):
    expected_result = True
    actual_result = False
    if os.path.exists(context.save_image_location):
        actual_result = True

    assert_that(actual_result, equal_to(expected_result), "The image must be existed in system")


@step("the user downloads image using API")
def download_image_using_api(context):
    href = ImagePage(context.driver).download_image_using_href(constants.IMAGE_PAGE["DOWNLOADABLE_BUTTON"])
    context.hash_code = hashlib.md5(requests.get(href, verify=False).text.encode()).hexdigest()


@then("the user notices that the hashcode of image is the same with {expected_hashcode}")
def check_hashcode_of_image(context, expected_hashcode):
    actual_hashcode = context.hash_code
    assert_that(actual_hashcode, equal_to(expected_hashcode), "The image's hashcode must be correct.")