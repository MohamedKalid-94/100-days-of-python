# ============================================================
# DAY 4 - RANDOMIZATION AND LISTS
# Topic: Random Module
# ============================================================

# The random module is a built-in Python module that allows us
# to generate random numbers and make random selections.
# To use it, we first need to import it.

import random
random_number = random.randint(1, 10)
print("Random number:", random_number)


# ============================================================
# 2. RANDOM FLOAT
# ============================================================

# random.random()
# Generates a random floating-point number between 0.0
# and 1.0.

random_float = random.random()
print("Random float:", random_float)


# ============================================================
# 3. RANDOM FLOAT WITH A RANGE
# ============================================================

# We can multiply random.random() by a number to create
# a larger range.

random_float_range = random.random() * 5
print("Random float between 0 and 5:", random_float_range)


# ============================================================
# 4. RANDOM CHOICE
# ============================================================

# random.choice() selects one random item from a sequence.
# A list is a common sequence that we can use.

friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
random_friend = random.choice(friends)
print("Randomly selected friend:", random_friend)

# Every time the program runs, a different friend may be selected.



# ============================================================
# 5. RANDOM BOOLEAN-LIKE DECISION
# ============================================================

# We can also use random numbers to make random decisions.

random_value = random.randint(0, 1)

if random_value == 1:
    print("Heads")
else:
    print("Tails")

# ============================================================
# 8. DEBUGGING EXERCISE
# ============================================================

# The following code contains a common mistake.
#
# Uncomment it and try to identify the problem.
#
# random_number = random.randint(1, 10)
# print("Number:", random_number)
#
# Question:
# What happens if we write:
#
# random_number = random.randint(10, 1)
#
# Think about why the starting value and ending value matter.

# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. import random
#    Imports Python's random module.
#
# 2. random.randint(1, 10)
#    Generates a random integer from 1 to 10.
#
# 3. random.random()
#    Generates a random float between 0 and 1.
#
# 4. random.choice(list)
#    Selects one random item from a list.
#
# These concepts will be combined with lists and conditional
# logic in the upcoming Day 4 exercises.