import requests
from config.env_setup import EnvSetUp


class RequestHelper:

    @staticmethod
    def send_get_request(end_point):
        url = EnvSetUp.API + end_point
        response = requests.get(url, headers={'Authorization': 'Bearer ' + EnvSetUp.TOKEN}, verify=False)
        return response

    @staticmethod
    def send_post_request(end_point):
        url = EnvSetUp.API + end_point
        response = requests.post(url, headers={'Authorization': 'Bearer ' + EnvSetUp.TOKEN}, verify=False)
        return response

    @staticmethod
    def send_post_request_with_data(end_point, data):
        url = EnvSetUp.API + end_point
        response = requests.post(url,
                                 headers={'Authorization': 'Bearer ' + EnvSetUp.TOKEN},
                                 data=data,
                                 verify=False)
        return response

    @staticmethod
    def send_delete_request(end_point):
        url = EnvSetUp.API + end_point
        response = requests.delete(url, headers={'Authorization': 'Bearer ' + EnvSetUp.TOKEN}, verify=False)
        return response
