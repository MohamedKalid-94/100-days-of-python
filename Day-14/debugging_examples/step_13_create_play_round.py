#Step 13 — Create play_round()
#At this point we had several separate pieces.
#We combined one complete round into:

def play_round():
    account_a = get_random_account()
    account_b = get_random_account(account_a)


    display_account(account_a, "A")
    display_account(account_b, "B")


    choice = get_valid_choice()


    correct_answer = compare_followers(
        account_a,
        account_b
    )


    if choice == correct_answer:
        print("You're right!")
        return True
    else:
        print("You're wrong!")
        return False

#This was a major step.
#play_round() now controls one complete game round.