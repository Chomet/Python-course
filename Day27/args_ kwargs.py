def addall(*args):  # we can enter any numer of arguments inside this function
    total = 0
    for number in args:
        total += number
    return total


print(addall(1, 2, 4, 8, 9, 6, 8))


def calculateall(x, **kwargs):  # we can enter any number of named arguments here
    print(kwargs)  # this is a dictionary with names or arguments as keys and values as values
    x += kwargs["add"]
    print(x)


calculateall(15, add=5, subtract=3, multiply=2, divide=3)


class Car:
    def __init__(self, **kwargs):
        self.manufacturer = kwargs.get("manufacturer")
        self.model = kwargs.get("model")
        self.year = kwargs.get("year")
        self.price = kwargs.get("price")


car = Car(model="GTR", year=2015)
print(car.manufacturer, car.model, car.year, car.price)