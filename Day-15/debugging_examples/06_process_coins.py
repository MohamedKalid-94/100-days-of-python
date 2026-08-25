# Day 15 - Coffee Machine
# Step 6: Process the customer's coins.
# Practice: input, calculations, variables, and return values.


def process_coins():
    print("Please insert coins.")

    # Ask how many of each coin the customer inserted.
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    # Convert all coins into their dollar values and calculate the total.
    total = (
        quarters * 0.25
        + dimes * 0.10
        + nickels * 0.05
        + pennies * 0.01
    )

    # Return the total payment to the calling code.
    return total