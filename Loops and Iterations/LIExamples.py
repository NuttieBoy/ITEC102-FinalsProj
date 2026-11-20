# Easy: While Loop count to 10
count = 1
while count <= 10:
    print(count)
    count += 1 # Output: 1 2 3 4 5 6 7 8 9 10

# Easy: While Loop count to 10 in reverse
count = 10
while count >= 1:
    print(count)
    count -= 1 # Output: 10 9 8 7 6 5 4 3 2 1

# Easy: For Loop count to 10
for count in range(1, 11):
    print(count) # Output: 1 2 3 4 5 6 7 8 9 10

# Easy: For Loop count to 10 in reverse
for count in range(10, 0, -1):
    print(count) # Output: 10 9 8 7 6 5 4 3 2 1

# Medium: While Loop to sum numbers from 1 to 100
total = 0
count = 1
while count <= 100:
    total += count
    count += 1
print(f"The sum of numbers from 1 to 100 is: {total}") # Output: The sum of numbers from 1 to 100 is: 5050

# Medium: List of numbers and sum them using a for loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for number in numbers:
    total += number
print(f"The sum of the numbers in the list is: {total}") # Output: The sum of the numbers in the list is: 55

# Hard: Nested loops to print a multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j}", end="\t")
    print() # Output: Multiplication table from 1 to 10

# Hard: Nested loops to print a pattern
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print() # Output: A right-angled triangle pattern of asterisks