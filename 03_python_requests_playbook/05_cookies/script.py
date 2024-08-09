import requests

# custom_cookies = {"user_id": "2"}
# response = requests.get("http://127.0.0.1:8000/api/cookies", cookies=custom_cookies)
# print(response.cookies.get_dict())
# print(response.cookies["user_id"])

# ===========================================================
# credentials = {"username": "some_name", "password": "pass"}
# login_response = requests.post("http://127.0.0.1:8000/api/login", data=credentials)
# login_cookies = login_response.cookies
# print("Cookies returned from login:")
# print(login_cookies.get_dict())
# print("Login response:")
# print(login_response.text)
# response = requests.get("http://127.0.0.1:8000/protected", cookies=login_cookies)
# print("Protected route:")
# print(response.status_code)
# print(response.text)
# ===========================================================

with requests.Session() as session:
    credentials = {"username": "some_name", "password": "pass"}

    session.post("http://127.0.0.1:8000/api/login", data=credentials)

    response = session.get("http://127.0.0.1:8000/protected")
    print("Protected route:")
    print(response.status_code)
    print(response.text)
