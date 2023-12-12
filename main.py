import requests
from datetime import datetime as dt

SEATTLE_LATITUDE = 47.6061
SEATTLE_LONGITUDE = -122.3328

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (latitude, longitude)
#
# print(iss_position)

# ------------------ check if it's dark out ---------------

parameters = {
    "lat": SEATTLE_LATITUDE,
    "lng": SEATTLE_LONGITUDE,
    "formatted": 0,
    "tzId": "America/Los_Angeles",
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_time = sunrise.split("T")[1].split("-")[0]
sunset_time = sunset.split("T")[1].split("-")[0]

print(sunrise)
print(sunrise_time)

time_now = str(dt.now()).split(" ")[1].split(".")[0]

print(time_now)