programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary["Bug"])

#Add item to dictionary
programming_dictionary["Newkey"] = "nova vrijednost u dictionariju"
print(programming_dictionary)

#Remove item from dictionary
programming_dictionary.pop("Bug")
print(programming_dictionary)

#New empty dictionary
empty = {}

for key in programming_dictionary:
  print(key) #this print keys only

#Nesting
countrycity = {
  "Croatia" : "Zagreb",
  "England" : "London"
}

travellog = {
  "Croatia" : {"visited_cities": ["Rijeka", "Senj", "Zadar"],
               "novisits": 12},
  "England" : ["London", "Manchester", "Leicester"]
}