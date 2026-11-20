
# 1. Variables & Data Types -> Storing different kinds of values
name = "Alex"                           # 'str' (string) stores text inside quotes
age = 25                                # 'int' (integer) stores whole numbers
height = 5.9                            # 'float' stores decimal numbers
is_student = True                       # 'bool' (boolean) stores True or False
print("1. Types:", type(name), type(age)) # Output: 1. Types: <class 'str'> <class 'int'>

# 2. F-Strings -> Injecting variables directly into text
greeting = f"Hi, I'm {name} and I'm {age}." # 'f' before quotes lets you put variables in {}
print("2. F-String:", greeting)         # Output: 2. F-String: Hi, I'm Alex and I'm 25.

# 3. Basic Math & Modulo -> Calculating numbers and remainders
total = 10 + 5 * 2                      # Follows PEMDAS: multiplies first (10), then adds 10
remainder = 10 % 3                      # '%' (modulo) divides 10 by 3 and returns the remainder (1)
print("3. Math:", total, "| Remainder:", remainder) # Output: 3. Math: 20 | Remainder: 1

# 4. Conditionals (if / elif / else) -> Making decisions in code
temp = 32                               # Variable storing temperature in Celsius
if temp > 30:                           # Checks first condition; runs indented code if True
    weather = "Hot"                     # Assigns "Hot" because 32 > 30
elif temp >= 20:                        # Checked only if the 'if' above was False
    weather = "Warm"
else:                                   # Fallback if all conditions above are False
    weather = "Cold"
print("4. Weather:", weather)           # Output: 4. Weather: Hot

# 5. For Loops -> Repeating an action a set number of times
total_sum = 0                           # Accumulator variable starting at 0
for num in range(1, 5):                 # Loops through numbers 1, 2, 3, 4 (stops before 5)
    total_sum += num                    # Adds current 'num' to 'total_sum' (0+1+2+3+4)
print("5. For Loop Sum:", total_sum)    # Output: 5. For Loop Sum: 10

# 6. While Loops -> Repeating an action until a condition becomes False
count = 3                               # Starting counter variable
while count > 0:                        # Keeps running as long as 'count' is above 0
    count -= 1                          # Subtracts 1 each loop so it doesn't run forever
print("6. While Loop End:", count)      # Output: 6. While Loop End: 0

# 7. Functions -> Reusable blocks of code that take inputs and return outputs
def add_tax(price, tax_rate=0.12):      # 'def' creates a function; 'tax_rate' defaults to 0.12
    final = price + (price * tax_rate)  # Calculates total price with tax
    return round(final, 2)              # Sends the rounded result back out of the function

bill = add_tax(100)                     # Calls the function with 100 and saves result in 'bill'
print("7. Function Result:", bill)      # Output: 7. Function Result: 112.0

# 8. Dictionaries -> Storing data as connected Key-Value pairs
user = {"username": "dev_ana", "xp": 50} # Curly braces {} hold "key": value pairs
user["xp"] += 25                        # Looks up "xp" key and adds 25 to its value
user["level"] = 2                       # Adds a brand-new key "level" with value 2
print("8. Dictionary:", user)           # Output: 8. Dictionary: {'username': 'dev_ana', 'xp': 75, 'level': 2}
