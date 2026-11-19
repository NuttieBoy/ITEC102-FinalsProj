# A list of lists, also called a nested list, is a list whose elements are themselves lists. Nested lists are useful for organizing data into rows and columns, similar to a table, spreadsheet, or matrix.
members = [ # Syntax: list_name = [[element1, element2, ...], [element1, element2, ...], ...]
    ["Alice", 25, "Engineer"],
    ["Bob", 30, "Designer"],
    ["Charlie", 22, "Student"]
]
# To access a specific element in a nested list, you can use multiple indices. The first index specifies the outer list, and the second index specifies the inner list.
print(members[0][0])  # Output: Alice
print(members[1][1])  # Output: 30
print(members[2][2])  # Output: Student
# You can also use nested loops to iterate through the elements of a nested list. The outerloop iterates through the outer list, and the inner loop iterates through each inner list.

for row in members:
    for element in row:
        print(element) # Output: Alice 25 Engineer Bob 30 Designer Charlie 22 Student
# A nested list can be modified by accessing its elements using indices. You can change the value of an element in a nested list by specifying the indices of the outer and inner lists.
members[0][1] = 26  # Change Alice's age to 26
print(members[0][1])  # Output: 26

# Another example of a nested list is a 2D matrix, which can be represented as a list of lists. Each inner list represents a row of the matrix, and each element in the inner list represents a column of the matrix.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(element) # Output: 1 2 3 4 5 6 7 8 9

# Summary: A list of lists, or nested list, is a powerful data structure that allows you to organize data in a tabular format. You can access and modify elements using indices, and you can use nested loops to iterate through the elements of the nested list.
