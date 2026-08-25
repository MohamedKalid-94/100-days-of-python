#Step 8 — Add the tie condition
#We realized our original function couldn't handle equal follower counts. 

def compare_followers(account_a, account_b):
    if account_a["followers"] > account_b["followers"]:
        return "A"
    elif account_b["followers"] > account_a["followers"]:
        return "B"
    else:
        return "T"

