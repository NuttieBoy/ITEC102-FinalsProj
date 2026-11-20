#                                               < - - - OS Module - - - >

# The OS module is a built-in Python module that allows Python programs to interact with the computer's operating system.
# It allows programmers to manage files and folders, access directories, create new folders, and interact with the computer's environment.


# Example 1: File and Directory Explorer
import os

# Get the current directory
location = os.getcwd()

print("CURRENT DIRECTORY:")
print(location)

# Display files and folders
print("\nCONTENTS:")

for item in os.listdir(location):
    print(item)



# Example 2: Automatic Folder Organizer
import os

files = ["report.pdf", "photo.jpg", "notes.txt"]

for file in files:
    extension = file.split(".")[-1]

    if extension == "pdf":
        folder = "PDF_Files"
    elif extension == "jpg":
        folder = "Images"
    elif extension == "txt":
        folder = "Text_Files"

    if not os.path.exists(folder):
        os.mkdir(folder)

    destination = os.path.join(folder, file)

    print(file, "will be organized into", destination)



# Example 3: File Existence Checker
import os

filename = input("Enter a filename: ")

if os.path.exists(filename):
    print("The file or folder exists!")
else:
    print("The file or folder does not exist.")


#                                               < - - - SYS Module - - - >

# The sys module is a built-in Python module that provides access to system-specific parameters and functions used by the Python interpreter.
# The SYS module helps Python programmers understand and control certain aspects of how their programs run.

# Example 1: Python System Information Checker
import sys

print("PYTHON SYSTEM INFORMATION")

print("Python Version:", sys.version)
print("Operating System:", sys.platform)
print("Python Executable:", sys.executable)
# This program displays information about the Python interpreter and operating system.


# Example 2: Memory Size Calculator
import sys

name = "Python Programming"
numbers = [10, 20, 30, 40, 50]
student = {"name": "Alex", "age": 18}

print("MEMORY USAGE")

print("String:", sys.getsizeof(name), "bytes")
print("List:", sys.getsizeof(numbers), "bytes")
print("Dictionary:", sys.getsizeof(student), "bytes")
# This program measures the memory size of different Python objects.


# Example 3: Command-Line Argument Reader
import sys

print("STUDENT INFORMATION")

if len(sys.argv) >= 3:
    name = sys.argv[1]
    course = sys.argv[2]

    print("Name:", name)
    print("Course:", course)
else:
    print("Please provide your name and course.")
# This program accepts information supplied when executing a Python file through the command line.


#                                               < - - - Statistic Module - - - >

# The statistics module is a built-in Python module that provides mathematical functions for analyzing numerical data.
# It is used to calculate statistical measurements such as mean, median, mode, variance, and standard deviation.

# Example 1: Student Grade Analyzer
import statistics

grades = [85, 90, 85, 95, 80, 85, 90]

print("STUDENT GRADE ANALYSIS")

print("Grades:", grades)
print("Average:", statistics.mean(grades))
print("Median:", statistics.median(grades))
print("Mode:", statistics.mode(grades))
#v his program calculates the average, median, and most frequently occurring grade of students.


# Example 2: Student Performance and Score Distribution
import statistics

scores = [75, 80, 85, 90, 95]

variance = statistics.variance(scores)
deviation = statistics.stdev(scores)

print("SCORE DISTRIBUTION")

print("Scores:", scores)
print("Variance:", variance)
print("Standard Deviation:", deviation)
# This program calculates the variance and standard deviation of students' scores.


# Example 3: Multiple Data Analysis
import statistics

sales = [1200, 1500, 1200, 1800, 2000, 1500, 1200]

average = statistics.mean(sales)
middle = statistics.median(sales)
frequent = statistics.multimode(sales)

print("WEEKLY SALES ANALYSIS")

print("Sales:", sales)
print("Average Sales:", average)
print("Median Sales:", middle)
print("Most Frequent Sales:", frequent)
# This program analyzes a collection of sales figures and identifies the average, highest frequency, and middle value.

