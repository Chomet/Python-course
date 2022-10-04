# File not found
try:
    with open("not_exist") as file:
        file.read()
except FileNotFoundError as msg:  # we can check with only except keyword, but then it will catch all errors
                                  # we can make multiple except clauses, one for each type of error
    print(f"File is missing: {msg}")
else:
    print("This will happen only if there were no exceptions")
finally:
    print("This will execute whatever happens")

# Key error
#new_dict = {"key": "value"}
#parameter = new_dict["not_exist"]

# Index error
#new_list = ["a", "b", "c"]
#parameterlist = new_list[4]

# Type error
#numb = 5 + "4"

# Our own error
height = int(input("Input height: "))
weight = int(input("Input weight: "))
bmi = weight / height**2
if bmi < 1:
    raise ValueError("BMI is not real, you entered something wrong")
