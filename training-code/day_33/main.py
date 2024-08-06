# import requests

# responce = requests.get("http://api.open-notify.org/iss-now.json")
# responce.raise_for_status()

# data = responce.json()

# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
# iss_position = (latitude,longitude)
# print(iss_position)

import requests
from datetime import datetime

my_lat = 16.506174
my_lng = 80.648018
parameters = {
    "lan":my_lng,
    "lng":my_lng,
    "formated":0,
}
responce = requests.get("https://api.sunrise-sunset.org/json?lat=80.648018&lng=80.648018&formated=0",params=parameters)
responce.raise_for_status()
data = responce.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)  

time_now = datetime.now()

print(time_now)
