# Example 1: NameError
#
# name = "Mohamed"
# print(nam)
#
# Problem:
# The variable is called "name", not "nam".


# Example 2: TypeError
#
# age = 32
# print("My age is " + age)
#
# Problem:
# You cannot directly combine a string and an integer using +.
#
# Correct:
age = 32

print("My age is " + str(age))


# Example 3: ValueError
#
# age = int("hello")
#
# Problem:
# "hello" cannot be converted into an integer.


# Example 4: SyntaxError
#
# print("Hello"
#
# Problem:
# The closing parenthesis is missing.