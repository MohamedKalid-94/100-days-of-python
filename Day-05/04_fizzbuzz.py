# ============================================================
# Topic: Coding Exercise 6 - FizzBuzz
# ============================================================


# ============================================================
# 1. WHAT IS FIZZBUZZ?
# ============================================================

# FizzBuzz is a common programming exercise used to practice:
#
# - for loops
# - range()
# - if / elif / else
# - modulo operator (%)
# - logical conditions


# ============================================================
# 2. THE RULES
# ============================================================

# For every number from 1 to 100:
#
# If the number is divisible by 3:
#     Print "Fizz"
#
# If the number is divisible by 5:
#     Print "Buzz"
#
# If the number is divisible by both 3 and 5:
#     Print "FizzBuzz"
#
# Otherwise:
#     Print the number.

# ============================================================
# 3. BASIC FIZZBUZZ
# ============================================================

for number in range(1, 101):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)


# ============================================================
# 4. WHY FIZZBUZZ MUST BE CHECKED FIRST
# ============================================================

# Numbers such as 15 are divisible by BOTH 3 and 5.
#
# If we check only:
#
# if number % 3 == 0:
#     print("Fizz")
#
# then 15 would print "Fizz" and we would never reach
# the "FizzBuzz" condition.
#
# Therefore, the combined condition must be checked first.

# ============================================================
# 5. LOGIC TABLE
# ============================================================

# Number divisible by 3 | Divisible by 5 | Result
#
# No  | No  → Number
# Yes | No  → Fizz
# No  | Yes → Buzz
# Yes | Yes → FizzBuzz

# ============================================================
# 6. KEY TAKEAWAYS
# ============================================================

# FizzBuzz combines several important concepts:
#
# for loops
# range()
# modulo %
# if / elif / else
# logical AND
#
# The most important logic is:
#
# if number % 3 == 0 and number % 5 == 0:
#     "FizzBuzz"
#
# elif number % 3 == 0:
#     "Fizz"
#
# elif number % 5 == 0:
#     "Buzz"
#
# else:
#     number