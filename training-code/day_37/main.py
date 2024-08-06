import requests
from datetime import datetime

username = "siddique"
token = "hf321ewdedssfrwefwfcws."
graph_id = "graph1"
pixels_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create user
response = requests.post(url=pixels_endpoint, json=user_params)
print("User creation response:", response.text)

graph_endpoint = f"{pixels_endpoint}/{username}/graphs"

graph_params = {
    "id": graph_id,
    "name": "Cycling graph",
    "unit": "km", 
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": token
}

# Create graph (uncomment if the graph does not already exist)
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print("Graph creation response:", response.text)

# Post pixel data
pixels_creation_endpoint = f"{pixels_endpoint}/{username}/graphs/{graph_id}"

today = datetime(year=2024, month=7, day=30)
# print(today.strftime("%Y-%m-%d"))

pixels_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15"
}

response = requests.post(url=pixels_creation_endpoint, json=pixels_data, headers=headers)
print("Pixel creation response:", response.text)





