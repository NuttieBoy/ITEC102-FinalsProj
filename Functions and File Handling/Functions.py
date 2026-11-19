# A function is a named block of code that performs a specific task. It only runs when it is called
# The def keyword defines a function. Syntax: def function_name():
def greet():
    print("Welcome to Python!")
greet()  # Calling the function. Output: Welcome to Python!
greet()  # A function can be called as many times as needed. Output: Welcome to Python!
# A parameter is a variable listed in the function definition. It lets you pass data into the function
# The value you pass when calling the function is called an argument
def greet_user(name):
    print("Hello,", name)
greet_user("Alice")  # Output: Hello, Alice
greet_user("Bob")  # Output: Hello, Bob
# A function can have multiple parameters, separated by commas
def add(a, b):
    print(a + b)
add(10, 20)  # Output: 30
# The return statement sends a value back to the caller, so it can be stored in a variable or used in an expression
def square(number):
    return number ** 2
result = square(5)
print(result)  # Output: 25
print(square(3) + square(4))  # Output: 25
# print() only displays information on the screen, return sends a value back to the calling code
def show():
    print("Hello")
def give():
    return "Hello"
show()  # Output: Hello
message = give()
print(message)  # Output: Hello
# A global variable is declared outside all functions and can be read anywhere in the program
site = "Welcome!"
def display():
    print(site)
display()  # Output: Welcome!
# To modify a global variable inside a function, use the global keyword
count = 0
def increase():
    global count
    count += 1
increase()
increase()
print(count)  # Output: 2
# A local variable is declared inside a function. It only exists while the function is running
def make_local():
    secret = 42
    print(secret)
make_local()  # Output: 42
# print(secret)  # This would cause a NameError because secret only exists inside the function
# The import statement lets you use built-in modules such as math, random, datetime, and os
import math
print(math.sqrt(25))  # Output: 5.0
from math import sqrt  # Importing a specific function
print(sqrt(49))  # Output: 7.0
import math as m  # Importing with an alias (a shorter name)
print(m.pi)  # Output: 3.141592653589793
