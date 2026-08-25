#We noticed that displaying A and B was duplicated.

#Instead of:
print("A:", account_a["name"])
print(account_a["description"], "from", account_a["country"])

print("B:", account_b["name"])
print(account_b["description"], "from", account_b["country"])

#we created:

def display_account(account, label):
    print(f"{label}: {account['name']}")
    print(f"{account['description']} from {account['country']}")

#Then:
display_account(account_a, "A")
display_account(account_b, "B")

#This introduced another important programming principle:
#Don't repeat the same logic unnecessarily.