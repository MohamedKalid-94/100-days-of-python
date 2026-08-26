# Day 16 - OOP Coffee Machine
# Step 13: Testing Payment Processing
#
# Test cases:
# 1. Successful payment
# 2. Insufficient payment


class MoneyMachine:

    def __init__(self):
        self.money_received = 0

    def report(self):
        print(f"Money: ${self.money_received:.2f}")

    def process_coins(self):
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

    def make_payment(self, cost):

        payment = self.process_coins()

        if payment >= cost:

            self.money_received += cost

            change = payment - cost

            print(f"Here is ${change:.2f} in change.")

            return True

        print("Sorry, that's not enough money. Money refunded.")

        return False


money_machine = MoneyMachine()

cost = 2.50

if money_machine.make_payment(cost):
    print("Payment successful.")

money_machine.report()