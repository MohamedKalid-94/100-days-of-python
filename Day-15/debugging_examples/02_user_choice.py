# Day 15 - Coffee Machine
# Step 2: Get the user's coffee choice.
# Practice: while loop, input(), variables, and .lower().

is_on = True

while is_on:
    # Ask the user which coffee they want.
    # .lower() converts the input to lowercase.
    choice = input(
        "What would you like? (espresso/latte/cappuccino): "
    ).lower()

    # Display the selected choice.
    print(f"You selected: {choice}")