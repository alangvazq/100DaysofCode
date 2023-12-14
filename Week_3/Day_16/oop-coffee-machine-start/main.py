from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drink_1 = MenuItem(name="espresso", cost=1.5, water=50, coffee=18, milk=0)
drink_2 = MenuItem(name="latte", cost=2.5, water=200, coffee=24, milk=150)
drink_3 = MenuItem(name="cappuccino", cost=3.0, water=250, coffee=24, milk=100)

drink_info = Menu()
resources = CoffeeMaker()
money = MoneyMachine()

coffee_maker = True

while coffee_maker:
    choice = input(f"What would you like? ({drink_info.get_items()}): ")
    if choice == "off":
        coffee_maker = False
    elif choice == "report":
        print(resources.report())
        print(money.report())
    else:
        if resources.is_resource_sufficient(drink_info.find_drink(choice)):
            if money.make_payment(drink_info.find_drink(choice).cost):
                resources.make_coffee(drink_info.find_drink(choice))

