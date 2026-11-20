from decimal import Decimal

# 1. Basic Float
item_price = 19.99
tax = 2.40
total = item_price + tax
print("1. Float Total:", total)         # Output: 1. Float Total: 22.389999999999997

# 2. Rounding Floats
raw_average = 88.6666667
clean_avg = round(raw_average, 2)
print("2. Rounded:", clean_avg)         # Output: 2. Rounded: 88.67

# 3. Exact Decimal (vs. Float Glitch)
print("   Float Glitch:", 0.1 + 0.2)    # Output:    Float Glitch: 0.30000000000000004
exact_sum = Decimal("0.1") + Decimal("0.2")
print("3. Exact Decimal:", exact_sum)   # Output: 3. Exact Decimal: 0.3

# 4. String Formatting (F-Strings)
channel = "CodeWithMe"
subs = 1500
banner = f"Welcome to {channel}! Subs: {subs}"
print("4. F-String:", banner)           # Output: 4. F-String: Welcome to CodeWithMe! Subs: 1500

# 5. String Methods
raw_email = "  User@Email.COM  "
clean_email = raw_email.strip().lower()
print("5. Cleaned:", clean_email)       # Output: 5. Cleaned: user@email.com

# 6. String Slicing
video_id = "VID-2026-99"
year = video_id[4:8]
print("6. Sliced Year:", year)          # Output: 6. Sliced Year: 2026

# 7. List []
tags = ["python", "coding", "tutorial"]
tags.append("beginner")
print("7. List:", tags)                 # Output: 7. List: ['python', 'coding', 'tutorial', 'beginner']

# 8. Set {}
viewers = {"Ana", "Ben", "Ana", "Cara"}
print("8. Unique Set:", viewers)        # Output: 8. Unique Set: {'Ana', 'Ben', 'Cara'}

# 9. Dictionary {key: value}
video = {"title": "Python Basics", "views": 100}
video["views"] += 50
print("9. Dictionary:", video)          # Output: 9. Dictionary: {'title': 'Python Basics', 'views': 150}
