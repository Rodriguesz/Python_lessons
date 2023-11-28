import requests
key = "d3f66f184969a517e17adc3d337105f9"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
# OWM_Endpoint = "https://pro.openweathermap.org/data/2.5/forecast/hourly"

weather_params = {
    "lat": -22.751070,
    "lon": -47.333260,
    "appid": key
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()

data = response.json()
print(data)