#Step 7 — Create compare_followers()
#We moved the comparison into a function:

def compare_followers(account_a, account_b):
    if account_a["followers"] > account_b["followers"]:
        return "A"
    else:
        return "B"
