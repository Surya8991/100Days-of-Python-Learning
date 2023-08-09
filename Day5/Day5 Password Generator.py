import random
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '<', '>', ',', '.', '?', '/', '~', '`', "'", '"']
print("Welcome to pyPassword Generator")
nr_letters=int(input("Enter number of letter would you like ? \n"))
nr_numbers=int(input("Enter number of numbers would you like ? \n"))
nr_symbols=int(input("Enter number of symbol would you like ? \n"))

# Easy method but the in sequence

password=''
for char in range(1,nr_letters+1):
    random_char=random.choice(letter)
    password+=random_char
for num in range(1,nr_numbers+1):
    random_num=random.choice(numbers)
    password+=random_num
for sym in range(1,nr_symbols+1):
    random_sym=random.choice(special_characters)
    password+=random_sym

print(f"Congratz your password is {password}")

# Hard Method loop
# password=[]

# for char in range(1,nr_letters+1):
#     random_char=random.choice(letter)
#     password.append(random_char)
# for num in range(1,nr_numbers+1):
#     random_num=random.choice(numbers)
#     password.append(random_num)
# for sym in range(1,nr_symbols+1):
#     random_sym=random.choice(special_characters)
#     password.append(random_sym)

# random.shuffle(password)

# jumbeled_password=''.join(password)
# print(f"Congratz your genertaed password is {jumbeled_password}")