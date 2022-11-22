# to guess the number
import random

correct_answer = random.randint(1, 100)
gameover = False

while gameover == False:

    player_guess = int(input("guess the number beetween 1 to 100 : "))

    if player_guess == correct_answer:
        compareanswer = "Right"
        gameover = True
    elif player_guess > correct_answer:
        compareanswer = "high"
    elif player_guess < correct_answer:
        compareanswer = "low"

    if compareanswer == "Right":
        print("correct answer u won!")
    elif compareanswer == "high":
        print("too highr ! guess again")
    elif compareanswer == "low":
        print("too low! guess again")