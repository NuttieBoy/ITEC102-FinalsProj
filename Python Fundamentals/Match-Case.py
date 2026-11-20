# Match statements allows you to perform pattern matching on values. They provide a more concise and readable way to handle multiple conditions compared to traditional if-elif-else statements.
# | is used to seperate values in a case.
grade = "F"
match grade:
    case "A" | "B":
        print("Excellent!")
    case "C" | "D":
        print("Satisfactory.")
    case "F":
        print("Failed.")
    case _:
        print("Invalid grade.")
# Output Failed
