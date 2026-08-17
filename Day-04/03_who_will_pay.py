# ============================================================
# Topic: Who Will Pay the Bill?
# ============================================================

import random

# 1. CREATING A LIST OF FRIENDS
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
print("Friends:", friends)

# 2. ACCESSING ITEMS USING INDEX
print("First friend:", friends[0])
print("Second friend:", friends[1])
print("Last friend:", friends[-1])

# 3. RANDOMLY SELECTING A FRIEND
payer = random.choice(friends)
print("The person who will pay the bill is:", payer)

# Every time we run the program, a different friend may be selected.

# 4. PRACTICAL EXAMPLE
friends = ["Kalid", "Ahmed", "Rahman", "Arun", "Karthik"]
payer = random.choice(friends)
print(f"{payer} will pay the bill!")


# 5. USING random.randint()
random_index = random.randint(0, len(friends) - 1)
payer = friends[random_index]
print("Randomly selected payer:", payer)

# 6. UNDERSTANDING len()

number_of_friends = len(friends)
print("Number of friends:", number_of_friends)

# 7. ADDING A NEW FRIEND

friends.append("Sanjay")
print("Updated friends:", friends)
payer = random.choice(friends)
print(f"{payer} will pay the bill!")


# ============================================================
# 10. MINI CHALLENGE
# ============================================================

# Create a list containing the names of five people.
#
# Then randomly select one person to:
#
# - Buy dinner
# - Bring snacks
# - Choose the movie
#
# Example:

people = ["Person 1", "Person 2", "Person 3", "Person 4", "Person 5"]

dinner_payer = random.choice(people)

print(f"{dinner_payer} will buy dinner.")


# ============================================================
# 11. DAY 4 CONCEPT CONNECTION
# ============================================================

# This exercise combines:
#
# - Lists
# - List indexing
# - len()
# - random.randint()
# - random.choice()
# - append()
#
# These concepts will also be useful in the final
# Rock Paper Scissors project.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# random.choice(list)
#     → Selects one random item from a list.
#
# len(list)
#     → Returns the number of items.
#
# list.append(item)
#     → Adds an item to the end of a list.
#
# list[index]
#     → Accesses an item using its index.
#
# Important:
#     Number of items and the last index are different.
