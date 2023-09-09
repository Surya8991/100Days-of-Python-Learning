# 100Days-of-Python-Learning

Creating this repository allows me to meticulously track my journey of learning about Python over the span of 100 days

## Day-1 in 100 Days of code

Learned about Print , input concepts in Python

1.Print:

In Python, print is like a command that tells the computer to display a message or some information on the screen.
It's like telling the computer, "Hey, show this to the user."
You put the message or data you want to show inside the parentheses of print().
For example, print("Hello, World!") will display "Hello, World!" on the screen.

2.Input:

input is another command in Python, but it's used to get information from the user.
It's like asking the user a question and waiting for their answer.
When you use input, the program stops and waits for the user to type something.
Whatever the user types is stored as text (a string) that you can use in your program.
For example, name = input("What's your name? ") will ask the user for their name, and whatever they type will be stored in the name variable

### Code

    print("Welcome to Band Name Generator 😎")

    city = input("Enter Your City Name \n")

    animal = input("Enter Your Pet's Name or a Name you Like \n")

    print(f"Thank You for using Brand Generator Your Band Name is \n {city} {animal}")

## Day2 in 100 Days of code

Learned about DataTypes in Python

**Data Types in Python:**

Data types are categories or classifications of data in programming languages that define how data is stored and manipulated. Python has several built-in data types, including:

1. **Integers (`int`):** These are whole numbers, like 5, -3, or 1000. You can perform arithmetic operations (addition, subtraction, multiplication, division) with integers.

2. **Floating-Point Numbers (`float`):** These are numbers with a decimal point, like 3.14 or -0.5. They are used for more precise calculations that involve fractions.

3. **Strings (`str`):** Strings are sequences of characters, like "Hello, World!" or "Python is fun." You can manipulate and process text using string operations.

4. **Boolean (`bool`):** Boolean values represent two possible states, `True` or `False`. They are used for logical operations and decision-making.

5. **Lists (`list`):** Lists are ordered collections of items. They can contain elements of different data types and are mutable (can be changed).

6. **Tuples (`tuple`):** Tuples are similar to lists but are immutable (cannot be changed). They are often used for storing related pieces of data.

7. **Dictionaries (`dict`):** Dictionaries store key-value pairs and are used for mapping keys to values. They are unordered and mutable.

8. **Sets (`set`):** Sets are unordered collections of unique elements. They are useful for removing duplicates and performing set operations like union and intersection.

**Manipulating Strings in Python:**

Strings in Python are quite versatile, and you can manipulate them in various ways:

1. **Concatenation:** You can combine two or more strings using the `+` operator.

   ```python
   first_name = "John"
   last_name = "Doe"
   full_name = first_name + " " + last_name
   ```

2. **String Interpolation:** You can insert variables or values into strings using f-strings (formatted strings).

   ```python
   name = "Alice"
   age = 30
   sentence = f"My name is {name} and I am {age} years old."
   ```

3. **String Slicing:** You can extract specific portions of a string using slicing. Strings are zero-indexed, and you can use square brackets `[]` to access individual characters or ranges of characters.

   ```python
   message = "Hello, World!"
   first_five_chars = message[:5]  # "Hello"
   ```

4. **String Methods:** Python provides many built-in methods for string manipulation. Some common methods include `upper()`, `lower()`, `strip()`, `replace()`, `split()`, and more.

   ```python
   text = "   Python is fun!   "
   stripped_text = text.strip()         # "Python is fun!"
   uppercase_text = text.upper()        # "   PYTHON IS FUN!   "
   replaced_text = text.replace("fun", "awesome")  # "   Python is awesome!   "
   ```

5. **String Length:** You can find the length (number of characters) of a string using the `len()` function.

   ```python
   text = "Hello, World!"
   length = len(text)  # 13
   ```

These are some of the basic string manipulation techniques in Python. Strings are fundamental for working with text data and are used extensively in Python programs.

Programs:

