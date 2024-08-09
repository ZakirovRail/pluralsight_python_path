import requests

# response = requests.get("http://127.0.0.1:8000/old-route")
# print(response.url)
# print(response.status_code)
# print(response.text)
"Will be automatically redirect to http://127.0.0.1:8000/new-route"

# ===========================

# response = requests.head("http://127.0.0.1:8000/old-route", allow_redirects=True)
# print(response.url)
# print(response.status_code)
# print(response.text)
"Will redirect, because HEAD method doesn;t allow redirects, but with allow_redirects it allows "

# ===========================

# try:
#     response = requests.get("http://127.0.0.1:8000/slow-response", timeout=3)
#     print(response.json())
# except requests.exceptions.ConnectTimeout:
#     print("The request failed to connect in the allotted time.")
# except requests.exceptions.ReadTimeout:
#     print("The server did not send any data in the allotted amount of time")

# ===========================

try:
    response = requests.get("http://10.255.255.1", timeout=(5, 6))
    print(response.json())
except requests.exceptions.ConnectTimeout:
    print("The request failed to connect in the allotted time.")
except requests.exceptions.ReadTimeout:
    print("The server did not send any data in the allotted amount of time")
