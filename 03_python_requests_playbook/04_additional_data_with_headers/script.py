import requests
import pprint

# response = requests.get(
#     "http://127.0.0.1:8000/items"
# )
#
# pprint.pp(response.headers)
# print(response.headers)

# =====================================================================================================================

custom_headers = {
    "Authorisation": "Bearer ACCESS_TOKEN",
    "Accept": "application/json",
}

response = requests.get(
    "http://127.0.0.1:8000/api/items",
    headers=custom_headers
)

print(response.request.headers)
