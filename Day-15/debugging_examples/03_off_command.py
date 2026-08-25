# Day 15 - Coffee Machine
# Step 3: Add the "off" command.
# Practice: while loop and changing program state.

is_on = True

while is_on:
    choice = input(
        "What would you like? (espresso/latte/cappuccino): "
    ).lower()

    if choice == "off":
        # Changing is_on to False stops the while loop.
        is_on = False
        print("Coffee machine is turned off.")

    else:
        print(f"You selected: {choice}")