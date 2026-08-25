#Step 3 — Prevent duplicate accounts
#We added:

while account_b == account_a:
    account_b = random.choice(data)

#Now A and B must be different.
#This was an important lesson in using a while loop to enforce a condition.