# Day 15 - Coffee Machine
# Step 4: Add the "report" command.
# Practice: elif, dictionary access, and displaying program state.

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

is_on = True

while is_on:
    choice = input(
        "What would you like? (espresso/latte/cappuccino): "
    ).lower()

    if choice == "off":
        is_on = False
        print("Coffee machine is turned off.")

    elif choice == "report":
        # Display the current amount of each resource.
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")

        # Display the amount of money collected.
        print(f"Money: ${money}")

    else:
        print(f"You selected: {choice}")