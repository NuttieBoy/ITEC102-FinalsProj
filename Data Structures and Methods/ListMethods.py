
# 1. .append() -> Adds a single item to the very end
fruits = ["apple", "banana"]    # 'fruits' stores a list of 2 strings
fruits.append("mango")          # Adds "mango" to the end of 'fruits'
print("1. append:", fruits)     # Output: 1. append: ['apple', 'banana', 'mango']

# 2. .insert() -> Adds an item at a specific position (index)
fruits = ["apple", "banana"]    # Reset 'fruits' list
fruits.insert(1, "orange")      # Puts "orange" at index 1 (the second spot)
print("2. insert:", fruits)     # Output: 2. insert: ['apple', 'orange', 'banana']

# 3. .remove() -> Deletes the first matching value it finds
fruits = ["apple", "banana"]    # Reset 'fruits' list
fruits.remove("apple")          # Searches for "apple" and deletes it
print("3. remove:", fruits)     # Output: 3. remove: ['banana']

# 4. .clear() -> Empties the entire list
fruits = ["apple", "banana"]    # Reset 'fruits' list
fruits.clear()                  # Wipes all items inside 'fruits'
print("4. clear:", fruits)      # Output: 4. clear: []

# 5. .pop() -> Removes an item by index AND saves it to a variable
fruits = ["apple", "banana", "mango"]  # List with 3 items (indices 0, 1, 2)
eaten = fruits.pop(1)                  # Removes index 1 ("banana") and stores it in 'eaten'
print("5. pop list:", fruits)          # Output: 5. pop list: ['apple', 'mango']
print("5. popped item:", eaten)        # Output: 5. popped item: banana

# 6. .count() -> Counts how many times a specific value appears
basket = ["apple", "mango", "apple"]   # 'basket' has duplicate strings
total = basket.count("apple")          # Counts "apple" occurrences, saves number in 'total'
print("6. count:", total)              # Output: 6. count: 2

# 7. .extend() -> Unpacks another list and merges its items into the first list
local_fruits = ["mango", "banana"]     # First list variable
imported = ["apple", "grape"]          # Second list variable
local_fruits.extend(imported)          # Takes items out of 'imported' and adds to 'local_fruits'
print("7. extend:", local_fruits)      # Output: 7. extend: ['mango', 'banana', 'apple', 'grape']

# 8. .sort(key=...) -> Reorders the list using a custom rule
fruits = ["banana", "fig", "apple"]    # Unsorted list of words with different lengths
fruits.sort(key=len)                   # Sorts 'fruits' from shortest word to longest using len()
print("8. sort by length:", fruits)    # Output: 8. sort by length: ['fig', 'apple', 'banana']
