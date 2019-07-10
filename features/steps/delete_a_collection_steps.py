from behave import *
from helper.collection_helper import CollectionHelper


@given("the user create new collection with data below")
def create_new_collection(context):
    context.data = dict()

    for row in context.table:
        context.data = {
            "title": row["title"],
            "description": row["description"],
            "private": row["private"],
        }

    context.col_id = CollectionHelper.create_a_collection(context.data).json()["id"]


@when('the user delete the newly created collection')
def send_request_delete_a_collection(context):
    context.response = CollectionHelper.delete_a_collection(context.col_id)
