# Create a Basic Python function to greet the user based on time and their name
# 1. Single Parameter/ input

# import datetime
# time = datetime.datetime.now()
# time_in_hr = time.hour
# name = input("Enter you Name \n")
# def greet(name):
#     if 6 <= time_in_hr < 12:
#         print(f"Good Morning!, {name} Have a nice day ahead.")
#     elif 12 <= time_in_hr < 18:
#         print(f"Good Afternoon, {name}! Have a nice day ahead.")
#     elif 18 <= time_in_hr or time_in_hr < 6:
#         print(f"Good Night, {name}! Sweet Dreams.")
#     else:
#         print("Have a nice day!")
# greet(name)

# OutPut:Good Afternoon, Ram! Have a nice day ahead.

# 2. Multiple parmaters
# We can add Multiple parmaters by adding a colun(,)

# def greet(name,city):
#     print(f"Hi I am {name} what is like in {city}")
# greet("Ram","Goa")
# output: Hi I am Ram what is like in Goa

# 3. if the input are not in order called positional arguments

# def greet(name,city):
#     print(f"Hi I am {name} what is like in {city}")

# eg : greet("Goa","Ram") output: Hi I am Goa what is like in Ram

# 4. To avoid the above problem or Situation we can use keyword arguments where we assign values to each arguments directly

def greet(name,city):
    print(f"Hi I am {name} what is like in {city}")

greet(city="Goa",name="Ram")
# output : Hi I am Ram what is like in Goa