### Program to find how much per person cost for food after adding tip

    print("Welcome to the Sunshine Cafe \n Tip Calcluator")
    bill=int(input("Enter the Bill Amount \n"))
    people=int(input("Enter the No. of People to Split the bill \n"))
    tip=int(input("Enter the tip: \n"))
    per_person=round(((bill+tip)/people),2)
    print(f"Amount to be paid by Per person is {per_person}")

### Roller Coaster Program

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

## Day3

Learned about Controllows and Logical Operations

Control flows and logical operations are fundamental concepts in programming, including Python. They are essential for making decisions, controlling the flow of a program, and performing various operations based on conditions. Let's explore both concepts in Python:

1. Control Flows:
Control flows determine the order in which statements in a program are executed. Python provides several control flow structures:

   a. Conditional Statements:
      - `if`: Conditional statements allow you to execute code blocks based on a condition. If the condition is true, the indented block of code is executed. If the condition is false, the block is skipped.
   
      ```python
      if condition:
          # code to execute if the condition is true
      else:
          # code to execute if the condition is false
      ```

   b. Loops:
      - `for`: The `for` loop is used to iterate over a sequence (e.g., a list or string) or a range of numbers.
      
      ```python
      for item in iterable:
          # code to execute for each item
      ```

      - `while`: The `while` loop continues to execute a block of code as long as a specified condition remains true.

      ```python
      while condition:
          # code to execute while the condition is true
      ```

   c. Loop Control Statements:
      - `break`: Terminates the current loop and jumps to the next statement outside the loop.
      - `continue`: Skips the current iteration of the loop and moves to the next iteration.

2. Logical Operations:
Logical operations in Python involve evaluating and manipulating boolean values (`True` or `False`) to make decisions. Python provides the following logical operators:

   a. `and`: The `and` operator returns `True` if both operands are `True`. Otherwise, it returns `False`.

   ```python
   if condition1 and condition2:
       # code to execute if both conditions are true
   ```

   b. `or`: The `or` operator returns `True` if at least one of the operands is `True`. It returns `False` if both operands are `False`.

   ```python
   if condition1 or condition2:
       # code to execute if at least one condition is true
   ```

   c. `not`: The `not` operator negates the boolean value of an expression. It returns `True` if the expression is `False`, and vice versa.

   ```python
   if not condition:
       # code to execute if the condition is false
   ```

   d. Comparison Operators: These operators compare values and return boolean results.
      - `==`: Equal to
      - `!=`: Not equal to
      - `<`: Less than
      - `<=`: Less than or equal to
      - `>`: Greater than
      - `>=`: Greater than or equal to

   ```python
   if x == 10:
       # code to execute if x is equal to 10
   ```

These control flow structures and logical operations are essential tools for creating conditional behavior, iterating through data, and making decisions in Python programs. They help you build complex algorithms and make your code more dynamic and responsive to different situations.

### Programs

    # Program to Print Leap year if year is divisible by 4 , 100 and 400 evenly
    year=int(input("Enter Year \n"))
    if year % 4 == 0 and year % 100 == 0 and year % 400 :
        print(year," is a Leap Year")
    else:
        print(year," is not a Leap Year")


    #Love Calculator Program
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

    #Odd or Even Program
    number = int(input("Which number do you want to check? "))
    if number % 2 == 0:
        print(number, "is a Even Number")
    else:
        print(number, "is a Odd Number")

    # In this Program We are gonna learn loopsss
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    turn = input("Pick a Direction Left or Right!? \n")
    if turn.lower() == 'left':
        swim_wait = input("Do you wanna swim or wait? \n")
        if swim_wait.lower() == "wait":
            door = input("Congrats you have crossed the sea ! Pick a Door from Red , Green and Yellow Door and find the Treasure \n")
            if door.lower() == "yellow":
                print("Congratz You Win!😊")
            elif door.lower() =="red":
                print("Burned by fire Game Over!")
            elif door.lower() == "green":
                print("Eaten By Beast Game Over!")
            else:
                print("Killed by Hunters Game Over!")
        else:
            print("Attacked by Sharks Game Over!")
    else:
        print("Wrong Choice You fell into the River Game Over!")
