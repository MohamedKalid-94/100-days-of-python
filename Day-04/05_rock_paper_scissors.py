# Project: Rock Paper Scissors

import random

# 1. CREATE THE CHOICES
# We use a list to store the three possible choices.

choices = ["Rock", "Paper", "Scissors"]

print("Available choices:")
print(choices)


# 2. GET THE PLAYER'S CHOICE
player_choice = int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissors: "))

# 3. VALIDATE THE PLAYER'S CHOICE
if player_choice not in [0, 1, 2]:
    print("Invalid choice.")
    exit()

player_choice_name = choices[player_choice]
print("You chose:", player_choice_name)

# 4. COMPUTER CHOICE
computer_choice = random.choice(choices)
print("Computer chose:", computer_choice)

# 5. DETERMINE THE RESULT
if player_choice_name == computer_choice:
    print("It's a Draw!")

elif player_choice_name == "Rock" and computer_choice == "Scissors":
    print("You Win!")

elif player_choice_name == "Scissors" and computer_choice == "Paper":
    print("You Win!")

elif player_choice_name == "Paper" and computer_choice == "Rock":
    print("You Win!")

else:
    print("Computer Wins!")

# 6. ANOTHER WAY TO SELECT THE COMPUTER'S CHOICE

# Instead of:
# computer_choice = random.choice(choices)
# we could generate a random index:

computer_index = random.randint(0, 2)
computer_choice_using_index = choices[computer_index]
print("Another random computer choice:", computer_choice_using_index)


# random.choice() is simpler when we only need a random item.
# random.randint() is useful when we specifically need
# a random number or index.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# The Rock Paper Scissors project combines the major
# Day 4 concepts:
#
# 1. Lists
# 2. Indexing
# 3. Random selection
# 4. Input
# 5. Conditional logic
# 6. Error prevention
#
# The important lesson is not just building the game.
#
# The important lesson is understanding how:
#
#     List
#       +
#     Indexing
#       +
#     Randomization
#       +
#     Conditional Logic
#
# can be combined to create a working program.