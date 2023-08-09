# import logo from Ceaser_Cipher_art file
from Ceaser_Cipher_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Logo print

print(logo)
# In a Single function
def ceaser_cipher(enc_dec,plain_text,shift_amount):
    changed_text=''
    for letter in plain_text:
        position=alphabet.index(letter)
        if enc_dec=="encode":
             new_position = position + shift_amount
             new_letter=alphabet[new_position]
             changed_text+=new_letter
        elif enc_dec=="decode":
             new_position = position - shift_amount
             new_letter=alphabet[new_position]
             changed_text+=new_letter
    print(f"The Code after performing {enc_dec}ing is {changed_text}")  

should_end=False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != "encode" and direction != "decode":
        print("Invalid Method")
        break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    ceaser_cipher(enc_dec=direction,plain_text=text,shift_amount=shift)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
    print("Goodbye")


# Perform encoding and decoding seperatly
# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")
# def decrypt(encypt_text,shift_amt):
#     decipher_text = ""
#     for letter in encypt_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amt
#         decipher_text += alphabet[new_position]
#     print(f"The decoded text is {decipher_text}")
# if direction=="encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction=="decode":
#     decrypt(encypt_text=text,shift_amt=shift)
# else:
#     print("Invalid Method")
