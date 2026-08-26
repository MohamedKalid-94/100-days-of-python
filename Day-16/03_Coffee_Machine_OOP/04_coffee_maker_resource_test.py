# Day 16 - OOP Coffee Machine
# Step 09: Testing Resource Availability
#
# This file demonstrates both:
# - Enough resources
# - Not enough resources


class CoffeeMaker:

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def is_resource_sufficient(self, drink):

        for item in drink.ingredients:

            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False

        return True


class Drink:

    def __init__(self, name, water, milk, coffee):
        self.name = name

        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }


coffee_maker = CoffeeMaker()


# Test 1: Enough resources.
latte = Drink(
    name="latte",
    water=200,
    milk=150,
    coffee=24,
)

if coffee_maker.is_resource_sufficient(latte):
    print("There are enough resources.")


print()


# Test 2: Not enough water.
large_drink = Drink(
    name="large coffee",
    water=400,
    milk=100,
    coffee=20,
)

coffee_maker.is_resource_sufficient(large_drink)