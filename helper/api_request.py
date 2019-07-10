import requests
from config.env_setup import EnvSetUp


class ApiRequest:
    domain = EnvSetUp().SITE
    token = EnvSetUp().TOKEN

    def get_a_photo(self, id_photo):
        url = self.domain + "photos/{0}".format(str(id_photo))
        response = requests.get(url, verify=False)
        return response

    def unlike_a_photo(self, id_photo):
        url = self.domain + 'photos/{0}/like'.format(str(id_photo))

        response = requests.delete(url=url,
                                   headers={'Authorization': 'Bearer ' + self.token},
                                   verify=False)
        return response

    def like_a_photo(self, id_photo):
        url = self.domain + 'photos/{0}/like'.format(str(id_photo))
        response = requests.post(url=url,
                                 headers={'Authorization': 'Bearer ' + self.token},
                                 verify=False)
        return response

    def get_a_collection(self, id_collection):
        url = self.domain + 'collections/{0}'.format(str(id_collection))
        response = requests.get(url=url,
                                headers={'Authorization': 'Bearer ' + self.token},
                                verify=False)
        return response

    def create_a_collection(self, title="title", description="description", private=False):
        url = self.domain + 'collections/'
        data = {
            "title": title,
            "description": description,
            "private": private,
        }
        response = requests.post(url=url,
                                 headers={'Authorization': 'Bearer ' + self.token},
                                 data=data, verify=False)
        return response

    def delete_a_collection(self, id_collection):
        url = self.domain + "/collections/{0}".format(str(id_collection))
        response = requests.delete(url=url,
                                   headers={'Authorization': 'Bearer ' + self.token},
                                   verify=False)
        return response
