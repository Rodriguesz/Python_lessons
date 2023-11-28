import requests 

TOKEN = "koljk43jkl24kj"
USERNAME = "rodrigues"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)

# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

from datetime import datetime 

GRAPH_ID = "graph1"

today = datetime.now()

add_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "50"
}

# pixel_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# response = requests.put(url=pixel_graph_endpoint, json=add_pixel, headers=headers)


update_pixel = {
    "quantity": "20"
}

# pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20231107"
# response = requests.put(url=pixel_update_endpoint, json=update_pixel, headers=headers)


pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20231107"

response = requests.delete(url=pixel_delete_endpoint, headers=headers)

