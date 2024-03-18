import requests

# response = requests.get("http://127.0.0.1:8000/api/items")
# response = requests.get("http://127.0.0.1:8000/api/something")
# print(response.status_code)
#
# if response.status_code == 200:
#     print("Success!")
# elif response.status_code == 500:
#     print("Server error.")
# elif response.status_code == 404:
#     print("Page not Found")
#
# print(response.text)

# =====================================================================================================================

try:
    response = requests.get("http://127.0.0.1:8000/api/something")
    response.raise_for_status()
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(err)
else:
    print(response.status_code)








