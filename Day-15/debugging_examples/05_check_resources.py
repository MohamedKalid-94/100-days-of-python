# Day 15 - Coffee Machine
# Step 5: Check whether enough ingredients are available.
# Practice: functions, parameters, dictionaries, loops, and return values.

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order_ingredients):
    # Loop through every ingredient required for the coffee.
    for item in order_ingredients:

        # Compare the required amount with the available amount.
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")

            # Stop the function and report that resources are insufficient.
            return False

    # If every ingredient is available, return True.
    return True