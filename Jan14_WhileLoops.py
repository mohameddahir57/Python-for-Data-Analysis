# 📅 Jan 14 — Day 14: while Loops
# Topic: Conditional Repetition

"""
A while loop repeats a block of code as long as a condition is True.
It is useful when you don't know exactly how many times you need to repeat.
"""

# ---------------------------------------------------------
# 1. Basic while loop
# ---------------------------------------------------------
print("--- 1. BASIC WHILE LOOP ---")
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1  # Crucial: If you don't increment, the loop never ends!

# ---------------------------------------------------------
# 2. while loop with User Input
# ---------------------------------------------------------
print("\n--- 2. WHILE WITH INPUT ---")
# Simulating a user password check
correct_pass = "python123"
user_input = ""
attempts = 0

# In a real scenario, this would use input(), but here we use a list to simulate
simulated_inputs = ["123", "hello", "python123"]

while user_input != correct_pass and attempts < 3:
    user_input = simulated_inputs[attempts]
    print(f"Attempt {attempts + 1}: Entered '{user_input}'")
    
    if user_input == correct_pass:
        print("Access Granted!")
    else:
        print("Wrong password. Try again.")
    attempts += 1

# ---------------------------------------------------------
# 3. break and continue
# ---------------------------------------------------------
print("\n--- 3. BREAK AND CONTINUE ---")
num = 0
print("Printing odd numbers below 10 using continue:")
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)

# ---------------------------------------------------------
# 📝 PRACTICE EXERCISES
# ---------------------------------------------------------

"""
EXERCISE 1: Number Summer
Write a loop that adds numbers from 1 to 10.
"""
print("\nExercise 1: Sum 1-10")
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print(f"Sum is: {total}")

"""
EXERCISE 2: Stop at 0
Decrement a variable from 10 to 1, but stop immediately if it reaches 0.
"""
print("\nExercise 2: Countdown with break")
n = 10
while n > -2 : # Designed to go past 0
    if n == 0:
        print("Zero reached! Stopping.")
        break
    print(n)
    n -= 1
