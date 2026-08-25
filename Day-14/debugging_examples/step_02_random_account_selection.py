#Step 2 — Select random accounts
#We introduced the random module.

import random

account_a = random.choice(data)
account_b = random.choice(data)

#Problem we discovered
#Sometimes both variables could contain the same account.

#For example: A → Instagram B → Instagram
#That doesn't make sense for the game.

