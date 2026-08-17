# Day 3 - Final Exercise
# Project: Treasure Island
#
# The goal of this project is to combine the control-flow
# concepts learned throughout Day 3.
#
# Concepts used:
# - input()
# - strings
# - if
# - elif
# - else
# - nested if statements
# - comparison operators
#
# The player must make decisions to find the treasure.

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

choice1 = input(
    "You are at a crossroad. "
    "Where do you want to go? "
    "Type 'left' or 'right': "
).lower()

if choice1 == "left":

    choice2 = input(
        "You have reached a lake. "
        "Type 'wait' to wait for a boat "
        "or 'swim' to swim across: "
    ).lower()

    if choice2 == "wait":

        choice3 = input(
            "You arrive at an island. "
            "There are three doors. "
            "Choose red, yellow or blue: "
        ).lower()

        if choice3 == "yellow":
            print("You found the treasure! You win!")

        elif choice3 == "red":
            print("You were burned by fire. Game Over.")

        elif choice3 == "blue":
            print("You were eaten by beasts. Game Over.")

        else:
            print("Invalid door. Game Over.")

    else:
        print("You were attacked. Game Over.")

else:
    print("You fell into a hole. Game Over.")


# ---------------------------------------------------------
# Exercise Challenge
# ---------------------------------------------------------
#
# After completing the basic version, try improving it.
#
# Possible improvements:
#
# 1. Add more paths.
# 2. Add additional choices.
# 3. Add a scoring system.
# 4. Add a restart option.
# 5. Add more endings.
#
# The goal is to practice control flow rather than simply
# copying the solution.
#
# This project brings together the major concepts from
# Day 3 into one interactive program.