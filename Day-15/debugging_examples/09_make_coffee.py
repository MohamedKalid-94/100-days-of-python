# Day 15 - Coffee Machine
# Step 9: Deduct ingredients after a successful purchase.
# Practice: functions, dictionary mutation, and program state.


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def make_coffee(choice, order_ingredients):
    # Deduct each required ingredient from the machine's resources.
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    # Confirm that the coffee has been prepared.
    print(f"Here is your {choice}. Enjoy!")


latte_ingredients = {
    "water": 200,
    "milk": 150,
    "coffee": 24,
}

make_coffee("latte", latte_ingredients)

print(resources)