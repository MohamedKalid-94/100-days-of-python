# Day 16 - Debugging Example
# Testing insufficient resources


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

                print(
                    f"Sorry, there is not enough {item}."
                )

                return False

        return True


class Drink:

    def __init__(self):

        self.ingredients = {
            "water": 400,
            "milk": 100,
            "coffee": 20,
        }


coffee_maker = CoffeeMaker()
drink = Drink()

coffee_maker.is_resource_sufficient(drink)