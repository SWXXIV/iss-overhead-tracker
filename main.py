import requests
import datetime as dt

SEATTLE_LATITUDE = 47.6061
SEATTLE_LONGITUDE = -122.3328

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])

iss_position = (iss_latitude, iss_longitude)

print(iss_position)

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

# sunrise_time = sunrise.split("T")[1].split("-")[0]
# sunset_time = sunset.split("T")[1].split("-")[0]

sunrise_time = dt.datetime.strptime(sunrise, '%Y-%m-%dT%H:%M:%S%z').time()
sunset_time = dt.datetime.strptime(sunset, '%Y-%m-%dT%H:%M:%S%z').time()

print(sunrise)
print(sunrise_time)

# time_now = str(dt.datetime.now()).split(" ")[1].split(".")[0]
print(time_now)

#If the ISS is close to my current position

# if abs(iss_latitude - SEATTLE_LATITUDE) <= 5 and
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

