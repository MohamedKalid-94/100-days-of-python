# Day 16 - OOP Coffee Machine
# Step 12-14: MoneyMachine Class
#
# Topics:
# - Object state
# - Processing coins
# - Payment validation
# - Change calculation
# - Recording money


class MoneyMachine:

    def __init__(self):
        # Store the total money collected.
        self.money_received = 0

    def report(self):
        # Display the money collected.
        print(f"Money: ${self.money_received:.2f}")

    def process_coins(self):
        # Ask the customer to insert coins.
        print("Please insert coins.")

        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        # Calculate the total value.
        total = (
            quarters * 0.25
            + dimes * 0.10
            + nickels * 0.05
            + pennies * 0.01
        )

        return total

    def make_payment(self, cost):
        # Process the customer's payment.
        payment = self.process_coins()

        # Check whether enough money was inserted.
        if payment >= cost:

            # Record only the cost of the drink.
            self.money_received += cost

            # Calculate change.
            change = payment - cost

            print(f"Here is ${change:.2f} in change.")

            return True

        # Payment was insufficient.
        print("Sorry, that's not enough money. Money refunded.")

        return False


# Create MoneyMachine object.
money_machine = MoneyMachine()


# Test payment.
cost = 2.50

if money_machine.make_payment(cost):
    print("Payment successful.")


# Display collected money.
money_machine.report()