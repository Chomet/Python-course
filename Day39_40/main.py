import requests
import datetime

TEQUILA_ID = "arvterevt"
TEQUILA_KEY = "avertarezrevrze"
TEQUILA_URL = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_SEARCH = "https://api.tequila.kiwi.com/v2/search"
SHEETY_URL = "rvtasrzezezt"

## Needs to be run only once, only needed for getting IATA codes
##sheety_cities = requests.get(url=SHEETY_URL).json()["prices"]
##sheet_row = 2
##for city in sheety_cities:
##    tequilla_codes = requests.get(url=TEQUILA_URL,
##                                  params={"term": city["city"],
##                                          "location_types": "city"},
##                                  headers={"apikey": TEQUILA_KEY})
##    code = tequilla_codes.json()["locations"][0]["code"]
##    sheety_response = requests.put(url=SHEETY_URL + f"/{sheet_row}",
##                                   json={"price":
##                                            {"iataCode": code}
##                                         })
##    sheet_row +=1

sheety_cities = requests.get(url=SHEETY_URL).json()["prices"]
date_from = datetime.date.today().strftime("%d/%m/%Y")
day_month_year = date_from.split("/")
new_day = int(day_month_year[0])
new_month = (int(day_month_year[1]) + 6) % 12
if int(day_month_year[1]) + 6 > 12:
    new_year = int(day_month_year[2]) + 1
else:
    new_year = int(day_month_year[2])
date_to = datetime.date(day=new_day, month=new_month, year=new_year).strftime("%d/%m/%Y")
print(date_from, date_to)

for city in sheety_cities:
    tequilla_flights = requests.get(url=TEQUILA_SEARCH,
                                    params={"fly_from": "LON",
                                            "fly_to": city["iataCode"],
                                            "date_from": date_from,
                                            "date_to": date_to,
                                            "price_to": city["lowestPrice"]
                                            },
                                    headers={"apikey": TEQUILA_KEY})
    flights = tequilla_flights.json()["data"]
    if len(flights) == 0:
        print(f"No flight from London to {city['city']} for target cheapest price of {city['lowestPrice']}"
              f" in next 6 months")
    for flight in flights:
        print(flight["cityFrom"], flight["flyFrom"], flight["utc_departure"], "-", flight["cityTo"], flight["flyTo"],
              flight["utc_arrival"], "Price: ", flight["price"])
