#                                               < - - - Easy Examples - - - >

# 1. List Function: append()

list = ["Coffee", "Juice", "Milk"]

list.append("Tea")

print (list)

# Output: ['Coffee', 'Juice', 'Milk', 'Tea']

# 2. List Function: remove()

list = ["Coffee", "Juice", "Milk"]

list.remove("Juice")

print (list)

# Output: ['Coffee', 'Milk']

# 3. List Function: clear()

list = ["Coffee", "Juice", "Milk"]

list.clear()

print (list)

# Output: []

# 4. List Function: sort()

numbers = [2, 3, 1, 4, 6, 7, 9]

numbers.sort()

print (numbers)

# Output: [1, 2, 3, 4, 6, 7, 9]



#                                               < - - - Intermediate Examples - - - >

# 1. List Comprehension

numbers = [12, 7, 15, 20, 8, 33, 10, 5, 18]

even_squares = [num ** 2 for num in numbers if num % 2 == 0]

print("Original Numbers:", numbers)
print("Squared Even Numbers:", even_squares)

# Output: 
# Original Numbers: [12, 7, 15, 20, 8, 33, 10, 5, 18]
# Squared Even Numbers: [144, 400, 64, 100, 324]

# 2. String Methods

text = "   Python Programming is FUN and Interesting!   "

cleaned_text = text.strip()

lowercase_text = cleaned_text.lower()

modified_text = lowercase_text.replace("fun", "powerful")

word_count = len(modified_text.split())

contains_python = "python" in modified_text

print("Original Text:", text)
print("Cleaned Text:", cleaned_text)
print("Modified Text:", modified_text)
print("Word Count:", word_count)
print("Contains Python:", contains_python)

# Output:
# Original Text:    Python Programming is FUN and Interesting!   
# Cleaned Text: Python Programming is FUN and Interesting!
# Modified Text: python programming is powerful and interesting!
# Word Count: 6
# Contains Python: True


#                                               < - - - Hard Examples - - - >

# 1. Tuples, sets, dictionary  

students = (
    ("Alex", 92),
    ("Mark", 78),
    ("John", 65),
    ("Chris", 88),
    ("Daniel", 95),
    ("James", 72)
)

passed = {name for name, grade in students if grade >= 75}

failed = {name for name, grade in students if grade < 75}

excellent = {name for name, grade in students if grade >= 90}

average = sum(grade for name, grade in students) / len(students)

average_performers = passed - excellent

print("Passed Students:", passed)
print("Failed Students:", failed)
print("Excellent Students:", excellent)
print("Average Grade:", round(average, 2))
print("Average Performers:", average_performers)

# Output:
# Passed Students: {'Alex', 'Mark', 'Chris', 'Daniel', 'James'}
# Failed Students: {'John'}
# Excellent Students: {'Alex', 'Daniel'}
# Average Grade: 81.67
# Average Performers: {'Mark', 'Chris', 'James'}

# 2. Tuples, sets, dictionary

inventory = {
    "Laptop": {"price": 35000, "stock": 5},
    "Mouse": {"price": 500, "stock": 20},
    "Keyboard": {"price": 1200, "stock": 10},
    "Monitor": {"price": 8500, "stock": 3}
}


sales = {
    "Laptop": 2,
    "Mouse": 8,
    "Keyboard": 4,
    "Monitor": 1
}

total_revenue = 0

for item, quantity in sales.items():

    if item in inventory:
        if quantity <= inventory[item]["stock"]:

            revenue = quantity * inventory[item]["price"]
            total_revenue += revenue

            inventory[item]["stock"] -= quantity

            print(f"{item}: Sold {quantity} units")
            print(f"Revenue: ₱{revenue:,}")

        else:
            print(f"{item}: Insufficient stock!")

print("\n===== INVENTORY REPORT =====")

for item, details in inventory.items():
    print(f"{item}: {details['stock']} units remaining")

print(f"\nTotal Revenue: ₱{total_revenue:,}")

# Output: 
# Laptop: Sold 2 units
# Revenue: ₱70,000
# Mouse: Sold 8 units
# Revenue: ₱4,000
# Keyboard: Sold 4 units
# Revenue: ₱4,800
# Monitor: Sold 1 units
# Revenue: ₱8,500

# ===== INVENTORY REPORT =====
# Laptop: 3 units remaining
# Mouse: 12 units remaining
# Keyboard: 6 units remaining
# Monitor: 2 units remaining

# Total Revenue: ₱87,300