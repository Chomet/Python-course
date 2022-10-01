data = []

with open("weather_data.csv", "r") as days:
    lines = days.readlines()
    for line in lines:
        data.append(line)
    print(data)

import csv

with open("weather_data.csv", "r") as days:
    csv_data = csv.reader(days)
    temperatures = []
    for line in csv_data:
        if line[1] != "temp":
            temperatures.append(int(line[1]))
    print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["day"])
print(data.day)  # works too!
dict = data.to_dict()
list = data["temp"].to_list()
print(dict)
print(list)
print(sum(list)/len(list))
print(data["temp"].mean(), data["temp"].max())  # pandas function to return average of all values in list
print(data[data["temp"] == data["temp"].max()])  # getting row with max temperature
monday = data[data["day"] == "Monday"]
print(int(monday["temp"]))

new_dict = {
    "persons": ["Marin", "Davor", "Ante"],
    "scores": [55, 66, 77]
}
# converting dictionaries to Pandas and Pandas to csv file
# newdata = pandas.DataFrame(new_dict)
# newdata.to_csv("newdata.csv")
