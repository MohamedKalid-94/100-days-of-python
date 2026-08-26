# Day 16 - OOP Coffee Machine
# Step 10: Making Coffee
#
# Topics:
# - Deducting resources
# - Modifying object state
# - Calling methods


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

    def make_coffee(self, drink):

        # Deduct each ingredient.
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]

        print(f"Here is your {drink.name}. Enjoy!")


class Drink:

    def __init__(self, name, water, milk, coffee):
        self.name = name

        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }


coffee_maker = CoffeeMaker()

drink = Drink(
    name="latte",
    water=200,
    milk=150,
    coffee=24,
)


if coffee_maker.is_resource_sufficient(drink):
    coffee_maker.make_coffee(drink)

print(coffee_maker.resources)