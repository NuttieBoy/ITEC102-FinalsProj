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
