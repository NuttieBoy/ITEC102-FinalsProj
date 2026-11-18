# List s an ordered, mutable collection of items enclosed in square brackets ([])
fruits = ["apple", "banana", "cherry"]
# Each item in a list has an index. Python uses zero-based indexing, meaning the first element has an index of 0
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana  
print(fruits[2])  # Output: cherry
fruits[1] = "blueberry"  # Modifying an element in the list
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
fruits.remove("cherry")  # Removing an element from the list
print(fruits)  # Output: ['apple', 'blueberry']
fruits.append("date")  # Adding an element to the end of the list
print(fruits)  # Output: ['apple', 'blueberry', 'date']
# Lists can contain elements of different data types, including numbers, strings, and even other lists
numbers = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")
sum = 0
for number in numbers: # Getting the average in a list
    sum += number
average = sum / len(numbers) # Len() function returns the number of items in a list
print(f"The average of the numbers in the list is: {average}")
reverse_list = reversed(numbers) # Reversing a list
print(list(reverse_list))
