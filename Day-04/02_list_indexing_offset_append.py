# ============================================================
# Topic: Lists, Indexing, Offset and Appending Items
# ============================================================

# ============================================================
# 1. CREATING A LIST
# ============================================================

# A list allows us to store multiple values in a single variable.
fruits = ["Apple", "Banana", "Orange", "Mango"]
print("Fruits:", fruits)

# ============================================================
# 2. ACCESSING ITEMS USING INDEX
# ============================================================

print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Third fruit:", fruits[2])
print("Fourth fruit:", fruits[3])


# ============================================================
# 3. UNDERSTANDING THE OFFSET
# ============================================================

# Humans normally count:
#
# 1st → Apple
# 2nd → Banana
# 3rd → Orange
# 4th → Mango
#
# Python counts:
#
# 0 → Apple
# 1 → Banana
# 2 → Orange
# 3 → Mango
#
# This difference is called an offset.
#
# The first position has an index of 0, not 1.


# ============================================================
# 4. NEGATIVE INDEXING
# ============================================================

# Python also allows us to access items from the end
# of the list using negative indexes.

# -1 → last item
# -2 → second-last item
# -3 → third-last item

print("Last fruit:", fruits[-1])
print("Second-last fruit:", fruits[-2])


# ============================================================
# 5. CHANGING A LIST ITEM
# ============================================================

fruits[1] = "Strawberry"
print("Updated fruits:", fruits)

# ============================================================
# 6. APPENDING AN ITEM
# ============================================================

# append() adds a new item to the end of a list.
fruits.append("Grapes")
print("After append:", fruits)

# ============================================================
# 7. APPENDING MULTIPLE ITEMS
# ============================================================

fruits.append("Watermelon")
fruits.append("Pineapple")
print("Final fruit list:", fruits)

# ============================================================
# 8. LIST LENGTH
# ============================================================

# len() tells us how many items are inside a list.
number_of_fruits = len(fruits)
print("Number of fruits:", number_of_fruits)


# ============================================================
# 9. PRACTICAL EXAMPLE
# ============================================================

# Imagine we are storing programming languages.
languages = ["Python", "C", "C++"]
print("First language:", languages[0])
languages.append("Java")
print("Languages:", languages)


# ============================================================
# 10. LIST WITH NUMBERS
# ============================================================

scores = [10, 20, 30, 40]
print("First score:", scores[0])
print("Last score:", scores[-1])

scores.append(50)
print("Updated scores:", scores)


# ============================================================
# 11. DEBUGGING EXERCISE - INDEXERROR
# ============================================================

# The following example would cause an IndexError:
#
# numbers = [10, 20, 30]
# print(numbers[3])
#
# Why?
#
# Valid indexes are:
#
# 0 → 10
# 1 → 20
# 2 → 30
#
# Index 3 does not exist.


# ============================================================
# 12. DEBUGGING EXERCISE - FIX THE INDEX
# ============================================================

numbers = [10, 20, 30]

# Incorrect:
#
# print(numbers[3])
#
# Correct:
#
print("Last number:", numbers[2])


# ============================================================
# 13. DEBUGGING EXERCISE - APPEND
# ============================================================

# append() adds exactly one item to the list.

animals = ["Dog", "Cat"]
animals.append("Horse")
print("Animals:", animals)

# ============================================================
# 14. PRACTICE CHALLENGE
# ============================================================

# Create a list containing three of your favourite movies.
# Then:
#
# 1. Print the first movie.
# 2. Print the last movie.
# 3. Add another movie using append().
# 4. Print the final list.
#
# Example:

movies = ["Movie A", "Movie B", "Movie C"]

print("First movie:", movies[0])
print("Last movie:", movies[-1])
movies.append("Movie D")
print("Updated movies:", movies)


# ============================================================
# 15. KEY TAKEAWAYS
# ============================================================

# Lists:
#
# items = ["A", "B", "C"]
#
# Indexing:
#
# items[0] → "A"
# items[1] → "B"
# items[2] → "C"
#
# Negative indexing: # items[-1] → "C"
# Append:            # items.append("D")
# Length:            # len(items)
