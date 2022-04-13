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
    "money": 0
}


def report():
    print(f"Water: {resources['water']} ml\nMilk: {resources['milk']} ml\nCoffee: {resources['coffee']} ml\nMoney: ${resources['money']}")


def check_resources(recipe):
    milk = MENU.get(recipe).get('ingredients').get('milk') if MENU.get(recipe).get('ingredients').get(
        'milk') is not None else 0
    water = MENU.get(recipe).get('ingredients').get('water')
    coffee = MENU.get(recipe).get('ingredients').get('coffee')

    if milk > resources['milk'] or water > resources['water'] or coffee > resources['coffee']:
        return False
    return True


def process_coins(recipe):
    cost = MENU.get(recipe).get('cost')
    print(f"Please insert coins. A {recipe} costs ${cost}")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = quarters * .25 + dimes * .1 + nickels * .05 + pennies * .01
    return total - cost


def make_drink(recipe):
    resources['water'] -= MENU[recipe]['ingredients']['water']
    resources['milk'] -= MENU[recipe]['ingredients']['milk']
    resources['coffee'] -= MENU[recipe]['ingredients']['coffee']
    resources['money'] += MENU[recipe]['cost']


running = True

while running:
    user_input = input("What would you like? (espresso/latte/cappuccino) ")
    if user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
        if not check_resources(user_input):
            print("Sorry, there are not enough ingredients")
        change = process_coins(user_input)
        if change < 0:
            print("Not enough coins!")
        else:
            print(f"Here is ${change} in change.")
            make_drink(user_input)
            print(f"Here is your {user_input}!")
    elif user_input == 'report':
        print(report())
    elif user_input == 'off':
        print("Turning off!")
        running = False


