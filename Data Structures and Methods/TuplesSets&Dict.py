#<--- Tuple --->
# A tuple is an immutable colection of elements. Datas inside tuples cannot be added, removed, or modified. Can store diff. data types.

# <--- Creating a Tuple --->

#Syntax: tuple_name = (item1, item2, item3)
#key note: "()" parantheses are used in creating tuples

#Example:
tuple = (1, 2, 3)
print(tuple) #Output: (1, 2, 3)

#Tuples can be accessed just like a list
tuple = (1, 2, 3)
print(tuple{1}) #Output: 2
#key note: Tuples uses zero-based index

#Modifying a tuple will always result in 'TypeError'

#<--- Tuple Methods --->

#1. count() - counts the number of occurrences of a value
number = (1, 2, 2, 3, 2, 4)
print(number.count(2)) #Output: 3

#2. index() - returns the index of the first occurrence of a value
names = (Ana, John, Jane)
print(names.index(John)) #Output: 1


#<--- Set --->
# A set is an unordered collection of unique elements. Duplicate values are automatically removed.

#<--- Creating a Set --->

#Syntax: set_name = {item1, item2, item3}
#Key note: "{}" curly braces are used in creating sets

#Example:
numbers = {1, 2, 3, 2, 4, 5}
print(numbers) #Output: {1, 2, 3, 4, 5}

#Elements can be added and removed in a set

#<--- Set Operations --->

#1. Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2) #Output: {1, 2, 3, 4, 5}

#2. Intersection 
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 & set2) #Output: 3

#3. Difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 - set2) #Output: {1, 2}


#<--- Dictionary --->

#A dictionary is a collection of key-value pairs. Each key is unique and is used to access its corresponding value.

#<--- Creating a Dictionary --->

#Syntax: dictionary = {
    "key": value
}

#Example: 
student = {
    "name": "Ana",
    "age": 18,
    "course": "Computer Science"
}
print(student) #Output: {'name': 'Ana', 'age': 18, 'course': 'Computer Science'}

#1. Accessing Values
student = {
    "name": "Ana",
    "age" : 18
}
print(student["name"]) #Output: Ana

#2. Modifying Values
student = {
    "name": "Ana",
    "age": 18
}

student["age"] = 19

print(student) #Output: {'name': 'Ana', 'age': 19}

#3. Adding a new Key-Value Pair
student = {
    "name": "Ana"
}

student["course"] = "Computer Science"

print(student) #Output: {'name': 'Ana', 'course': 'Computer Science'}

#4. Removing an Entry
student = {
    "name": "Ana"
    "age": 18
}

student.pop("age")

print(student) #Output: {'name': 'Ana'}

#<--- Common Dictionary Methods --->

#1. keys() - Return all keys
#2. values() - Return all values
#3. items() - Returns all key-value pairs
#4. get(key) - Returns the value associated with a key
#5. pop(key) - Removes a key-value pair
#6. update() - 	Updates or adds key-value pairs
#7. clear() - 	Removes all entries