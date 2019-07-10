from helper import constants
from helper.request_helper import RequestHelper


class CollectionHelper:
    @staticmethod
    def get_a_collection(collection_id):
        endpoint = constants.GET_COLLECTION_ENDPOINT.format(collection_id=str(collection_id))
        response = RequestHelper.send_get_request(endpoint)
        return response

    @staticmethod
    def get_a_collection_response(collection_id):
        endpoint = constants.GET_COLLECTION_ENDPOINT.format(collection_id=str(collection_id))
        response = RequestHelper.send_get_request(endpoint)
        return response

    @staticmethod
    def create_a_collection(data):
        endpoint = constants.CREATE_COLLECTION_ENDPOINT
        response = RequestHelper.send_post_request_with_data(endpoint, data)
        return response

    @staticmethod
    def delete_a_collection(collection_id):
        endpoint = constants.DELETE_COLLECTION_ENDPOINT.format(collection_id=collection_id)
        response = RequestHelper.send_delete_request(endpoint)
        return response
