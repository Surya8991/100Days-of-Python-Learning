# import files and modules
import random
from art import logo, vs
from celeb_data import data


score = 0
def random_data():
   return random.choice(data)

celebA = random_data()
celebB = random_data()
print("CelebA :- ", celebA["name"],
      celebA["follower_count"], celebA["description"])
print("CelebB :- ", celebB["name"],
      celebB["follower_count"], celebB["description"])

# def celeb_follower_comp():
#     if celebA["follower_count"]>celebB["follower_count"]:
#         winner_count=celebA["follower_count"]
#         print(celebA["name"],f"Wins with follwer count of {winner_count} Millons")
#     elif celebA["follower_count"] < celebB["follower_count"]:
#         winner_count=celebB["follower_count"]
#         print(celebB["name"],f"Wins with follwer count of {winner_count} Millons")
#     elif celebA["follower_count"] == celebB["follower_count"]:
#         print("Draw as both as same follower count")

# celeb_follower_comp()


def celeb_follower_compare():
    if celebA["follower_count"] > celebB["follower_count"]:
        return "A"
    elif celebA["follower_count"] < celebB["follower_count"]:
        return "B"
    elif celebA["follower_count"] == celebB["follower_count"]:
        return "AB"


celeb_follower_winner = celeb_follower_compare()

print(celeb_follower_winner)



def celeb_add_score():
    global score  # Declare score as global
    game_over = False
    while not game_over:
        celeb_choice = input("Who has more followers ? Type 'A' or 'B' ").upper()
        if celeb_follower_winner == celeb_choice:
            score += 1
            print(f"Your guess is correct Your Score :- {score}")
        else:
            game_over=True
            print(f"Sorry Wrong Answer! Your Final Score :- {score} ")
            
def high_low_game():
   celeb_add_score()
   
high_low_game()