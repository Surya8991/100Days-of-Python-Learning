# FizzBuzz Program : print fizz if number is divisible by 3 and buzz if divisilbe by 5 and fizz BUzz if divisible by 5 and 3
print("Welcome to the Fizz Buzz Program \n")
number=int(input("Enter the number till you wanna run \n"))
result=[]
for num in range(1,number+1):
    if num % 3 == 0 and num % 5 ==0:
        result.append("FizzBuzz")
    elif num % 3 == 0:
        result.append("Fizz")
    elif num % 5 ==0:
        result.append("Buzz")
    else:
        result.append(num)
print(result)
