############ DEBUGGING#####################


# Describe Problem
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
# my_function()
# We are not getting any output when i == 20 because range reaches from 1 to 19
# sol: We can change the range from 1 to 21


# # Reproduce the Bug

# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0,5)
# print(dice_imgs[dice_num])
# We are getting an error of index when dice_num = 6 because an array starts from 0 not 1 and for 6 elemnets the range is 0 to 5 / 0 to n-1
# Sol: change the randint from 0 to 5

# # Play Computer

# year = int(input("What's your year of birth?"))
# if year >= 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")
# When the year is 1980 or 1984 there is no output
# To fix the issue we can assign that year greater then or equal to 1994 is Gen Z

# # Fix the Errors

# age = int(input("How old are you?\n "))
# if age >= 18:
#     print(f"You can drive at age {age}.")
# Error: We cannot check the age which is a str and check is it greater then 18 and cant display the age in print statement and indendent issues
# Solution change the data type of age to int , add a 4 space indendation and add f to the print statement


# #Print is Your Friend

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# Error word_per_page was given an equal to operator then assignemnet oppereator
# Sol: Replace == with = in word_per_page line

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
