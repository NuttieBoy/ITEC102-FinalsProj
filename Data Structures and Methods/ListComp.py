
# 1. Capitalizing -> Transforms every string in a list
fruits = ["apple", "banana", "mango"]          # Original list of lowercase strings
caps = [f.upper() for f in fruits]             # Takes each fruit 'f', makes it uppercase, builds 'caps'
print("1. uppercase:", caps)                   # Output: 1. uppercase: ['APPLE', 'BANANA', 'MANGO']

# 2. Math on Numbers -> Multiplies every number in a list
prices = [10, 20, 30]                          # Original list of integers
doubled = [p * 2 for p in prices]              # Multiplies each price 'p' by 2, stores in 'doubled'
print("2. doubled:", doubled)                  # Output: 2. doubled: [20, 40, 60]

# 3. Extracting Lengths -> Counts characters of each word
words = ["fig", "apple", "banana"]             # List of strings with varying lengths
lengths = [len(w) for w in words]              # Gets character count of each word 'w'
print("3. lengths:", lengths)                  # Output: 3. lengths: [3, 5, 6]

# 4. Adding Labels -> Combines static text with each item
names = ["Ana", "Ben", "Cara"]                 # List of first names
tags = ["User: " + n for n in names]           # Attaches "User: " before each name 'n'
print("4. tags:", tags)                        # Output: 4. tags: ['User: Ana', 'User: Ben', 'User: Cara']

# 5. Filtering Numbers -> Keeps only items that pass a test
nums = [4, 15, 8, 23, 12]                      # Mixed list of small and large numbers
big_nums = [n for n in nums if n > 10]         # Keeps 'n' ONLY IF it is greater than 10
print("5. big_nums:", big_nums)                # Output: 5. big_nums: [15, 23, 12]

# 6. Filtering + Transforming -> Filters first, then modifies
fruits = ["apple", "fig", "mango", "kiwi"]     # Original list of fruits
long_caps = [f.upper() for f in fruits if len(f) > 4] # Uppercases 'f' ONLY IF longer than 4 letters
print("6. long_caps:", long_caps)              # Output: 6. long_caps: ['APPLE', 'MANGO']

# 7. If-Else Logic -> Changes items differently based on a condition
scores = [85, 60, 92, 70]                      # List of exam scores
# Notice: When using 'if-else', the condition moves BEFORE the 'for' loop
results = ["Pass" if s >= 75 else "Fail" for s in scores] # Labels score 's' as Pass or Fail
print("7. results:", results)                  # Output: 7. results: ['Pass', 'Fail', 'Pass', 'Fail']

# 8. Flattening Nested Lists -> Unpacks a 2D grid into a single flat list
matrix = [[1, 2], [3, 4], [5, 6]]              # A list containing 3 inner lists (rows)
flat = [num for row in matrix for num in row]  # Loops through each 'row', then each 'num' inside it
print("8. flat:", flat)                        # Output: 8. flat: [1, 2, 3, 4, 5, 6]
