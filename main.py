import requests
import datetime as dt

SEATTLE_LATITUDE = 47.6061
SEATTLE_LONGITUDE = -122.3328

# ---------------- Where is the ISS? --------------#
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])

iss_position = (iss_latitude, iss_longitude)

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

# sunrise_time = sunrise.split("T")[1].split("-")[0]
# sunset_time = sunset.split("T")[1].split("-")[0]

# convert strings into datetime objects so you can compare them to current time like civilized machines
sunrise_time = dt.datetime.strptime(sunrise, '%Y-%m-%dT%H:%M:%S%z').time()
sunset_time = dt.datetime.strptime(sunset, '%Y-%m-%dT%H:%M:%S%z').time()

# print(sunrise)
# print(sunrise_time)

# time_now = str(dt.datetime.now()).split(" ")[1].split(".")[0]

# --------------- what time is it right now? ------------
time_now = dt.datetime.now().time()
# print(time_now)
# print(time_now > sunset_time)

# is the ISS within 5 degrees of me?

iss_within_5deg_lat = (abs(iss_latitude - SEATTLE_LATITUDE) <= 5)
iss_within_5deg_lng = (abs(iss_longitude - SEATTLE_LONGITUDE) <= 5)

# is it dark out?

is_day = (sunrise_time <= time_now <= sunset_time)


if iss_within_5deg_lat and iss_within_5deg_lng and not is_day:
    # this is where I'd email myself or SMS
    pass


