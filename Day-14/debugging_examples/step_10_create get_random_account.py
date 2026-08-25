#Step 10 — Create get_random_account()
#We noticed that random account selection was becoming repeated code.

def get_random_account(exclude=None):
    account = random.choice(data)


    while account == exclude:
        account = random.choice(data)

    return account

#Now we can simply write:
account_a = get_random_account()
account_b = get_random_account(account_a)