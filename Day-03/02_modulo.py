# Day 3 - Control Flow
# Topic: Modulo Operator
#
# The modulo operator (%) gives us the remainder
# after dividing one number by another.
#
# Example:
# 10 % 3 = 1
#
# Because:
# 10 / 3 = 3 remainder 1

number = 10

remainder = number % 3

print("Remainder:", remainder)


# ---------------------------------------------------------
# Checking Even and Odd Numbers
# ---------------------------------------------------------
#
# An even number is completely divisible by 2.
# Therefore, the remainder will be 0.
#
# If number % 2 == 0:
#     The number is even.
#
# Otherwise:
#     The number is odd.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# ---------------------------------------------------------
# Debugging Exercise
# ---------------------------------------------------------
#
# Find and fix the problem in the code below.
#
# The intention is to check whether the number is even.
#
# Original code:
#
# number = 8
#
# if number % 2 = 0:
#     print("Even")
#
# The comparison operator should be used correctly.

number = 8

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
