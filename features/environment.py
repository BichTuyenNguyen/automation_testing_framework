import os
from browser.browser import Browser
from config.env_setup import EnvSetup
from helper.collection_helper import CollectionHelper


def before_all(context):
    pass


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    context = init_browser_session(context)
    context.driver.maximize_window()
    context.driver.get(EnvSetup.SITE)


def init_browser_session(context):
    context.driver = Browser.connection()
    return context


def after_scenario(context, scenario):
    if "check-add-photo-to-collection" in scenario.tags:
        CollectionHelper.delete_a_collection(context.collection_id)

    if "check-image-downloadable" in scenario.tags:
        if os.path.exists(context.save_image_location):
            os.remove(context.save_image_location)
        else:
            print("File path does not exist in system.")
    context.driver.quit()


def after_all(context):
    pass
