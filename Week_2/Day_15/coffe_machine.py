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

end_transaction = True
# TODO Function that asks for coins and returns total.


def cash():
    total_coins = 0
    coins_values = {"quarters": 0.25, "dimes": 0.10, "nickels": 0.05, "pennies": 0.01}

    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    total_coins += quarters * coins_values["quarters"]
    dimes = int(input("How many dimes?: "))
    total_coins += dimes * coins_values["dimes"]
    nickels = int(input("How many nickels?: "))
    total_coins += nickels * coins_values["nickels"]
    pennies = int(input("How many pennies?: "))
    total_coins += pennies * coins_values["pennies"]

    return total_coins


# TODO While to repeat cycle.
while end_transaction:
    # TODO Input What would you like.
    coffee_selection = input("What would you like? (espresso, latte, cappuccino): ")
    if coffee_selection == "off":
        end_transaction = False
    elif coffee_selection == "report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}ml")
    # TODO Check if there are enough ingredients.
    elif coffee_selection in ["espresso", "latte", "cappuccino"]:
        for ingredient, amount in MENU[coffee_selection]["ingredients"].items():
            if resources[ingredient] < amount:
                print(f"Sorry there is not enough {ingredient}")
                break
        else:
            # TODO Ask to insert coins.
            total = cash()
            if total < MENU[coffee_selection]["cost"]:
                print("Sorry, you don't have enough")
            else:
                for ingredient, amount in MENU[coffee_selection]["ingredients"].items():
                    resources[ingredient] -= amount
                # TODO Print difference and coffee selection.
                print(MENU[coffee_selection]["cost"])
                print(f"Here is ${round((total - MENU[coffee_selection]["cost"]), 1)}")
                print(f"Here is your {coffee_selection} ☕ Enjoy!")
