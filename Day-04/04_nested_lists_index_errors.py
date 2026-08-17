# Topic: Nested Lists and IndexErrors

# 1. BASIC LIST
# A normal list can contain several values.

fruits = ["Apple", "Banana", "Orange"]
print("Fruits:", fruits)

# 2. NESTED LIST
# A nested list is a list that contains other lists.

fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Potato", "Tomato"]
food = [fruits, vegetables]
print("Food:", food)


# The structure is:
#
# food
# ├── fruits
# │   ├── Apple
# │   ├── Banana
# │   └── Orange
# │
# └── vegetables
#     ├── Carrot
#     ├── Potato
#     └── Tomato


# 3. ACCESSING A NESTED LIST

# food[0] gives us the first nested list.
print("First nested list:", food[0])
# food[1] gives us the second nested list.
print("Second nested list:", food[1])

# 4. ACCESSING AN ITEM INSIDE A NESTED LIST

# We can use two indexes.
# First index → selects the nested list.
# Second index → selects an item inside that list.

print("First fruit:", food[0][0])
print("Second fruit:", food[0][1])
print("First vegetable:", food[1][0])
print("Second vegetable:", food[1][1])


# Example:
#
# food[0][1]
#
# food[0]    → fruits
# [1]        → Banana

# 5. NESTED LIST WITH NUMBERS

scores_team_a = [10, 20, 30]
scores_team_b = [40, 50, 60]

scores = [scores_team_a, scores_team_b]

print("Scores:", scores)

print("Team A first score:", scores[0][0])
print("Team B first score:", scores[1][0])


# 6. INDEXERROR
numbers = [10, 20, 30]

print("Valid index 0:", numbers[0])
print("Valid index 1:", numbers[1])
print("Valid index 2:", numbers[2])


# The following would cause an IndexError:
# print(numbers[3])
# The list has three items.

# Valid indexes:
#
# 0
# 1
# 2
#
# Index 3 does not exist.


# 7. UNDERSTANDING len() WITH LISTS
numbers = [10, 20, 30]
print("Number of items:", len(numbers))
last_index = len(numbers) - 1
print("Last index:", last_index)

# 8. INDEXERROR WITH NESTED LISTS
# Nested lists can have their own indexes.

players = [
    ["Alice", "Bob"],
    ["Charlie", "David"]
]

print("Players:", players)

print("First team:", players[0])
print("Second team:", players[1])

print("First player of Team 1:", players[0][0])
print("Second player of Team 1:", players[0][1])

print("First player of Team 2:", players[1][0])
print("Second player of Team 2:", players[1][1])


# 9. DEBUGGING NESTED LISTS

# Consider:
#
# players = [
#     ["Alice", "Bob"],
#     ["Charlie", "David"]
# ]
#
# What happens here?
#
# players[2]
#
# There are only two nested lists.
#
# Valid indexes:
#
# 0 → ["Alice", "Bob"]
# 1 → ["Charlie", "David"]
#
# Index 2 does not exist.


# 10. CORRECTING THE ERROR

players = [
    ["Alice", "Bob"],
    ["Charlie", "David"]
]

# Incorrect:
#
# print(players[2])
#
# Correct:

print("Second team:", players[1])

# 11. DEBUGGING INNER INDEXES

# There is another possible IndexError.
# Example:
# players[0][2]
# players[0] contains:
# ["Alice", "Bob"]
# Valid inner indexes:
# 0 → Alice
# 1 → Bob
# Index 2 does not exist.

# Correct:
print("Second player of Team 1:", players[0][1])

# 12. MODIFYING A NESTED LIST

players = [
    ["Alice", "Bob"],
    ["Charlie", "David"]
]

players[0][1] = "Eve"
print("Updated players:", players)

# The list is now:
#
# [
#     ["Alice", "Eve"],
#     ["Charlie", "David"]
# ]


# 13. APPENDING TO A NESTED LIST

players[0].append("Frank")
print("After adding player:", players)


# 14. PRACTICE CHALLENGE

# Create a nested list containing two teams.
# Each team should contain three players.

# Then:
# 1. Print the first player of Team 1.
# 2. Print the last player of Team 2.
# 3. Add another player to Team 1.
# 4. Print the updated structure.

team_a = ["Player A1", "Player A2", "Player A3"]
team_b = ["Player B1", "Player B2", "Player B3"]

teams = [team_a, team_b]

print("Team 1 first player:", teams[0][0])
print("Team 2 last player:", teams[1][-1])

teams[0].append("Player A4")

print("Updated teams:", teams)


# 15. DEBUGGING CHECKLIST

# When you see an IndexError:
# 1. Check the list.
# 2. Count how many items it contains.
# 3. Remember that indexing starts from 0.
# 4. Find the highest valid index.
# 5. For nested lists, check BOTH indexes.

# Example:
# list[outer_index][inner_index]

# Check:
# - Does outer_index exist?
# - Does inner_index exist inside that nested list?


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# Nested list:
#
# teams = [
#     ["A", "B"],
#     ["C", "D"]
# ]
#
# teams[0]
#     → ["A", "B"]
#
# teams[0][1]
#     → "B"
#
# IndexError happens when an index is outside the valid range.
#
# Always remember:
#
# First item → index 0
# Last index → len(list) - 1