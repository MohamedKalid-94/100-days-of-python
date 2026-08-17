# Day 3 - Control Flow
# Pizza Order Practice
#
# This exercise combines:
# - input()
# - if / elif / else
# - nested if
# - multiple if
# - arithmetic operations
# - string comparison

print("Welcome to Python Pizza!")

size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()


# ---------------------------------------------------------
# Calculate Base Price
# ---------------------------------------------------------

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Invalid pizza size.")


# ---------------------------------------------------------
# Add Pepperoni
# ---------------------------------------------------------
#
# The pepperoni price depends on the pizza size.
# This is an example of a nested if statement.

if pepperoni == "Y":

    if size == "S":
        bill += 2
    else:
        bill += 3


# ---------------------------------------------------------
# Add Extra Cheese
# ---------------------------------------------------------

if extra_cheese == "Y":
    bill += 1


print("Your final bill is:", bill)


# ---------------------------------------------------------
# Debugging Exercise
# ---------------------------------------------------------
#
# Common mistakes:
#
# 1. Forgetting to initialize bill.
# 2. Using = instead of == when comparing values.
# 3. Forgetting to convert the user's input to uppercase.
# 4. Adding the wrong pepperoni price.
# 5. Forgetting += when adding an extra charge.
#
# Example:
#
# bill += 1
#
# means:
#
# bill = bill + 1
