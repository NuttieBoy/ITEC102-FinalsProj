# This file is used for learning purposes
# print is used to display values enclosed by a parenthesis (value)
# words use "words" in order to be displayed, numbers do not need ""
print ("Hello, World!")
# variables hold values denoted by the = sign
# python can evaluate mathematical expressions denoted by +,*,/
a = 100
b = 200
c = 300
d = a * b / c
print(d)
name = "Nathaniel"
age = 18
print(name)
print(age)
# commas ,can be used to seperate multiple values
print ("Name:", name)
print ("Age:", age)
# f-strings provide a clean way to input variables within text f{}
#The letter f before the quotation marks tells Python to replace the values inside {} with the corresponding variables or expressions.
print (f"My name is {name} and I am {age} years old")
#By default, print() ends with a new line. You can change this behavior using the end parameter.
print ("Hello,",end=" ")
print ("World!")
#When printing multiple values, Python separates them with a space by default. You can change the separator using the sep parameter.
print ("Nat","Bat","Rat", sep=".")
#Special characters begin with a backslash (\).
#\n = new line
#\t = horizontal tab
#\" = Double Quotation Mark
#\' = Single Quotation Mark
#\\ = Backslash
print ("First Line \nSecond Line")
print ("Name: \tNathaniel")
print ("\"Quotation Mark")
print ("\'Single Quote")
print ("\\Backslash")
# The equal sign (=) is called the assignment operator because it assigns a value to a variable. 
height = 2.25
print (height)
# variables cannot contain numbers or special characters at the beginning of their names. They can only start with letters or underscores (_).
# integers are whole numbers, while floats are decimal numbers.
age = 60
year = 2026
price = 19.99
print (price)
# The type() function is used to determine the data type of a variable or value.
print(type(height))
print(type(age))
print(type(year))
# strings are sequences of characters enclosed in either single quotes (' ') or double quotes (" ").
# You can use either single or double quotes to define a string, as long as you are consistent within the same string.
# Strings can contain letters, numbers, symbols, and whitespace characters.
name = "Nathaniel"
course = 'Python Programming'
print(name)
print(course)
#Booleans are a data type that can have one of two values: True or False. They are often used to represent the truth value of a condition or statement. 
is_student = True
is_teacher = False
print(is_student)
print(is_teacher)
#Python allows multiple variables to be assigned in a single line.
name, age, course = "Nathaniel", 18, "Python Programming"
print(name, age , course)
print(name)
print(age)
print(course)
#You can assign the same value to several variables simultaneously.
x = y = z = 10
print(x)
print(y)
print(z)
#Variables can be reassigned at any time.
score = 85
print(score)
score = 90
print(score)
# concatenation is the process of combining two or more strings together using the + operator.
first_name = "Nathaniel"
last_name = "Bacomo"
full_name = first_name + " " + last_name
#The space (" ") between the names is added manually to separate the words.
print(full_name)
# Variables containing strings can be combined with other strings.
course = "Python Programming"
message = "I am currently enrolled in " + course
print(message)
# You can join several strings in a single expression.
city = "Liliw"
province = "Laguna"
country = "Philippines"
Location = city + "." + province + "," + country
print(Location)
# Python does not allow strings and numbers to be concatenated directly.
# Use the str() function to convert numbers into strings before concatenation.
age = 18
message = "I am " + str(age) + " years old"
print(message)
# Instead of concatenation, you can separate values with commas in the print() function.
age = 18
name = "Nathaniel"
print("Name:", name, "Age:", age)
print("Hello" + "," + " " + name + "!")