# Day 16 - Debugging Example
# Testing an invalid menu item


class MenuItem:

    def __init__(self, name):
        self.name = name


class Menu:

    def __init__(self):

        self.menu = [
            MenuItem("espresso"),
            MenuItem("latte"),
            MenuItem("cappuccino"),
        ]

    def find_drink(self, order_name):

        for item in self.menu:

            if item.name == order_name:
                return item

        print("Sorry, that item is not available.")

        return None


menu = Menu()

# Invalid item.
drink = menu.find_drink("pizza")

if drink:
    print(drink.name)