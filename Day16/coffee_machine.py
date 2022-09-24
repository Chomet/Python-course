from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

items = Menu()
moneycount = MoneyMachine()
coffeemaker = CoffeeMaker()

while True:
    print(f"What do you like? ({items.get_items()})?")
    choices = input("Type report if you want report, type off to exit the program: ").lower()
    if choices == "report":
        coffeemaker.report()
        moneycount.report()
    elif choices == "off":
        break
    else:
        item = items.find_drink(choices)
        if item is not None:
            if moneycount.make_payment(item.cost) and coffeemaker.is_resource_sufficient(item):
                coffeemaker.make_coffee(item)
