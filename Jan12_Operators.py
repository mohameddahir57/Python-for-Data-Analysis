# 📅 Jan 12 — Day 12: Comparison & Logical Operators
# Topic: Making Complex Decisions

"""
In this lesson, we learn how to compare values and combine multiple conditions.
These are the building blocks of any decision-making logic in Python.
"""

# ---------------------------------------------------------
# 1. Comparison Operators
# ---------------------------------------------------------
# Used to compare two values. They return a Boolean (True or False).

a = 10
b = 5

print("--- 1. COMPARISON OPERATORS ---")
print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")   # Equal to
print(f"a != b: {a != b}")   # Not equal to
print(f"a > b : {a > b}")    # Greater than
print(f"a < b : {a < b}")    # Less than
print(f"a >= 10: {a >= 10}") # Greater than or equal to
print(f"b <= 5 : {b <= 5}")  # Less than or equal to

# ---------------------------------------------------------
# 2. Logical Operators
# ---------------------------------------------------------
# Used to combine multiple conditions.

x = 7
y = 12

print("\n--- 2. LOGICAL OPERATORS ---")
# AND: Both must be True
print(f"(x > 5 and y < 15)  : {x > 5 and y < 15}") 

# OR: At least one must be True
print(f"(x > 10 or y > 10)  : {x > 10 or y > 10}") 

# NOT: Reverses the result
print(f"not(x == 7)         : {not(x == 7)}")


# ---------------------------------------------------------
# 3. Practical Example: Admission Criteria
# ---------------------------------------------------------
print("\n--- 3. PRACTICAL EXAMPLE ---")
age = 22
has_license = True

if age >= 18 and has_license:
    print("You can rent a car.")
else:
    print("You cannot rent a car.")

# ---------------------------------------------------------
# 📝 PRACTICE EXERCISES
# ---------------------------------------------------------

"""
EXERCISE 1: Range Checker
Check if a number is between 10 and 20 (inclusive).
"""
num = 15
if num >= 10 and num <= 20:
    print(f"{num} is in range.")
else:
    print(f"{num} is out of range.")

"""
EXERCISE 2: Weekend or Weekday
Create a boolean variable 'is_weekend'. If it is NOT weekend, print "Go to work".
"""
is_weekend = False
if not is_weekend:
    print("Go to work")
else:
    print("Enjoy the weekend!")
