#Step 12 — Validate user input
#We didn't want the user entering:

#123
#hello
#XYZ
#and breaking the game logic.

#So we created:

VALID_CHOICES = ["A", "B", "T"]

#Then:

def get_valid_choice():
    while True:
        choice = input("Who has more followers? A, B or T: ").upper()

        if choice in VALID_CHOICES:
            return choice
        print("Invalid choice. Please enter A, B or T.")

#Now invalid input causes the program to ask again.