import random


data = [
    {
        "name": "Instagram",
        "followers": 1000000,
        "description": "Social media platform",
        "country": "USA"
    },
    {
        "name": "FB",
        "followers": 100000,
        "description": "Social media platform",
        "country": "UK"
    },
    {
        "name": "Twitter",
        "followers": 10000,
        "description": "Social media platform",
        "country": "UAE"
    },
    {
        "name": "LinkedIn",
        "followers": 1000000,
        "description": "Professional networking platform",
        "country": "USA"
    }
]


VALID_CHOICES = ["A", "B", "T"]
MAX_SCORE = 5


def compare_followers(account_a, account_b):
    """Compare follower counts and return A, B, or T."""
    if account_a["followers"] > account_b["followers"]:
        return "A"
    elif account_b["followers"] > account_a["followers"]:
        return "B"
    else:
        return "T"


def get_random_account(exclude=None):
    """Return a random account different from the excluded account."""
    account = random.choice(data)

    while account == exclude:
        account = random.choice(data)

    return account


def display_account(account, label):
    """Display account information."""
    print(f"{label}: {account['name']}")
    print(f"{account['description']} from {account['country']}")


def get_valid_choice():
    """Ask the user for a valid A, B, or T choice."""
    while True:
        choice = input(
            "Who has more followers? A, B or T: "
        ).upper()

        if choice in VALID_CHOICES:
            return choice

        print("Invalid choice. Please enter A, B or T.")


def play_round():
    """Play one round and return True for correct, False for wrong."""
    account_a = get_random_account()
    account_b = get_random_account(account_a)

    display_account(account_a, "A")
    display_account(account_b, "B")

    choice = get_valid_choice()

    correct_answer = compare_followers(account_a, account_b)

    if choice == correct_answer:
        if correct_answer == "T":
            print("It's a tie! You're right!")
        else:
            print("You're right!")

        return True

    print("You're wrong!")
    return False


def run_game():
    """Run the game and keep track of the score."""
    score = 0

    while True:
        result = play_round()

        if result:
            score += 1
            print("Score:", score)

            if score >= MAX_SCORE:
                print("Congratulations! You reached the maximum score.")
                break

        else:
            print("Final Score:", score)
            break


run_game()