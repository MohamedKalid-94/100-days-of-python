#Step 4 — Display the accounts
#We accessed dictionary values:

print("A:", account_a["name"])
print("B:", account_b["name"])

#Then we expanded the data:

{
    "name": "Instagram",
    "followers": 1000000,
    "description": "Social media platform",
    "country": "USA"
}

#And displayed:
print(account_a["description"], "from", account_a["country"])
