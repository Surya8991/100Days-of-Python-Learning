# Program to build a Number Guessing Game
# Import random module
from art import logo
from random import *

# Logo
print(logo)

# random input
random_no = randint(1, 100)
print(random_no)


print("Welcome to Guess a Number Game !")
print("I'm Thinking of a number between 1 and 100 ")
# Inputs
difficulty = input("Choose a Difficulty . Type 'easy' or 'hard' ").lower()
# attempts
if difficulty == "easy":
    attempt = 10
elif difficulty == "hard":
    attempt = 5
else:
    print("Invalid Game Mode")
    exit()

print(f" You Have {attempt} attempt left to guess the correct number")
number = int(input("Guess a Number: \n"))
while attempt > 0:
    if random_no > number:
        print(f'attempt No {attempt}')
        attempt -= 1
        print(
            f"Too Low \n Guess Again \n You Have {attempt} attempt left to guess the correct number")
        number = int(input("Guess a Number \n"))
    elif random_no < number:
        print(f'attempt No {attempt}')
        attempt -= 1
        print(
            f"Too High \n Guess Again \n You Have {attempt} attempt left to guess the correct number")
        number = int(input("Guess a Number \n"))
    elif random_no == number:
        print(f"You have Won , The Correct number is : {random_no} ")
        break
    if attempt == 0:
        print(f"You Lost The Game \n The Correct number is : {random_no} ")
