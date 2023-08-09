# Program to find the number is prime number or not
def isPrime(number):
    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

number = int(input("Enter a number: "))
if isPrime(number):
    print("It is a Prime Number")
else:
    print("It is not a Prime Number")
