# Step 5

import random
# import modules from another files
from Hangman_words import word_list
from Hangman_art import logo, stages
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()


    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            if letter in display:
                print(
                    f"You have already entered the correct letter :- {letter}\n")
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"{guess} is a Wrong Letter Entered")
        if lives == 0:
            end_of_game = True
            print("You lose & Hangman Died")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
 