import requests
import json
from pprint import pprint

# # THIS WORKS:
# class Address:
#
#     dict_body = {'postcodes': [input("Please enter a postcode\n")]}
#     json_body = json.dumps(dict_body)
#     headers = {'Content-Type': 'application/json'}
#     address = "https://api.postcodes.io/postcodes/"
#     req_response = requests.post(address, headers=headers, data=json_body)
#     result = req_response.json()['result']
#
#     pprint(req_response.json())


class Address:
    def __init__(self):
        self.dict_body = {'postcodes': [input("Please enter a postcode\n")]}
        self.json_body = json.dumps(self.dict_body)
        self.headers = {'Content-Type': 'application/json'}
        self.address = "https://api.postcodes.io/postcodes/"
        self.req_response = requests.post(self.address, headers=self.headers, data=self.json_body)
        self.result = self.req_response.json()['result']



