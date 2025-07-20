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

def print_resources(material_resource, money):
    water = material_resource["water"]
    milk = material_resource["milk"]
    coffe = material_resource["coffee"]
    print(f"Water: {water}ml \nMilk: {milk}ml \nCoffe: {coffe}g \nMoney: ${money}")

def check_resources(coffe_type):
    for ingredients_type in coffe_type:
        if coffe_type[ingredients_type] > resources[ingredients_type]:
            print(f"Sorry there is not enough {ingredients_type}.")
            return False
    return True

def process_coins():
    total = 0
    print("Please insert coins.")
    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    for coin_type in coins:
        coin = int(input(f"How many {coin_type}?: "))
        total += coin * coins[coin_type]
    return total

def check_transaction_successful(coffe_price, paying_money):
    global shop_money
    if paying_money == coffe_price:
        shop_money += paying_money
        return True
    elif paying_money > coffe_price:
        shop_money += coffe_price
        print(f"Here is ${(paying_money - coffe_price):.2f} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def deduct_resources(coffe_ingredients, drink_name):
    for coffe_ingredients_type in coffe_ingredients:
        resources[coffe_ingredients_type] -= coffe_ingredients[coffe_ingredients_type]
    print(f"Here is your {drink_name}. Enjoy!")

is_selling = True
shop_money = 0

while is_selling:
    coffe_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffe_choice == "off":
        print("Machine is down.")
        is_selling = False
    elif coffe_choice == "report":
        print_resources(resources, shop_money)
    else:
        drink = MENU[coffe_choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if check_transaction_successful(drink["cost"], payment):
                deduct_resources(drink["ingredients"], coffe_choice)
