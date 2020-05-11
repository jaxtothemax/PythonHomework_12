import random
import json
from datetime import datetime
import sys

secret = random.randint(1, 30)
now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())


def show_scores():
    print("-----Scores from previous players-----")
    for score_dict in score_list:
<<<<<<< HEAD:12.5 - Modular_Guessing_Game/guessing_game.py
        print(
            "Player: " + score_dict['name'] + ", " + str(score_dict["attempts"]) + " attempts, wrong attempts: " + str(
                score_dict.get("wrong_attempts")) + ", secret number: " + str(
                score_dict["secret_number"]) + ", date: " + score_dict["date"])


def quit_game():
    sys.exit()


=======
        print("Player: " + score_dict['name'] + ", " + str(score_dict["attempts"]) + " attempts, wrong attempts: " + str(score_dict.get("wrong_attempts")) + ", secret number: " + str(score_dict["secret_number"]) + ", date: " + score_dict["date"])
        
def quit_game():
    sys.exit()

>>>>>>> temp-branch:12.5/guessing_game.py
def play_game():
    user_input = input(
        "What do you want to do? Press 1 to play the game, press 2 to show top scores and press 3 to quit: ")
    if user_input == "1":
        name = str(input("Enter your name: "))
        attempts = 0
        while True:

            guess = int(input("Guess the secret number (between 1 and 30): "))
            attempts += 1

            if guess == secret:
                score_list.append({
<<<<<<< HEAD:12.5 - Modular_Guessing_Game/guessing_game.py
                    "secret_number": secret,
                    "name": name, "wrong_attempts": attempts - 1,
                    "attempts": attempts,
=======
                    "secret_number": secret, 
                    "name": name, "wrong_attempts": attempts-1, 
                    "attempts": attempts, 
>>>>>>> temp-branch:12.5/guessing_game.py
                    "date": date_time
                })

                with open("score_list.txt", "w") as score_file:
                    score_file.write(json.dumps(score_list))

                print("You've guessed it - congratulations! It's number " + str(secret))
                print("Attempts needed: " + str(attempts))

                user_decision = input("Do you want to play again? Answer with y or n: ")
                if user_decision == "y":
                    play_game()
                else:
                    quit_game()
                break

            elif guess > secret:
                print("Your guess is not correct... try something smaller")

            elif guess < secret:
                print("Your guess is not correct... try something bigger")
    elif user_input == "2":
        quit_game()


play_game()
