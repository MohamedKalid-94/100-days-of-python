# ============================================================
# Project: Password Generator
# ============================================================

import random


# ============================================================
# DAY 5 FINAL PROJECT
# ============================================================

# This project combines the concepts learned during Day 5:
#
# - Lists
# - for loops
# - range()
# - random.choice()
# - Strings
# - User input

# The user chooses how many:
#
# - Letters
# - Symbols
# - Numbers
#
# should be included in the password.


# ============================================================
# 1. CHARACTER DATA
# ============================================================

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z"
]

numbers = [
    "0", "1", "2", "3", "4",
    "5", "6", "7", "8", "9"
]

symbols = [
    "!", "#", "$", "%", "&", "(", ")", "*", "+"
]


# ============================================================
# 2. DISPLAY THE AVAILABLE OPTIONS
# ============================================================

print("Welcome to the Password Generator!")

# ============================================================
# 3. GET USER REQUIREMENTS
# ============================================================

nr_letters = int(input("How many letters would you like? "))

nr_symbols = int(input("How many symbols would you like? "))

nr_numbers = int(input("How many numbers would you like? "))


# ============================================================
# 4. CREATE AN EMPTY PASSWORD LIST
# ============================================================

# We start with an empty list.
#
# Characters will be added to this list during the loops.

password = []


# ============================================================
# 5. GENERATE RANDOM LETTERS
# ============================================================

for character in range(nr_letters):

    random_letter = random.choice(letters)

    password.append(random_letter)


# ============================================================
# 6. GENERATE RANDOM SYMBOLS
# ============================================================

for character in range(nr_symbols):

    random_symbol = random.choice(symbols)

    password.append(random_symbol)


# ============================================================
# 7. GENERATE RANDOM NUMBERS
# ============================================================

for character in range(nr_numbers):

    random_number = random.choice(numbers)

    password.append(random_number)


# ============================================================
# 8. DISPLAY THE PASSWORD BEFORE SHUFFLING
# ============================================================

print("Password before shuffling:", password)


# At this point, the password follows the order:
#
# Letters
# Symbols
# Numbers
#
# Example:
#
# abc!#$123
#
# This is not ideal because the character types appear in
# predictable groups.


# ============================================================
# 9. SHUFFLE THE PASSWORD
# ============================================================

random.shuffle(password)

print("Shuffled password:", password)


# random.shuffle() changes the order of the items in the list.


# ============================================================
# 10. CONVERT THE LIST INTO A STRING
# ============================================================

# The password is currently stored as a list.
#
# Example:
#
# ["a", "B", "#", "7", "!"]
#
# We want:
#
# "aB#7!"
#
# join() combines the list items into one string.

final_password = "".join(password)

print("Your password is:", final_password)


# ============================================================
# 1. DEBUGGING EXERCISE - FORGETTING APPEND
# ============================================================

# Incorrect:
#
# for character in range(nr_letters):
#     random_letter = random.choice(letters)
#
# The random letter is generated but never stored.
#
# Correct:
#
# for character in range(nr_letters):
#     random_letter = random.choice(letters)
#     password.append(random_letter)


# ============================================================
# 2. DEBUGGING EXERCISE - WRONG RANGE
# ============================================================

# Incorrect:
#
# for character in range(nr_letters - 1):
#     ...
#
# This generates one character fewer than requested.
#
# Correct:
#
# for character in range(nr_letters):
#     ...


# ============================================================
# 3. DEBUGGING EXERCISE - PASSWORD AS STRING
# ============================================================

# We use a list while building the password because lists
# are easy to modify.
#
# Example:
#
# password = []
# password.append("A")
# password.append("!")
#
# Then we convert it into a string:
#
# final_password = "".join(password)


# ============================================================
# 4. TESTING THE PASSWORD GENERATOR
# ============================================================

# Example input:
#
# Letters: 5
# Symbols: 2
# Numbers: 3
#
# Total characters:
#
# 5 + 2 + 3 = 10
#
# The final password should contain exactly 10 characters.


# ============================================================
# 5. VERIFY PASSWORD LENGTH
# ============================================================

expected_length = nr_letters + nr_symbols + nr_numbers

actual_length = len(final_password)

print("Expected password length:", expected_length)
print("Actual password length:", actual_length)


if expected_length == actual_length:
    print("Password length verified.")
else:
    print("Password length error.")


# ============================================================
# 6. DAY 5 CONCEPTS USED
# ============================================================

# This project demonstrates:
#
# Lists
# for loops
# range()
# random.choice()
# random.shuffle()
# append()
# join()
# len()
# User input
# int()
# Variables
#
# The project combines multiple individual concepts into one
# working application.


# ============================================================
# 7. KEY TAKEAWAYS
# ============================================================

# The Password Generator demonstrates why loops are useful.
#
# Instead of manually writing:
#
# password.append(random.choice(letters))
# password.append(random.choice(letters))
# password.append(random.choice(letters))
#
# we can use:
#
# for character in range(nr_letters):
#     password.append(random.choice(letters))
#
# The loop automatically repeats the operation the required
# number of times.
#
# This is one of the main reasons loops are fundamental in
# programming.