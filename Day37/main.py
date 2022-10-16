import requests
import datetime
import time
# https://pixe.la/ -> how to use this API
# https://docs.pixe.la/ -> explanation for each API call

USERNAME = "agfggf"
TOKEN = "agdfg"
ID = "agfg"

# this needs to be executed only once
# create_user = requests.post(url="https://pixe.la/v1/users",
#                             json={"token": TOKEN,
#                                   "username": USERNAME,
#                                   "agreeTermsOfService": "yes",
#                                   "notMinor": "yes"})
# print(create_user.json())

# this also needs to be executed only once
# graph_definition = requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs",
                                 # json={"id": ID,
                                 #       "name": "ssgdagg",
                                 #       "unit": "km",
                                 #       "type": "float",
                                 #       "color": "shibafu"},
                                 # headers={"X-USER-TOKEN": TOKEN})
# print(graph_definition.json())

# get current day and convert it to format we need
current_day = datetime.date.today().strftime("%Y%m%d")

# this posts a new value and replaces the old one
post_value = requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{ID}",
                           json={"date": current_day,
                                 "quantity": "1"},
                           headers={"X-USER-TOKEN": TOKEN})

# we can't create and update the pixel immediately, we will get an error, we need to wait a moment to update it
time.sleep(1)

# this updates the old value
put_value = requests.put(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{ID}/{current_day}",
                         json={"quantity": "3"},
                         headers={"X-USER-TOKEN": TOKEN})

time.sleep(1)

# this deletes the registered value with specific username, ID on specific day
delete_value = requests.delete(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{ID}/{current_day}",
                               headers={"X-USER-TOKEN": TOKEN})

print(post_value, put_value, delete_value)
