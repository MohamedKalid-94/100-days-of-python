# Day 16 - OOP Coffee Machine
# Step 15: Connecting Menu, CoffeeMaker and MoneyMachine


from menu_class import Menu
from coffee_maker_class import CoffeeMaker
from money_machine_class import MoneyMachine


# Create objects from each class.
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


# Display available drinks.
print(menu.get_items())


# Test selecting a drink.
drink = menu.find_drink("latte")


if drink:

    print(f"Selected: {drink.name}")
    print(f"Cost: ${drink.cost:.2f}")

    # Check whether enough ingredients are available.
    if coffee_maker.is_resource_sufficient(drink):

        # Check whether the customer pays enough.
        if money_machine.make_payment(drink.cost):

            # Make the coffee after successful payment.
            coffee_maker.make_coffee(drink)