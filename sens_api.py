import requests


class SensApi:

    def __init__(self, cred_path) -> None:

        with open(cred_path) as f:
            self.API_KEY = f.read()

    def update_tags(self, serial: str, tags: list):
        '''
        Itterates throguh a list and adds those as the tags
        '''

        # Grab only zones if the item cannot be an int
        tag_list = []

        for tag in tags:
            try:
                int(tag)
            except ValueError:
                tag_list.append(tag)

        headers = {
            'accept': 'application/json',
        }

        params = {
            'apiKey': self.API_KEY
        }

        json_data = {
            'tags': tag_list,
        }

        response = requests.put(
            f'https://stickntrack.sensolus.com/rest/api/v2/devices/{serial}', params=params, headers=headers, json=json_data)
        response.raise_for_status()
