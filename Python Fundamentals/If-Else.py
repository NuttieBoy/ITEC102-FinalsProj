#if statements are used to make decisions in Python. They allow you to execute certain blocks of code based on specific conditions.
#else statements are used in conjunction with if statements to provide an alternative block of code to execute when the condition in the if statement is not met.
grade = int(input("Enter your grade:"))
passing_grade = 60
if grade >= passing_grade:
    print("Congratulations! You passed the course.")
else: 
    print("Sorry, you did not pass the course. Better luck next time!")
# Logical operators are used to combine multiple conditions in if statements. The three main logical operators in Python are and, or, and not.
# The and operator returns True if both conditions are true, while the or operator returns True if at least one of the conditions is true. The not operator negates the truth value of a condition.
print ("Special Assistance for those aged 15 and below or 60 and above")
age = int(input("Enter your age:"))
if age <= 15 and age >= 0 or age >= 60 and age <= 120:
    print("You are eligible for special assistance.")
else:
    print("You are not eligible for special assistance.")
is_student = True
is_teacher = False
print (not is_student)
print (not is_teacher)
# if-elif-else statements allow you to check multiple conditions in a sequential manner. The elif (short for "else if") statement is used to specify additional conditions to check if the previous conditions are not met.
score = int(input("Enter your score:"))
if score >= 90:
    print("You got an A!")
elif score >= 60:
    print("You passed the course.")
else:
    print("You failed the course.")
#Multiple if statements are independent of one another. Each condition is evaluated separately, even if a previous condition is already True
number = 20
if number > 10:
    print("The number is greater than 10.")
if number % 2 == 0:
    print("The number is even.")
if number < 30:
    print("The number is less than 30.")
# Nested if statements are if statements placed inside another if statement. They allow you to create more complex decision-making structures by checking additional conditions within the scope of a previous condition.
# Nested if-else statements are if-else statements placed inside another if statement. They allow you to create more complex decision-making structures by providing alternative blocks of code to execute based on additional conditions.
age = 17
has_id = True
if age >= 18:
    if has_id:
        print("You are eligible to enter the club.")
else:
    print("You need to show your ID to enter the club.")
# Variables canalso be manipulated under the if statement. This allows you to modify the value of a variable based on certain conditions.
Grade = 65
joined_Seminar = True
joined_Workshop = True
if joined_Seminar == True:
    Grade = Grade + 5
if joined_Workshop == True:
    Grade = Grade + 5
print("Final Grade:", Grade)