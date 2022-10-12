# possible status codes: https://www.webfx.com/web-development/glossary/http-status-codes/
import requests
import datetime

response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
response2 = requests.get(url="http://api.open-notify.org/iss-now.j1son")
code1 = response1.status_code
code2 = response2.status_code
iss_long = 0
iss_lat = 0
if code1 != 200:
    response2.raise_for_status()  # built in raise exception function
else:
    print(response1.json())
    iss_long = float(response1.json()["iss_position"]["longitude"])
    iss_lat = float(response1.json()["iss_position"]["latitude"])
    print(iss_long, iss_lat)

# https://sunrise-sunset.org/api -> API for sunrise and sunset
# params attribute is dictionary of required params for API call, documentation mentions them
sunset_response = requests.get(url="https://api.sunrise-sunset.org/json", params={"lat": 45.8, "long": 15.93, "formatted": 0})
sunrise_time = sunset_response.json()["results"]["sunrise"].split("T")[1]
sunset_time = sunset_response.json()["results"]["sunset"].split("T")[1]
print(sunrise_time.split(":")[0])
print(sunset_time.split(":")[0])
date = datetime.datetime.now()
print(date.hour)

if abs(iss_long - 45.8) < 10 and abs(iss_lat - 15.93) < 10:
    if not (int(sunrise_time.split(":")[0]) < date.hour < int(sunset_time.split(":")[0])):
        print(sunrise_time, sunset_time, date.hour)
