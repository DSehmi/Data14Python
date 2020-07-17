import requests
from Models.single_postcode_model import SinglePCModel
from config_manager import base_url


class SinglePC():

    def __init__(self, single_postcode):
        self.url = "https://api.postcodes.io/postcodes/" + single_postcode
        self.request = requests.get(self.url)
        self.header_details = self.request.headers
        self.response_json = self.request.json()

    def response(self):
        return SinglePCModel(self.response_json)


pc = SinglePC("B7 4BB")
print(pc.response().latitude)
