import requests
from datetime import datetime
import creds

PIXELA_END_POINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph11"
# TODO 1: Create a user account:
PARAMS = {
    "token": creds.TOKEN,
    "username": creds.USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=PIXELA_END_POINT, json=PARAMS)
print(response.text)

# TODO 2: Create a graph definition:
GRAPH_END_POINT = f"{PIXELA_END_POINT}/{creds.USERNAME}/graphs"
GRAPH_PARAMS = {
    "id": GRAPH_ID,
    "name": "Project Building Tracker",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}
HEADERS = {
    "X-USER-TOKEN": creds.TOKEN
}
#
response = requests.post(url=GRAPH_END_POINT, headers=HEADERS, json=GRAPH_PARAMS)
print(response.text)

# TODO 3: Post value to the graph:
#
date = datetime.strftime(datetime.today(), "%y%y%m%d")
POST_END_POINT = f"{ PIXELA_END_POINT}/{creds.USERNAME}/graphs/{GRAPH_ID}"

GRAPH_BODY = {
    "date": "20220612",
    "quantity": "5"
}

response = requests.post(url=POST_END_POINT, headers=HEADERS, json=GRAPH_BODY)
print(response.text)

# TODO 4: Updating the values in Graph:
PUT_END_POINT = f"{PIXELA_END_POINT}/{creds.USERNAME}/graphs/{GRAPH_ID}/20220612"
PARAM = {
    "quantity": "40"
}
response = requests.put(url=PUT_END_POINT, headers=HEADERS, json=PARAM)
print(response.text)

