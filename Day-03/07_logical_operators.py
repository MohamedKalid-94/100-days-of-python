# Day 3 - Logical Operators
#
# Python provides three important logical operators:
#
# and
# or
# not
#
# They allow us to combine multiple conditions.

# ---------------------------------------------------------
# AND
# ---------------------------------------------------------
#
# With AND, all conditions must be True.

age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive.")


# ---------------------------------------------------------
# OR
# ---------------------------------------------------------
#
# With OR, at least one condition must be True.

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It is the weekend.")


# ---------------------------------------------------------
# NOT
# ---------------------------------------------------------
#
# NOT reverses a Boolean value.

is_raining = False

if not is_raining:
    print("You can go outside.")


# ---------------------------------------------------------
# Combining Logical Operators
# ---------------------------------------------------------

age = 25
has_ticket = True
is_vip = False

if age >= 18 and (has_ticket or is_vip):
    print("Entry allowed.")
else:
    print("Entry denied.")


# ---------------------------------------------------------
# Debugging Exercise
# ---------------------------------------------------------
#
# Carefully check the following conditions.
#
# 1. AND requires both conditions to be True.
# 2. OR requires at least one condition to be True.
# 3. NOT reverses the Boolean result.
#
# Example:
#
# True and False → False
# True or False  → True
# not True       → False


# ---------------------------------------------------------
# Key Learning
# ---------------------------------------------------------
#
# Logical operators allow multiple conditions to be
# combined into a single decision.