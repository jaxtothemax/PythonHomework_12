import random

def play_game():
    country = {"Slovenia":"Ljubljana", "Croatia":"Zagreb", "Serbia":"Belgrade", "Spain":"Barcelona", 
               "Austria":"Vienna", "Hungary":"Budapest", "Italy":"Rome", "UK":"London", 
               "Slovakia":"Bratislava", "Germany":"Berlin", "Portugal":"Lisboa"}
               
    random_country = random.choice(list(country))
    capital_city = input(f"What is the capital city of {random_country}: ")

    key,value = random_country,capital_city
    if key in country and value == country[key]:
        print("That's correct, continue!")
    else:
        print("That's incorrect, google it!")

    play_game()
  
            
play_game()
