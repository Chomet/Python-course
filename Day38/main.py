import requests
import datetime

# https://developer.nutritionix.com/ - nutritionix API, needs registration
APP_ID = "gfagfs"
APP_KEY = "agsgf"
NUTRITIONIX_URL = "agfad"
# https://sheety.co/docs/requests -> Sheety API and documentation, connect via Google Sheets
SHEETY_URL = "agffgaf"

query = input("What were you doing as exercise yesterday? ")
response = requests.post(url=NUTRITIONIX_URL,
                         json={'query': query,
                               "gender": "male",
                               "weight_kg": "7627627682",
                               "height_cm": "782682768276",
                               "age": "72868627867"},
                         headers={"x-app-id": APP_ID,
                                  "x-app-key": APP_KEY})
all_exercises = response.json()["exercises"]

current_day = datetime.date.today().strftime("%d/%m/%Y")
current_time = datetime.datetime.now().strftime("%H:%M:%S")
for exercise in all_exercises:
    sheety_response = requests.post(url=SHEETY_URL,
                                    json={"workout":
                                              {"date": current_day,
                                               "time": current_time,
                                               "exercise": exercise["name"].title(),
                                               "duration": exercise["duration_min"],
                                               "calories": exercise["nf_calories"]},
                                          })
    print(sheety_response.json())



