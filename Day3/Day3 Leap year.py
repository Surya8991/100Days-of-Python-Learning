# Program to Print Leap year if year is divisible by 4 , 100 and 400 evenly
year=int(input("Enter Year \n"))
if year % 4 == 0 and year % 100 == 0 and year % 400 :
    print(year," is a Leap Year")
else:
    print(year," is not a Leap Year")