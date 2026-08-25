# Day 15 - Coffee Machine
# Step 8: Check whether the customer paid enough.
# Practice: comparison operators, if/else, arithmetic, and change.


def process_coins():
    print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = (
        quarters * 0.25
        + dimes * 0.10
        + nickels * 0.05
        + pennies * 0.01
    )

    return total


cost = 2.50
payment = process_coins()

if payment >= cost:
    # Calculate the money that must be returned to the customer.
    change = payment - cost

    print(f"Here is ${change:.2f} in change.")

else:
    print("Sorry, that's not enough money. Money refunded.")