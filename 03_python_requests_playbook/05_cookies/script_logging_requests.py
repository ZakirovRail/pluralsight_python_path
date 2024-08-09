import requests
import logging
from requests.exceptions import RetryError
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


logging.basicConfig(level=logging.DEBUG)
requests_log = logging.getLogger("urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

session = requests.Session()
retries = Retry(total=3, backoff_factor=0.1, status_forcelist=[500], allowed_methods={"GET"})
session.mount("http://127.0.0.1", HTTPAdapter(max_retries=retries))

try:
    response = session.get("http://127.0.0.1:8000/flaky")
    print("Final response status:", response.status_code)
except RetryError:
    print("Maximum retries exceeded. Server is not available.")
