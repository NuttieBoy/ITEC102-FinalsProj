# File streaming means reading or writing a file one piece at a time instead of loading the whole file into memory
# The open() function opens a file and returns a file object. Syntax: open("filename", "mode")
# Modes: "r" read (default), "w" write (overwrites), "a" append, "x" create new (error if it exists), "r+" read and write, "w+" read and write (overwrites), "a+" read and append
file = open("message.txt", "w")  # "w" creates the file, or overwrites it if it already exists
file.write("Hello\nWelcome to Python.")  # \n moves to a new line, write() does not add it for you
file.close()  # Always close the file when you are done
file = open("message.txt", "r")
print(file.read())  # read() reads the entire file. Output: Hello (new line) Welcome to Python.
file.close()
file = open("message.txt", "r")
print(file.readline().strip())  # readline() reads one line. Output: Hello
print(file.readline().strip())  # Output: Welcome to Python.
file.close()
file = open("message.txt", "r")
print(file.readlines())  # readlines() returns all lines as a list. Output: ['Hello\n', 'Welcome to Python.']
file.close()
# Looping over the file is the most efficient way to stream it, because only one line is in memory at a time
file = open("message.txt", "r")
for line in file:
    print(line.strip())  # strip() removes the \n at the end of each line
file.close()
# Append mode adds new content to the end without removing the old content
file = open("message.txt", "a")
file.write("\nWelcome to file streaming.")
file.close()
# The with statement is the recommended way. It closes the file automatically, even if an error happens
with open("message.txt", "r") as file:
    content = file.read()
print(content)
import os
print(os.path.exists("message.txt"))  # Checking if a file exists. Output: True
print(os.path.exists("ghost.txt"))  # Output: False
try:
    with open("ghost.txt", "r") as file:  # Opening a missing file raises an error
        print(file.read())
except FileNotFoundError:
    print("File not found.")  # Output: File not found.
