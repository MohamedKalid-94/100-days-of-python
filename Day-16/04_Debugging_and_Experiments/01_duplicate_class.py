# Day 16 - Debugging and Experiments
# Example 01: Duplicate Class Definition
#
# Problem:
# Defining the same class twice causes the second definition
# to replace the first definition.


# First CoffeeMaker class.
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


# Accidentally defining CoffeeMaker again.
class CoffeeMaker:

    def __init__(self):
        self.resources = {
            "water": 100,
        }


# Create an object using CoffeeMaker.
coffee_maker = CoffeeMaker()


# The object is created using the SECOND CoffeeMaker class.
print(coffee_maker.resources)


# Uncommenting the line below will cause an error because
# the second CoffeeMaker class does not contain report().

# coffee_maker.report()