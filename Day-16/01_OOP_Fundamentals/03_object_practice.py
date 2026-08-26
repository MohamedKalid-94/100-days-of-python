# Day 16 - Object-Oriented Programming
# Step 03: Modifying Object Attributes
#
# Topics:
# - Object attributes
# - Methods
# - Modifying object state
# - Calling methods
# - Direct attribute modification


class Car:

    def __init__(self, brand, speed):
        # Store the car's initial data.
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        # Increase the speed by 10 km/h.
        self.speed += 10

        print(
            f"{self.brand} is now going at {self.speed} km/h."
        )

    def brake(self):
        # Decrease the speed by 10 km/h.
        self.speed -= 10

        print(
            f"{self.brand} is now going at {self.speed} km/h."
        )


# Create a Car object.
my_car = Car("Toyota", 50)

# Access object attributes.
print(my_car.brand)
print(my_car.speed)

print()

# Modify object state using a method.
my_car.accelerate()
my_car.accelerate()

print()

my_car.brake()

print()

# Directly modify an object attribute.
my_car.speed = 100

print(
    f"Manually changed speed to {my_car.speed} km/h."
)