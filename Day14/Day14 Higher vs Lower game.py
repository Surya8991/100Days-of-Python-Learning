# import files and modules
import random
from art import logo, vs
from celeb_data import data
print(logo)

score = 0


def random_data():
    return random.choice(data)


def celeb_follower_compare(celebA, celebB):
    if celebA["follower_count"] > celebB["follower_count"]:
        return "A"
    elif celebA["follower_count"] < celebB["follower_count"]:
        return "B"
    elif celebA["follower_count"] == celebB["follower_count"]:
        return "AB"


def celeb_add_score():
    global score  # Declare score as global
    game_over = False
    while not game_over:
        celebA = random_data()
        celebB = random_data()
        print("CelebA :- ", celebA["name"],"as",
              celebA["description"], " from ", celebA['country'], "\n")
        print(vs)
        print("CelebB :- ", celebB["name"],"as",
              celebB["description"]," from ", celebB['country'], "\n")
        celeb_follower_winner = celeb_follower_compare(celebA, celebB)
        print(celeb_follower_winner)
        celeb_choice = input(
            "Who has more followers ? Type 'A' or 'B' or 'both' if you think both have Equal follower count \n").upper()
        if celeb_follower_winner == celeb_choice:
            score += 1
            print(f"\n 😊 Your guess is correct Your Score :- {score} \n")
        else:
            game_over = True
            print(f"\n 🙃 Sorry Wrong Answer! Your Final Score :- {score} \n")


def high_low_game():
    celeb_add_score()


high_low_game()
