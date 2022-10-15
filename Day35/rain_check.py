import requests

# check https://openweathermap.org/api/one-call-3 for API call
# one call 2.5 still works
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",
                        params={"lat": 45.8,
                                "lon": 15.93,
                                # exclude parameter is not actually needed since we still need to dig in hourly tab
                                # "exclude": "current,minutely,daily,alerts",
                                "appid": "yourid"})
# http://jsonviewer.stack.hu/ -> see JSON answer more clearly
hourly_weather_report = response.json()["hourly"]
# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2 - ID is what we are interested to check
weather_codes = []
for n in range(0, 12):
    # There can be a multiple weather conditions but first one is always a main condition
    # Since we are only interested in raining, we can only check for first element under weather parameter
    weather_id = int(hourly_weather_report[n]["weather"][0]["id"])
    if weather_id < 700:
        print(f"In {n+1} hours there is a chance for rain")
    weather_codes.append(weather_id)
print(weather_codes)

