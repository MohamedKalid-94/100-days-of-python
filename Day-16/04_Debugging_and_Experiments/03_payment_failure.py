# Day 16 - Debugging Example
# Testing insufficient payment


class MoneyMachine:

    def __init__(self):
        self.money_received = 0

    def make_payment(self, payment, cost):

        if payment >= cost:

            self.money_received += cost

            change = payment - cost

            print(f"Change: ${change:.2f}")

            return True

        print("Sorry, that's not enough money.")

        return False


money_machine = MoneyMachine()

# Cost = $2.50
# Payment = $0.41

money_machine.make_payment(0.41, 2.50)

money_machine.report = lambda: print(
    f"Money: ${money_machine.money_received:.2f}"
)

money_machine.report()