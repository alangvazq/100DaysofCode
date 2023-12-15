from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drink_info = Menu()
resources = CoffeeMaker()
money = MoneyMachine()

coffee_maker = True

while coffee_maker:
    choice = input(f"What would you like? ({drink_info.get_items()}): ")
    if choice == "off":
        coffee_maker = False
    elif choice == "report":
        resources.report()
        money.report()
    else:
        drink = drink_info.find_drink(choice)
        if resources.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                resources.make_coffee(drink)
