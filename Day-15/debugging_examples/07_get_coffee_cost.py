# Day 15 - Coffee Machine
# Step 7: Get the selected coffee's ingredients and cost.
# Practice: nested dictionaries and dictionary access.

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

choice = input(
    "What would you like? (espresso/latte/cappuccino): "
).lower()

if choice in MENU:
    # Access the selected coffee's ingredients.
    order_ingredients = MENU[choice]["ingredients"]

    # Access the selected coffee's price.
    cost = MENU[choice]["cost"]

    print(f"You selected: {choice}")
    print(f"Ingredients: {order_ingredients}")
    print(f"Cost: ${cost:.2f}")

else:
    print("Sorry, that's not a valid choice.")