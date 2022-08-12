import requests


class SensApi:

    def __init__(self, api_key) -> None:
        self.API_KEY = api_key

    def update_tags(self, serial: str, tags: list, address: str):
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

        address_info = address.split(sep=",")
        # add the country to the tags and remove the whitespace
        tag_list.append(address_info[-1].strip())
        # Add the city to the tags and remove the whitespace
        tag_list.append(address_info[-2].strip())

        print(f"tag list: {tag_list}")

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
