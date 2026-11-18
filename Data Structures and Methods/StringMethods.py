#String methods: allow programmers to manipulate, search, modify, and format text efficiently.
#<--- Common String Methods --->

#1. upper() - converts all characters to uppercase.
text = "python"
print(text.upper()) #Output: PYTHON

#2. lower() - convert all characters to lowercase.
text = "PYTHON"
print(text.lower()) #Output: python

#3. title() - converts every first letter of a word to uppercase
text = "python programming"
print(text.title()) #Output: Python Programming

#4. capitalize() - capitalizes only the first letter of the string
text = "python programming"
print(text.capitalize()) #Output: Python proogrammming

#5. strip() -   removes leading and trailing whitespaces
text = "   python   "
print(text.strip()) #Output: pythoon

#6. replace() - replaces one substring with another
text = "I love python"
print(text.replace("python", "java")) #Output: I love java

#7. split() - split string into a list
text = "Running,Walking,Sliding"
print(text.split()) #Output: ['Running', 'Walking', 'Sliding']

#8. join() - joins elements of a list into a singe string
fruits = ["Apple", "Banana", "Orange"]
print(", ".join(fruits)) #Output: Apple, Banana, Orange

#9. startwith() - checks wether a string starts with a specific value
text = "python programming"
print(text.startwith("python")) #Output: True

#10. endswith() - checks wether a string ends with a specific value
text = "python programming"
print(text.endswith("programming")) #Output: True

#11. find() - returns an index of the FIRST occurence of a substring
text = "Python Programming"
print(text.find("Programming")) #Output: 7

#12. count() - counts how many times a substring appears
text = "banana"
print(text.count("a")) #Output: 3

#13. isalpha() - checks wether all characters are alphabetic
text = "python"
print(text.isalpha()) #Output: True

#14. isdigit() - checks wether all characters are digits
text = "12345"
print(text.isdigit()) #Output: True'

#15. isalnum() - checks wether all characters are letters or numbers
text = "python123"
print(text.isalnum()) #Output: True

#16. isspace() - checks wether all characters are whitespace
text = "  "
print(text.isspace()) #Output: True