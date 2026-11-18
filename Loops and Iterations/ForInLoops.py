# The range() function generates a sequence of integers. It does not display the numbers by itself. Instead, it is commonly used with a for loop.
# range(stop) The sequence starts at 0 by default and stops before the value of stop.
for i in range(6):
    print(i)
# range(start, stop) The sequence starts at the value of start and stops before the value of stop.
for i in range(3, 8):
    print(i)
# range(start, stop, step) The sequence starts at the value of start, stops before the value of stop, and increments by the value of step.
for i in range(2, 10, 2):
    print(i)    
# negative step counts backwards
for i in range(10, 0, -1):
    print(i)
# Multiplication Table Example
number = int(input("Enter a number: "))
for i in range(1, 11):
    product = number * i
    print(f"{number} x {i} = {product}")