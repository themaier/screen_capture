import requests
import time
import json

HEADER = {"accept": "application/json"}
BASE_URL = "https://how-too.coflnet.com"
# BASE_URL = "http://localhost:8000"
PATH = "/api/api/tutorials"


# def post(json=None, files=None):
#     """Send a POST request to the specified path with JSON or multipart data."""
#     response = requests.post(
#         f"{BASE_URL}{PATH}", json=json, files=files, headers=HEADER
#     )
#     return response.json()


def post(data=None, files=None):
    """Send a POST request to the specified path with JSON or multipart data."""
    multipart_form_data = []
    multipart_form_data.append(("tutorial_str", (None, data.json())))
    for file in files:
        # multipart_form_data.append(("files", ("b.jpg", file, "image/jpeg")))
        multipart_form_data.append(file)
    print(multipart_form_data)
    response = requests.post(
        f"{BASE_URL}{PATH}", headers=HEADER, files=multipart_form_data
    )

    print(response.json())
    return response.json()
