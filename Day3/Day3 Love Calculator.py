print("Welcome to the Love calculator\n")
name1 = input("Enter First Person Name\n")
name2 = input("Enter Second Person Name \n")

name1_count = str(sum(1 for char in name1.lower() if char in ['t', 'r', 'u', 'e']))
name2_count = str(sum(1 for char in name2.lower() if char in ['l', 'o', 'v', 'e']))
total_per = int(name1_count) + int(name2_count)

print(total_per)

if total_per < 10:
    print(f"Your Score is {total_per}. You are like coke and mentos.")
elif 40 <= total_per <= 50:
    print(f"Your Score is {total_per}. You are so-so.")
elif total_per > 90:
    print(f"Your Score is {total_per}. You are like coke and mentos.")
else:
    print(f"You are in love! Score is {total_per}.")
