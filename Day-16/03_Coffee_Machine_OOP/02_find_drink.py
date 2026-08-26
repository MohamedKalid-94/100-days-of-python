# Day 16 - OOP Coffee Machine
# Step 07: Finding a Drink
#
# This step focuses on testing the find_drink() method.


class MenuItem:

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost

        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }


class Menu:

    def __init__(self):
        self.menu = [
            MenuItem("espresso", 50, 0, 18, 1.5),
            MenuItem("latte", 200, 150, 24, 2.5),
            MenuItem("cappuccino", 250, 100, 24, 3.0),
        ]

    def get_items(self):
        return "/".join(item.name for item in self.menu)

    def find_drink(self, order_name):

        for item in self.menu:

            if item.name == order_name:
                return item

        print("Sorry, that item is not available.")
        return None


# Create Menu object.
menu = Menu()

print(menu.get_items())


# Test with a valid drink.
drink = menu.find_drink("latte")

if drink:
    print(f"Drink: {drink.name}")
    print(f"Cost: ${drink.cost:.2f}")
    print(f"Ingredients: {drink.ingredients}")


# Test with an invalid drink.
invalid_drink = menu.find_drink("pizza")