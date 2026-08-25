#Step 15 — Create the game loop
#Instead of playing only once:

while True:
    result = play_round()


    if result:
        score += 1
        print("Score:", score)
    else:
        print("Final Score:", score)
        break

#Now the game continues until the player gives a wrong answer.