# Day 16 - Object-Oriented Programming
# Step 01: Classes and Objects
#
# Topics:
# - Classes
# - Objects
# - __init__()
# - Attributes
# - Methods


# A class is a blueprint for creating objects.
class User:

    def __init__(self, name, age):
        # Store data inside the object.
        self.name = name
        self.age = age

    def introduce(self):
        # Access the object's attributes using self.
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")

    def have_birthday(self):
        # Modify the object's age.
        self.age += 1

        print(f"Happy birthday, {self.name}!")
        print(f"You are now {self.age} years old.")


# Create a User object.
user_1 = User("Mohamed", 32)

# Display the initial object state.
user_1.introduce()

print()

# Call a method that changes the object's state.
user_1.have_birthday()

print()

# Display the updated object state.
user_1.introduce()