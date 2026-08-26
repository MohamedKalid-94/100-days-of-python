# Day 16 - OOP Coffee Machine
# Step 08-11: CoffeeMaker Class
#
# Topics:
# - Object state
# - Methods
# - Checking resources
# - Modifying resources
# - Reporting resources


class CoffeeMaker:

    def __init__(self):
        # Store the available resources.
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        # Display current resources.
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        # Check every ingredient required by the drink.
        for item in drink.ingredients:

            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False

        return True

    def make_coffee(self, drink):
        # Deduct the ingredients used by the drink.
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]

        print(f"Here is your {drink.name}. Enjoy!")


# Temporary Drink class used only for testing.
class Drink:

    def __init__(self, name, water, milk, coffee):
        self.name = name

        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }


# Create CoffeeMaker object.
coffee_maker = CoffeeMaker()


# Display initial resources.
coffee_maker.report()

print()


# Create a test latte.
drink = Drink(
    name="latte",
    water=200,
    milk=150,
    coffee=24,
)


# Check resources.
if coffee_maker.is_resource_sufficient(drink):

    # Make coffee.
    coffee_maker.make_coffee(drink)

print()


# Display remaining resources.
coffee_maker.report()