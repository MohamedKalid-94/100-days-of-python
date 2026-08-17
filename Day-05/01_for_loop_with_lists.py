# Topic: Using the for Loop with Python Lists

# 1. Basic For Loop with a List

fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)


# The variable "fruit" represents the current item.

# First iteration:  # fruit = "Apple"
# Second iteration: # fruit = "Banana"
# Third iteration:  # fruit = "Orange"

# 2. FOR LOOP WITH NUMBERS

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)

# 3. PERFORMING CALCULATIONS INSIDE A LOOP

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    square = number * number
    print(f"{number} squared = {square}")


# 4. ADDING VALUES INSIDE A LOOP
# We can use a variable to keep track of a running total.

numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

print("Total:", total)

# 5. FOR LOOP WITH STRINGS

name = "Python"

for letter in name:
    print(letter)


# Output:
#
# P
# y
# t
# h
# o
# n


# 6. FOR LOOP WITH CONDITIONS
# A for loop can be combined with if statements.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        print(number, "is even")

# 7. FINDING NUMBERS GREATER THAN A VALUE

scores = [45, 78, 92, 34, 88, 67]

for score in scores:
    if score >= 70:
        print(score, "is a good score")


# 8. MODIFYING VALUES DURING A LOOP

prices = [100, 200, 300, 400]

for price in prices:
    discounted_price = price * 0.9
    print("Original:", price, "Discounted:", discounted_price)


# 9. PRACTICAL EXAMPLE - TEMPERATURES

temperatures = [28, 31, 35, 29, 38]

for temperature in temperatures:
    if temperature >= 35:
        print(temperature, "°C - Hot")
    else:
        print(temperature, "°C - Normal")


# ============================================================
# 1. PRACTICAL EXAMPLE - STUDENT SCORES
# ============================================================

student_scores = [85, 72, 91, 64, 78]

for score in student_scores:
    if score >= 80:
        print(score, "- Excellent")
    elif score >= 60:
        print(score, "- Passed")
    else:
        print(score, "- Needs improvement")


# ============================================================
# 2. DEBUGGING EXERCISE - INDENTATION
# ============================================================

# Python uses indentation to determine which statements belong
# to the loop.
#
# Incorrect:
#
# for fruit in fruits:
# print(fruit)
#
# This causes an IndentationError.
#
# Correct:

fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print("Correct:", fruit)


# The code inside the loop must be indented.


# ============================================================
# 3. DEBUGGING EXERCISE - WRONG VARIABLE
# ============================================================

# Consider:
#
# fruits = ["Apple", "Banana", "Orange"]
#
# for fruit in fruits:
#     print(fruits)
#
# This prints the entire list during every iteration.
#
# If the intention is to print one fruit at a time,
# we should print the loop variable:

for fruit in fruits:
    print("One item:", fruit)


# ============================================================
# 4. DEBUGGING EXERCISE - TOTAL
# ============================================================

# Incorrect approach:
#
# numbers = [10, 20, 30]
#
# total = 0
#
# for number in numbers:
#     total = number
#
# print(total)
#
# This gives 30 instead of 60 because the previous value of
# total is overwritten every time.
#
# Correct approach:

numbers = [10, 20, 30]

total = 0

for number in numbers:
    total += number

print("Correct total:", total)


# ============================================================
# 5. LOOPING THROUGH A LIST OF NAMES
# ============================================================

names = ["Kalid", "Ahmed", "Rahman", "Arun"]

for name in names:
    print(f"Hello, {name}!")

# ============================================================
# 1. KEY TAKEAWAYS
# ============================================================

# Basic syntax:
#
# for item in list:
#     do_something()

# Important concepts:

# - for
# - in
# - list
# - loop variable
# - indentation
# - if inside a loop
# - calculations inside a loop
# - accumulating values

# The for loop is one of the most important tools in Python
# because it allows us to process collections of data
# efficiently.