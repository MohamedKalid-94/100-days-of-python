# Day 3 - Control Flow
# Topic: Multiple if Statements in Succession
#
# Multiple independent if statements are different
# from an if / elif / else structure.
#
# Every if condition is checked independently.

score = int(input("Enter your score: "))

if score >= 50:
    print("You passed.")

if score >= 75:
    print("Good performance.")

if score >= 90:
    print("Excellent performance.")


# ---------------------------------------------------------
# if / elif / else vs Multiple if
# ---------------------------------------------------------
#
# With if / elif / else:
# only one matching block is executed.
#
# With multiple if statements:
# several conditions can be True and several blocks
# can execute.

print("\nExample with multiple independent conditions:")

age = 25

if age >= 18:
    print("Adult")

if age >= 21:
    print("Above 21")

if age >= 25:
    print("25 or older")


# ---------------------------------------------------------
# Debugging Exercise
# ---------------------------------------------------------
#
# Consider this code:
#
# if score >= 50:
#     print("Pass")
# elif score >= 75:
#     print("Good")
#
# If score is 80, "Pass" is printed and the elif
# condition is never reached.
#
# When independent results are required, separate if
# statements may be more appropriate.