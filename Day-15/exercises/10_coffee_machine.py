# Day 15 - Coffee Machine
# Final Project
#
# This program simulates a coffee machine.
#
# The machine can:
# 1. Accept a coffee order.
# 2. Check available resources.
# 3. Process coins.
# 4. Check whether payment is sufficient.
# 5. Calculate and return change.
# 6. Add successful sales to machine money.
# 7. Deduct ingredients after a successful purchase.
# 8. Display a resource report.
# 9. Turn itself off.


def check_resources(order_ingredients):
    """Check whether the machine has enough ingredients."""

    # Loop through every ingredient required by the selected coffee.
    for item in order_ingredients:

        # Compare the required quantity with the available quantity.
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False

    # All required ingredients are available.
    return True


def process_coins():
    """Collect coins and return the total payment."""

    print("Please insert coins.")

    # Get the number of each type of coin.
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    # Convert each coin into its dollar value.
    total = (
        quarters * 0.25
        + dimes * 0.10
        + nickels * 0.05
        + pennies * 0.01
    )

    # Return the calculated payment.
    return total


def make_coffee(choice, order_ingredients):
    """Deduct ingredients and serve the selected coffee."""

    # Deduct the required amount of every ingredient.
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {choice}. Enjoy!")


# Menu containing every available coffee.
# Each coffee has its required ingredients and cost.
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


# Starting resources available inside the machine.
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Total money collected by the machine.
money = 0

# Controls whether the machine continues running.
is_on = True


# Main program loop.
while is_on:

    # Ask the customer what coffee they want.
    choice = input(
        "What would you like? (espresso/latte/cappuccino): "
    ).lower()

    # The "off" command stops the machine.
    if choice == "off":
        is_on = False
        print("Coffee machine is turned off.")

    # The "report" command displays the current machine state.
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")

    # Handle a normal coffee order.
    else:

        # Make sure the user's choice exists in the menu.
        if choice in MENU:

            # Get the ingredients required for the selected coffee.
            order_ingredients = MENU[choice]["ingredients"]

            # Check whether the machine has enough resources.
            if check_resources(order_ingredients):

                print(f"You selected: {choice}")

                # Get the price of the selected coffee.
                cost = MENU[choice]["cost"]
                print(f"Cost: ${cost:.2f}")

                # Ask the customer to insert coins.
                payment = process_coins()

                # Check whether the customer paid enough.
                if payment >= cost:

                    # Add only the coffee's cost to machine revenue.
                    # Extra money is returned as change.
                    money += cost

                    # Calculate the change.
                    change = payment - cost

                    print(f"Here is ${change:.2f} in change.")

                    # Deduct ingredients and serve the coffee.
                    make_coffee(choice, order_ingredients)

                else:
                    # Do not keep the money when payment is insufficient.
                    print("Sorry, that's not enough money. Money refunded.")

        else:
            # Handle unknown coffee choices.
            print("Sorry, that's not a valid choice.")