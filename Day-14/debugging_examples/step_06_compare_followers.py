#Step 6 — Compare followers
#We first wrote the comparison directly:

if account_a["followers"] > account_b["followers"]:
    print("A has more followers")
else:
    print("B has more followers")

#Then we recognized that this logic should be reusable.