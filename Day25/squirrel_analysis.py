import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = data["Primary Fur Color"].unique()[1::]
colorcount = data["Primary Fur Color"].value_counts();
colorcount.to_csv("wow.csv")
countlist = []
colorlist = []
for color in colors:
    colorlist.append(color)
for count in colorcount:
    countlist.append(count)
dict = {"Fur Color": colorlist, "Count": countlist}
print(dict)
newdata = pandas.DataFrame(dict)
newdata.to_csv("squirrel_count.csv")
