# Day 3 - Control Flow
# Topic: Nested if Statements and elif
#
# A nested if statement is an if statement
# placed inside another if statement.
#
# elif allows us to check multiple conditions.

age = int(input("Enter your age: "))

if age >= 18:

    has_license = input("Do you have a driving license? Y/N: ").upper()

    if has_license == "Y":
        print("You can drive.")
    else:
        print("You need a driving license.")

else:
    print("You are too young to drive.")


# ---------------------------------------------------------
# elif Example
# ---------------------------------------------------------
#
# elif means "else if".
#
# Python checks the conditions from top to bottom.
# Once a condition is True, its block is executed.

score = int(input("Enter your score: "))

if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Fail")


# ---------------------------------------------------------
# Debugging Exercise
# ---------------------------------------------------------
#
# The following program contains a logic problem.
#
# Think about what happens when the user enters 95.
#
# Incorrect logic:
#
# if score >= 50:
#     print("Grade C")
# elif score >= 75:
#     print("Grade B")
# elif score >= 90:
#     print("Grade A")
#
# The conditions must be arranged from the highest
# threshold to the lowest threshold.

score = 95

if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Fail")