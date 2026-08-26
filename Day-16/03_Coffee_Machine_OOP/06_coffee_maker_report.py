# Day 16 - OOP Coffee Machine
# Step 11: CoffeeMaker Report


class CoffeeMaker:

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):

        for item in drink.ingredients:

            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False

        return True

    def make_coffee(self, drink):

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

# Initial report.
coffee_maker.report()

print()

drink = Drink(
    name="latte",
    water=200,
    milk=150,
    coffee=24,
)

if coffee_maker.is_resource_sufficient(drink):
    coffee_maker.make_coffee(drink)

print()

# Report after making coffee.
coffee_maker.report()