import random

def play_game():
    country = {"Slovenia":"Ljubljana", "Croatia":"Zagreb", "Serbia":"Belgrade", "Spain":"Madrid", 
               "Austria":"Vienna", "Hungary":"Budapest", "Italy":"Rome", "UK":"London", 
               "Slovakia":"Bratislava", "Germany":"Berlin", "Portugal":"Lisboa", "Norway":"Oslo", 
               "Sweden":"Stockholm", "Denmark":"Copenhagen", "Russia":"Moscow", "Japan":"Tokyo", "Finland":"Helsinki",
               "China":"Beijing", "India":"New Delhi"}
               
    random_country = random.choice(list(country))
    capital_city = input(f"What is the capital city of {random_country}: ").title()

    if capital_city == country[random_country]:
        print("That's correct, continue!")
    else:
        print("That's incorrect, google it!")

    play_game()
  
play_game()
