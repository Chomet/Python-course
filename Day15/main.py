MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
QUARTER = 0.25
DIME = 0.1
NICKEL = 0.05
PENNY = 0.01


def make_coffee(choice):
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many quarters: "))
    total_amount = quarters * QUARTER + dimes * DIME + nickels * NICKEL + pennies * PENNY
    milk_exists = "milk" in MENU[choice]["ingredients"]
    if resources["water"] < MENU[choice]["ingredients"]["water"]:
        print("Not enough water in machine")
        return 0
    if milk_exists:
        if resources["milk"] < MENU[choice]["ingredients"]["milk"]:
            print("Not enough milk in machine")
            return 0
    if resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
        print("Not enough coffee in machine")
        return 0
    if total_amount < MENU[choice]["cost"]:
        print("Not enough money")
        return 0
    else:
        resources["water"] -= MENU[choice]["ingredients"]["water"]
        if milk_exists:
            resources["milk"] -= MENU[choice]["ingredients"]["milk"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
        print(f"Here is ${round(total_amount - MENU[choice]['cost'], 2)} in change")
        print(f"Here is your {choice}. Enjoy!")
        return MENU[choice]["cost"]


def print_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${money}")


while True:
    print("What do you like? (espresso/latte/cappuccino)?")
    choices = input("Type report if you want report, type off to exit the program: ").lower()
    if choices == "espresso" or choices == "latte" or choices == "cappuccino":
        money += make_coffee(choices)
    elif choices == "report":
        print_report()
    elif choices == "off":
        break
    else:
        print("Wrong input entered")
