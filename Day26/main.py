# List comprehensions
oldlist = [1, 2, 3]
newlist = [item + 1 for item in oldlist]
print(newlist)

name = "Marin"
newname = [letter for letter in name]
print(newname)

doublednums = [n*2 for n in range(1, 5)]
print(doublednums)

listofnums = [11, 22, 33, 44, 55, 66, 88, 711]
evennums = [n for n in listofnums if n % 2 == 1]
print(evennums)

# Dictionary comprehension
dict = {f"key{n}": n for n in listofnums}
print(dict)
new_dict = {key: n*2 for (key, n) in dict.items() if n % 2 == 1} # new dictionary from old one
print(new_dict)

students = {
    "persons": ["Marin", "Davor", "Ante"],
    "scores": [55, 66, 77]
}

# DataFrame looping
import pandas
students_panda = pandas.DataFrame(students)
for (key, value) in students_panda.items():
    print(key)  # persons, scores
    print(value)  # everything else: rows with persons and scores plus name of column and type
for (rowindex, data) in students_panda.iterrows():
    print(rowindex)  # 0,1,2 etc
    print(data["persons"], data["scores"])
    # Above method is much better way for looping DataFrames
