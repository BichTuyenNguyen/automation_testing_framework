from helper.collection_helper import CollectionHelper
from helper.photo_helper import PhotoHelper


def before_all(context):
    pass


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    # delete a collection after creating
    if "create_a_collection_with_required_field" in scenario.tags:
        CollectionHelper.delete_a_collection(context.response.json()["id"])

    # unlike photo after like
    if "like_a_photo_with_specific_id" in scenario.tags:
        PhotoHelper.unlike_a_photo(context.like_photo_id)


def after_all(context):
    pass
