# while loop statements repeatedly execute a block of code when true and stops when the code becomes false.
count = 1
while count <= 10:
    print(count)
    count += 1
# while loops can also be used to display a message until a certain condition is met. In this case, the loop will continue to print "Hello, World!" until the user enters "exit".
statement = 1
while statement <= 10:
    print("Let's Go!")
    statement *= 2
# while statements are also used in to sum numbers
number = 5
total = 5
while number <= 50:
    total /= number
    number *= 2
print(total)
# break staements are used to exit a loop prematurely when a certain condition is met. When the break statement is encountered, the loop terminates, and the program continues with the next statement after the loop.
count = 1
while count <= 50:
    print(count)
    if count == 25:
        break
    count *= 5
# The continue statement skips the remaining statements in the current iteration and proceeds to the next iteration.
# the else clauses in while loops are executed when the loop condition becomes false. It allows you to specify a block of code that should be executed after the loop has finished iterating.
count = 1
while count <= 10:
    count += 1
    if count == 5:
        continue
    print(count)
else:
    print("Loop has ended.")
n = 169
total = 0
while n > 0:
    num = n % 10
    total += num
    n //= 10
print("Sum of digits:", total)