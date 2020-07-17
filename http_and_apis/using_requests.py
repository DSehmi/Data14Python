# NEVER CALL YOUR PYTHON FILE REQUESTS
# HTTP Status Codes
# 404 - Page Not Found
# 200 - OK (Success)

# import requests
# from pprint import pprint
#
# address = "https://api.postcodes.io/postcodes/UB2 4LU"
# req_response = requests.get(address)
#
# # print(req_response)
# # print(type(req_response))
#
# print(req_response.status_code)
# print(req_response.headers)
# pprint(req_response.content)
# pprint(type(req_response.content))  # bytes class
# pprint(req_response.json())
# pprint(type(req_response.json()))
#
#
# print(req_response.json()['result']['eastings'])
# print(req_response.json()['result']['northings'])
#
# result = req_response.json()['result']
# print(f"Eastings: {result['eastings']}; Northings: {result['northings']}")
#
# print(f"NUTS Code: {result['codes']['nuts']}")

# NEW SECTION

import requests
import json
from pprint import pprint

dict_body = {'postcodes': ["B7 4BB", "OX49 5NU", "M32 0JG", "NE30 1DP"]}
json_body = json.dumps(dict_body)
headers = {'Content-Type': 'application/json'}

address = "https://api.postcodes.io/postcodes/"
req_response = requests.post(address, headers=headers, data=json_body)

# pprint(req_response.json()['result'][0])
pprint(req_response.json()['result'])

for postcode in req_response.json()['result']:
    # print(postcode)
    result = postcode['result']
    print(f"Postcode: {result['postcode']}; Eastings: {result['eastings']}; "
          f"Northings: {result['northings']}; NUTS Code: {result['codes']['nuts']}")

class Address:
    def 