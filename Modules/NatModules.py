import random 
# The random module is a built-in python module that randomizes sequences such as list, tuples, and strings

# Example 1 
random_number = random.randint(1, 10)  # Generates a random integer between 1 and 10
print("Random number between 1 and 10:", random_number)

# Example 2 
fruits = ["apple", "banana", "cherry", "date"]
random_fruit = random.choice(fruits)  # Randomly selects a fruit from the list
print("Random fruit:", random_fruit)

# Example 3
random_list = random.sample(range(1, 20), 5)  # Generates a list of 5 unique random integers between 1 and 19
print("Random list of 5 unique integers:", random_list)


import datetime
# The datetime module is a built-in python module that allows you to work with dates and times.

# Example 1
current_date = datetime.date.today()  # Gets the current date
print("Current date:", current_date)

# Example 2
current_time = datetime.datetime.now()  # Gets the current date and time
print("Current time:", current_time)

# Example 3
future_date = current_date + datetime.timedelta(days=7)  # Calculates the date 7 days from now
print("Date 7 days from now:", future_date)

import math
# The math module is a built-in python module that provides mathematical functions and constants.

# Example 1
square_root = math.sqrt(int(input("Enter a number: ")))  # Calculates the square root of the entered number
print("Square root:", square_root)

# Example 2
pi_value = math.pi  # Gets the value of pi
print("Value of pi:", pi_value)

# Example 3
factorial_value = math.factorial(int(input("Enter a number: ")))  # Calculates the factorial of the entered number
print("Factorial:", factorial_value)
