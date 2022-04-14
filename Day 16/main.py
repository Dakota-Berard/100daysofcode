from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machineOn = True

menu = Menu()
coffeem = CoffeeMaker()
money = MoneyMachine()

while machineOn:
    user_input = input(f"What would you like? ({menu.get_items()}) ").lower()
    if user_input == "report":
        coffeem.report()
        money.report()
    elif user_input == "off":
        print("Shutting Down...")
        break
    else:
        drink = menu.find_drink(user_input)
        if coffeem.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            print("Creating drink...")
            coffeem.make_coffee(drink)
