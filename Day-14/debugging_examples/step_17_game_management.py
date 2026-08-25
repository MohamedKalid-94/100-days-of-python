#Step 17 — Separate game management into run_game()

def run_game():
    score = 0

    while True:
        result = play_round()

        if result:
            score += 1
            print("Score:", score)

            if score >= MAX_SCORE:
                print(
                    "Congratulations! "
                    "You reached the maximum score."
                )
                break

        else:
            print("Final Score:", score)
            break

#And finally:
run_game()