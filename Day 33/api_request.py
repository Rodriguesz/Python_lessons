import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# response.raise_for_status()

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (latitude, longitude)
# print(iss_position)

parameters= {
    "lat": -22.751070,
    "long": -47.333260,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time = datetime.now()

print(sunrise)
print(sunset)
print(time.hour)