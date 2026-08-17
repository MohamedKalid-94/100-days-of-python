# ============================================================
# Topic: for Loops and the range() Function
# ============================================================


# ============================================================
# 1. WHAT IS range()?
# ============================================================
for number in range(5):
    print(number)

# ============================================================
# 2. range(start, stop)
# ============================================================
# We can specify where the range should start.

for number in range(1, 6):
    print(number)

# ============================================================
# 3. range() WITH A STEP
# ============================================================

for number in range(1, 11, 2):
    print(number)

# ============================================================
# 4. COUNTING BY 2
# ============================================================

for number in range(2, 11, 2):
    print(number)

# ============================================================
# 5. COUNTING BY 5
# ============================================================

for number in range(5, 31, 5):
    print(number)

# ============================================================
# 6. COUNTING BACKWARDS
# ============================================================

for number in range(10, 0, -1):
    print(number)

# ============================================================
# 7. range() WITH CALCULATIONS
# ============================================================

for number in range(1, 6):
    square = number ** 2
    print(number, "squared =", square)

# ============================================================
# 8. SUMMING NUMBERS
# ============================================================

total = 0

for number in range(1, 11):
    total += number

print("Sum from 1 to 10:", total)


# ============================================================
# 9. MULTIPLICATION TABLE
# ============================================================

number = 5

for multiplier in range(1, 11):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")


# ============================================================
# 10. RANGE AND LIST INDEXES
# ============================================================

# range() can also be used to access list indexes.

fruits = ["Apple", "Banana", "Orange", "Mango"]

for index in range(len(fruits)):
    print(index, fruits[index])

# ============================================================
# 11. FOR LOOP VS range()
# ============================================================

# When we need the actual items:

for fruit in fruits:
    print(fruit)


# When we need the indexes:

for index in range(len(fruits)):
    print(index, fruits[index])


# ============================================================
# 12. KEY TAKEAWAYS
# ============================================================

# range(stop)
#     Starts at 0 and stops before stop.
#
# range(start, stop)
#     Starts at start and stops before stop.
#
# range(start, stop, step)
#     Allows us to control the increment.
#
# Examples:
#
# range(5)
# range(1, 6)
# range(1, 11, 2)
# range(10, 0, -1)
#
# The most important rule:
# The STOP value is NOT included.
# Understanding this prevents many off-by-one errors.