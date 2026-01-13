# 📅 Jan 13 — Day 13: for Loops
# Topic: Iterating through Data

"""
For loops are used to repeat a block of code a specific number of times
or to iterate over items in a list, string, or range.
"""

# ---------------------------------------------------------
# 1. Using range()
# ---------------------------------------------------------
# range(stop) -> 0 to stop-1
# range(start, stop) -> start to stop-1
# range(start, stop, step) -> start to stop-1 with step increments

print("--- 1. RANGE FUNCTION ---")
print("Numbers 0 to 4:")
for i in range(5):
    print(i)

print("\nNumbers 2 to 6:")
for i in range(2, 7):
    print(i)

print("\nEven numbers 2 to 10:")
for i in range(2, 11, 2):
    print(i)

# ---------------------------------------------------------
# 2. Iterating over a Sequence
# ---------------------------------------------------------
print("\n--- 2. ITERATING OVER A SEQUENCE ---")
word = "Python"
print(f"Characters in '{word}':")
for char in word:
    print(char.upper())

# ---------------------------------------------------------
# 3. Practical Example: Summing Numbers
# ---------------------------------------------------------
print("\n--- 3. PRACTICAL EXAMPLE: SUMMING ---")
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print(f"Total sum is: {total}")

# ---------------------------------------------------------
# 📝 PRACTICE EXERCISES
# ---------------------------------------------------------

"""
EXERCISE 1: Multiplication Table
Print the multiplication table of 5 (from 1 to 10).
"""
print("\nExercise 1: 5x Table")
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")

"""
EXERCISE 2: Countdown
Write a loop that counts down from 5 to 1.
"""
print("\nExercise 2: Countdown")
for i in range(5, 0, -1):
    print(i)
