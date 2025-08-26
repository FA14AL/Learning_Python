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

profit = 0

def resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry! There is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please enter coins.")
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.10
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total

def check_transaction(money_received, drinks_cost):
    if money_received > drinks_cost:
        change = round(money_received - drinks_cost, 2)
        global profit
        profit += drinks_cost
        print(f"Here is ${change} in change.")
        return True
    else :
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Water:{resources['water']}ml\nMilk:{resources['milk']}ml\nCoffee:{resources['coffee']}g\nMoney:${profit}")

    else:
        drink = MENU[choice]
        if resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if check_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

