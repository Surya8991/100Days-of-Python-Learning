# import files and modules
import random
from art import logo, vs
from celeb_data import data

celebA=random.choice(data)
celebB=random.choice(data)
score=0
print("CelebA :- ",celebA["name"],celebA["follower_count"],celebA["description"])
print("CelebB :- ",celebB["name"],celebB["follower_count"],celebB["description"])

celeb_choice=input("Who has more followers ? Type 'A' or 'B' ")

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
     if celebA["follower_count"]>celebB["follower_count"]:
        return "A"
     elif celebA["follower_count"] < celebB["follower_count"]:
        return "B"
     elif celebA["follower_count"] == celebB["follower_count"]:
        return "AB"

celeb_follower_winner=celeb_follower_compare()

print(celeb_follower_winner)

def celeb_add_score():
    if celeb_follower_winner == celeb_choice:
        print("Your guess is correct")