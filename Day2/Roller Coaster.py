print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age=int(input("Enter your age"))
if height >= 120:
    if age >=18:
        print("You can ride and Your fare is 7$")
    else:
        print("You can ride and your fare is 5$")
else:
    print("You are too short for the ride")
