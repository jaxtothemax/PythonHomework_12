import random

def play_game():
    country = {"Slovenia":"Ljubljana", "Croatia":"Zagreb", "Serbia":"Belgrade", "Spain":"Barcelona", 
               "Austria":"Vienna", "Hungary":"Budapest", "Italy":"Rome", "UK":"London", 
               "Slovakia":"Bratislava", "Germany":"Berlin", "Portugal":"Lisboa"}
               
    random_country = random.choice(list(country))
    capital_city = input(f"What is the capital city of {random_country}: ")

    for key, value in country.items():
        if capital_city == value:
            print("That's correct!")
            play_game()
    else: 
        print("That's incorrect, try again!")
        play_game()

play_game()