# Day 16 - Object-Oriented Programming
# Step 02: Understanding self
#
# Topics:
# - self
# - Multiple objects
# - Object-specific attributes
# - Calling methods


class Dog:

    def __init__(self, name):
        # self refers to the current object.
        self.name = name

    def bark(self):
        # self.name accesses the name belonging
        # to the current object.
        print(f"{self.name} says: Woof!")


# Create two different Dog objects.
dog_1 = Dog("Bruno")
dog_2 = Dog("Rocky")


# Call the same method on two different objects.
dog_1.bark()
dog_2.bark()