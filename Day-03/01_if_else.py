# Day 3 - Control Flow
# Topic: if / else and Conditional Operators

# In Day 3, we start making decisions in our programs.

# The if statement checks whether a condition is True.
# If it is True, the code inside the if block runs.
# Otherwise, the else block runs.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# ---------------------------------------------------------
# Comparison Operators
# ---------------------------------------------------------
#
# Python provides comparison operators to compare values:
#
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to
# ==  Equal to
# !=  Not equal to
#
# The result of a comparison is either True or False.

number = 10

if number > 5:
    print("Number is greater than 5")

if number == 10:
    print("Number is equal to 10")

if number != 20:
    print("Number is not equal to 20")


# ---------------------------------------------------------
# Conditional Operators
# ---------------------------------------------------------
#
# Conditions can be combined with if / else to control
# how the program behaves.

temperature = 30

if temperature > 25:
    print("It is a hot day.")
else:
    print("It is not a hot day.")
