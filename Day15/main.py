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

COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01
}

def process_coins():
    total_value = 0
    for coin, value in COIN_VALUES.items():
        count = int(input(f"Enter the number of {coin}s: "))
        total_value += count * value
    return total_value

while True:
    order = input("What would you like? (espresso/latte/cappuccino) or report: ").lower()

    if order == "report":
        print(resources)
    elif order in MENU:
        drink = MENU[order]
        if all(resources[ingredient] >= drink["ingredients"].get(ingredient, 0) for ingredient in drink["ingredients"]):
            print("Please insert coins.")
            coin_inserted_value = process_coins()

            if coin_inserted_value >= drink["cost"]:
                change = round(coin_inserted_value - drink["cost"], 2)
                print(f"Enjoy your {order.capitalize()}! Here's your change: ${change}")
                resources["money"] += drink["cost"]
                for ingredient, quantity in drink["ingredients"].items():
                    resources[ingredient] -= quantity
            else:
                print("Sorry, not enough money. Money refunded.")
        else:
            print("Sorry, not enough ingredients to make the drink.")
    elif order == "off":
        print("Turning off the coffee machine.")
        break
    else:
        print("Invalid input. Please choose from the available options.")
