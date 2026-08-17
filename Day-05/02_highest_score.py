# ============================================================
# Topic: Highest Score
# ============================================================


# ============================================================
# 1. THE PROBLEM
# ============================================================

# Suppose we have a list of student scores.
#
# We want to find the highest score without using Python's
# built-in max() function.
#
# This is useful practice for understanding how a for loop
# can process every item in a list.

student_scores = [78, 65, 89, 91, 72, 95, 84]
print("Student scores:", student_scores)


# ============================================================
# 2. START WITH A LOW HIGHEST SCORE
# ============================================================

# We create a variable to keep track of the highest score
# found so far.

highest_score = 0

for score in student_scores:

    if score > highest_score:
        highest_score = score

print("Highest score:", highest_score)

# ============================================================
# 3. USING NEGATIVE SCORES
# ============================================================

# Starting with 0 only works correctly if we know all scores
# are positive.
#
# Consider:

scores = [-10, -20, -5, -30]

highest_score = 0

for score in scores:
    if score > highest_score:
        highest_score = score

print("Incorrect approach for negative values:", highest_score)


# The answer should actually be -5.
#
# Starting with 0 caused the problem because 0 is greater
# than every value in the list.


# ============================================================
# 4. BETTER INITIALIZATION
# ============================================================

# A safer approach is to start with the first item in the list.

scores = [-10, -20, -5, -30]

highest_score = scores[0]

for score in scores:
    if score > highest_score:
        highest_score = score

print("Correct highest score:", highest_score)


# ============================================================
# 5. WHY scores[0]?
# ============================================================

# scores[0] gives us the first item in the list.
#
# We then compare every other score against it.
#
# This makes the algorithm work even when the values are
# negative.


# ============================================================
# 6. PRACTICAL EXAMPLE - EXAM SCORES
# ============================================================

exam_scores = [67, 88, 92, 76, 95, 81]

highest_exam_score = exam_scores[0]

for score in exam_scores:
    if score > highest_exam_score:
        highest_exam_score = score

print("Highest exam score:", highest_exam_score)


# ============================================================
# 7. PRACTICAL EXAMPLE - PLAYER SCORES
# ============================================================

player_scores = [120, 450, 320, 875, 640, 210]

highest_player_score = player_scores[0]

for score in player_scores:
    if score > highest_player_score:
        highest_player_score = score

print("Highest player score:", highest_player_score)


# ============================================================
# 8. DEBUGGING EXERCISE - WRONG COMPARISON
# ============================================================

# Consider:
#
# scores = [50, 80, 70, 90]
#
# highest_score = scores[0]
#
# for score in scores:
#     if score < highest_score:
#         highest_score = score
#
# This finds the LOWEST score instead of the highest.
#
# For the highest score we need:
#
# if score > highest_score:


# ============================================================
# 9. DEBUGGING EXERCISE - OVERWRITING THE VALUE
# ============================================================

# Incorrect:
#
# scores = [50, 80, 70, 90]
#
# highest_score = scores[0]
#
# for score in scores:
#     highest_score = score
#
# print(highest_score)
#
# This simply replaces highest_score with every value.
#
# The final value would be 90 only because 90 happens to be
# the last item.
#
# It would fail if the highest value appeared earlier.


# Correct:

scores = [50, 95, 70, 80]

highest_score = scores[0]

for score in scores:
    if score > highest_score:
        highest_score = score

print("Correct highest score:", highest_score)


# ============================================================
# 10. PRACTICE CHALLENGE
# ============================================================

# Find the highest number from the following list without
# using max().

numbers = [34, 78, 12, 99, 45, 67, 23]

highest_number = numbers[0]

for number in numbers:
    if number > highest_number:
        highest_number = number

print("Highest number:", highest_number)


# ============================================================
# 1. KEY TAKEAWAYS
# ============================================================

# The general pattern for finding the highest value is:
#
# highest = list[0]
#
# for item in list:
#     if item > highest:
#         highest = item
#
# This is an important programming pattern.
#
# We are not relying on a built-in function.
#
# Instead, we are understanding the logic behind finding
# the maximum value.