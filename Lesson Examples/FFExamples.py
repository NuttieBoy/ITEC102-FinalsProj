# Example 1 (Easy): Write and read a file
with open("fruits.txt", "w") as file:
    file.write("apple\nbanana\ncherry\n")
with open("fruits.txt", "r") as file:
    print(file.read())  # Output: apple, banana, cherry (each on its own line)

# Example 2 (Easy): Append a new line to the file
with open("fruits.txt", "a") as file:
    file.write("date\n")
with open("fruits.txt", "r") as file:
    print(file.read())  # Output: apple, banana, cherry, date

# Example 3 (Easy): Read one line at a time
with open("fruits.txt", "r") as file:
    print(file.readline().strip())  # Output: apple
    print(file.readline().strip())  # Output: banana

# Example 4 (Easy): Stream the file with a for loop
with open("fruits.txt", "r") as file:
    for fruit in file:
        print("Fruit:", fruit.strip())  # Output: Fruit: apple ... Fruit: date

# Example 5 (Intermediate): Number each line
with open("fruits.txt", "r") as file:
    number = 1
    for fruit in file:
        print(f"{number}. {fruit.strip()}")  # Output: 1. apple  2. banana  3. cherry  4. date
        number += 1

# Example 6 (Intermediate): Write many lines using a loop
with open("squares.txt", "w") as file:
    for n in range(1, 6):
        file.write(f"{n} squared is {n * n}\n")
with open("squares.txt", "r") as file:
    print(file.read())  # Output: 1 squared is 1 ... 5 squared is 25

# Example 7 (Intermediate): Add up numbers stored in a file
with open("numbers.txt", "w") as file:
    file.write("10\n20\n30\n40\n50\n")
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())  # Lines are text, so convert them with int()
print("Total:", total)  # Output: Total: 150

# Example 8 (Intermediate): Count the lines and words in a file
line_count = 0
word_count = 0
with open("squares.txt", "r") as file:
    for line in file:
        line_count += 1
        word_count += len(line.split())  # split() breaks a line into words
print("Lines:", line_count)  # Output: Lines: 5
print("Words:", word_count)  # Output: Words: 20

# Example 9 (Hard): Copy a file and change the text to uppercase
with open("fruits.txt", "r") as source, open("fruits_upper.txt", "w") as target:  # Two files in one with
    for line in source:
        target.write(line.upper())
with open("fruits_upper.txt", "r") as file:
    print(file.read())  # Output: APPLE, BANANA, CHERRY, DATE

# Example 10 (Hard): Read a file in chunks (true streaming)
with open("fruits.txt", "r") as file:
    chunk = file.read(6)  # Read 6 characters at a time
    while chunk != "":  # read() returns an empty string at the end of the file
        print(repr(chunk))  # Output: 'apple\n' 'banana' '\nchier'... (6 characters per chunk)
        chunk = file.read(6)

# Example 11 (Hard): Handle a missing file safely with a function
def safe_read(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
print(safe_read("fruits.txt"))  # Output: apple, banana, cherry, date
print(safe_read("ghost.txt"))  # Output: File not found.

# Example 12 (Hard): Skip bad lines and keep going
with open("mixed.txt", "w") as file:
    file.write("10\nabc\n30\nxyz\n50\n")
total = 0
with open("mixed.txt", "r") as file:
    for line in file:
        try:
            total += int(line.strip())
        except ValueError:
            print("Skipping:", line.strip())  # Output: Skipping: abc  then  Skipping: xyz
print("Total:", total)  # Output: Total: 90

# Example 13 (Hard): Stream a large file and filter it into a new file
with open("big.txt", "w") as file:
    for i in range(1, 100001):
        file.write(f"Line number {i}\n")
saved = 0
with open("big.txt", "r") as source, open("every_tenth.txt", "w") as target:
    for line in source:  # Only one line is in memory at a time
        if line.strip().endswith("0"):
            target.write(line)
            saved += 1
print("Lines saved:", saved)  # Output: Lines saved: 10000

# Functions examples 

# Example 1 (Easy): A function with no parameters
def say_hello():
    print("Hello, World!")
say_hello()  # Output: Hello, World!

# Example 2 (Easy): A function with one parameter
def welcome(name):
    print("Welcome,", name)
welcome("Kent")  # Output: Welcome, Kent

# Example 3 (Easy): A function with two parameters
def multiply(a, b):
    print(a * b)
multiply(6, 7)  # Output: 42

# Example 4 (Easy): A function that returns a value
def double(number):
    return number * 2
print(double(8))  # Output: 16

# Example 5 (Intermediate): Use a returned value in a calculation
def area_of_rectangle(width, height):
    return width * height
room = area_of_rectangle(4, 5)
print(f"The area is {room} square meters")  # Output: The area is 20 square meters

# Example 6 (Intermediate): A default parameter value is used when no argument is given
def greet_with_title(name, title="Student"):
    print(f"Hello, {title} {name}")
greet_with_title("Maria")  # Output: Hello, Student Maria
greet_with_title("Cruz", "Professor")  # Output: Hello, Professor Cruz

# Example 7 (Intermediate): A function that returns True or False
def is_even(number):
    return number % 2 == 0
print(is_even(10))  # Output: True
print(is_even(7))  # Output: False

# Example 8 (Intermediate): Keyword arguments let you name the parameters in any order
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")
describe_pet(name="Max", animal="dog")  # Output: I have a dog named Max

# Example 9 (Intermediate): A global counter that a function modifies
visits = 0
def add_visit():
    global visits
    visits += 1
    print("Total visits:", visits)
add_visit()  # Output: Total visits: 1
add_visit()  # Output: Total visits: 2
add_visit()  # Output: Total visits: 3

# Example 10 (Intermediate): Local and global variables with the same name are different variables
level = 1
def change_level():
    level = 99  # This is a new local variable, the global one is not changed
    print("Inside:", level)
change_level()  # Output: Inside: 99
print("Outside:", level)  # Output: Outside: 1

# Example 11 (Hard): A function that calls another function
def square_number(n):
    return n * n
def sum_of_squares(a, b):
    return square_number(a) + square_number(b)
print(sum_of_squares(3, 4))  # Output: 25

# Example 12 (Hard): A function with a loop and a return value
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))  # Output: 120

# Example 13 (Hard): A function that checks for a prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(17))  # Output: True
print(is_prime(18))  # Output: False

# Example 14 (Hard): A function that returns two values
def min_and_max(a, b):
    if a < b:
        return a, b
    return b, a
smallest, largest = min_and_max(9, 4)
print(smallest, largest)  # Output: 4 9

# Example 15 (Hard): A function that calls itself (recursion)
def countdown(n):
    if n == 0:
        print("Liftoff!")
        return
    print(n)
    countdown(n - 1)
countdown(3)  # Output: 3  2  1  Liftoff!

# Example 16 (Hard): Mini program using functions and the math module
def circle_area(radius):
    return math.pi * radius ** 2
def circle_circumference(radius):
    return 2 * math.pi * radius
r = 5
print(f"Area: {circle_area(r):.2f}")  # Output: Area: 78.54
print(f"Circumference: {circle_circumference(r):.2f}")  # Output: Circumference: 31.42
