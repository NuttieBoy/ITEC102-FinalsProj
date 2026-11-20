# ===== CALENDAR =====
# The calendar module works with dates, weekdays, months, and years
import calendar

# Example 1: Print the calendar of a month
print(calendar.month(2026, 11))

# Example 2: Find the weekday of a date (Monday is 0, Sunday is 6)
day_number = calendar.weekday(2026, 11, 19)
print(calendar.day_name[day_number])  # Output: Thursday

# Example 3: Check if a year is a leap year
print(calendar.isleap(2028))  # Output: True
print(calendar.isleap(2026))  # Output: False


# ===== TIME =====
# The time module works with the current time, delays, and measuring how long code takes
import time

# Example 1: Show the current date and time
print(time.strftime("%Y-%m-%d %H:%M:%S"))  # Output: 2026-11-20 14:30:05 (yours will be different)

# Example 2: Pause the program for 1 second
print("Wait for it...")
time.sleep(1)
print("Done!")  # Output: Done!

# Example 3: Measure how long some code takes
start = time.time()
total = 0
for number in range(1, 1000001):
    total += number
end = time.time()
print("Total:", total)  # Output: Total: 500000500000
print(f"It took {end - start:.2f} seconds")  # Output: It took 0.06 seconds (yours will be different)


# ===== JSON =====
# JSON is a text format for storing data. The json module converts Python data to JSON and back
import json

# Example 1: Convert a dictionary to JSON text
student = {"name": "Alice", "age": 20}
text = json.dumps(student)
print(text)  # Output: {"name": "Alice", "age": 20}

# Example 2: Convert JSON text back to a dictionary
data = json.loads(text)
print(data["name"])  # Output: Alice

# Example 3: Save to a file and load it back
with open("student.json", "w") as file:
    json.dump(student, file)
with open("student.json", "r") as file:
    loaded = json.load(file)
print(loaded["age"])  # Output: 20


# ===== MINI PROJECT: STUDY LOG (calendar + time + json) =====
# calendar finds the weekday, time gets the date and the study duration, json saves the result
today = time.localtime()
weekday = calendar.day_name[calendar.weekday(today.tm_year, today.tm_mon, today.tm_mday)]

start = time.time()
time.sleep(1)  # Pretend the student is studying for 1 second
seconds = round(time.time() - start)

session = {"date": time.strftime("%Y-%m-%d"), "weekday": weekday, "seconds": seconds}
with open("study_log.json", "w") as file:
    json.dump(session, file, indent=4)

with open("study_log.json", "r") as file:
    log = json.load(file)
print(f"Studied on {log['weekday']} for {log['seconds']} second(s)")  # Output: Studied on Friday for 1 second(s)
