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

# try:
#     response = requests.get("http://127.0.0.1:8000/api/something")
#     response.raise_for_status()
# except requests.exceptions.HTTPError as http_err:
#     print(f"HTTP error occurred: {http_err}")
# except Exception as err:
#     print(err)
# else:
#     print(response.status_code)

# =====================================================================================================================

# query_params = {"offset": 2, "limit": 2, "max_price": 40}
# response = requests.get("http://127.0.0.1:8000/api/items", params=query_params)
# print(response.json())

# =====================================================================================================================


# def log_url(response, *args, **kwargs):
#     print(f"Requested URL: {response.url}")
#
#
# response = requests.get("http://127.0.0.1:8000/api/items", hooks={"response": log_url})

# =====================================================================================================================

# response = requests.post(
#     "http://127.0.0.1:8000/items/new",
#     data={"name": "Another item", "price": 44},
#     allow_redirects=False,
# )
# print(response.request.headers["content-type"])
# print(response.request.body)

# =====================================================================================================================

# message_body = {"name": "New ITEM 08_04_2", "price": 22}
#
# response = requests.post(
#     "http://127.0.0.1:8000/ipi/items",
#     json=message_body
# )
# print(response.request.headers["content-type"])
# print(response.request.body)

# =====================================================================================================================

# import xml.etree.ElementTree as ET
#
# message_body = """
# <item>
#     <name>Some item</name>
#     <price>300</price>
# </item>
# """
#
# response = requests.post(
#     "http://127.0.0.1:8000/ipi/items/xml",
#     data=message_body,
#     headers={"Content-Type": "application/xml"}
# )
#
# # print(response.request.headers["content-type"])
# # print(response.request.body)
#
# print(ET.fromstring(response.text).find("name").text)
# print(ET.fromstring(response.text).find("price").text)


# =====================================================================================================================


file1 = open("file1.csv", "rb")
file2 = open("file2.csv", "rb")

files = [
    ("files", ("file1.csv", file1, "text/csv")),
    ("files", ("file2.csv", file1, "text/csv")),
]

response = requests.post(
    "http://127.0.0.1:8000/upload-files",
    files=files,
)

file1.close()
file2.close()

print(response.json())
