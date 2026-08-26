# Day 16 - OOP Coffee Machine
# Step 06: MenuItem and Menu Classes
#
# Topics:
# - Creating classes
# - Creating objects
# - Object attributes
# - Lists of objects


class MenuItem:

    def __init__(self, name, water, milk, coffee, cost):
        # Store the name of the drink.
        self.name = name

        # Store the cost of the drink.
        self.cost = cost

        # Store the ingredients required for the drink.
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }


class Menu:

    def __init__(self):
        # Create MenuItem objects.
        self.menu = [
            MenuItem(
                name="espresso",
                water=50,
                milk=0,
                coffee=18,
                cost=1.5,
            ),
            MenuItem(
                name="latte",
                water=200,
                milk=150,
                coffee=24,
                cost=2.5,
            ),
            MenuItem(
                name="cappuccino",
                water=250,
                milk=100,
                coffee=24,
                cost=3.0,
            ),
        ]

    def get_items(self):
        # Return all available drink names.
        return "/".join(item.name for item in self.menu)

    def find_drink(self, order_name):
        # Search through all MenuItem objects.
        for item in self.menu:

            # Check whether the requested drink exists.
            if item.name == order_name:
                return item

        # Return None if the drink doesn't exist.
        print("Sorry, that item is not available.")
        return None


# Create a Menu object.
menu = Menu()

# Display available drinks.
print(menu.get_items())

# Test finding a drink.
drink = menu.find_drink("latte")

if drink:
    print(f"Drink: {drink.name}")
    print(f"Cost: ${drink.cost:.2f}")
    print(f"Ingredients: {drink.ingredients}")