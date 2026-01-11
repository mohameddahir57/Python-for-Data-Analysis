# 📅 Jan 11 — Day 11: if / else Statements
# Topic: Control Flow - Decisions in Python

"""
Control Flow is how a program decides which code to run based on conditions.
In Python, we use 'if', 'elif' (else if), and 'else' to make decisions.
"""

# 1. Simple 'if' statement

age = 20

print("--- 1. Simple IF ---")  # Indentation is important!
if age >= 18:   # Every if, elif, and else line MUST end with a colon.
    print("You are an adult.")  
    print("You can vote.")  

# 2. 'if - else' statement

print("\n--- 2. IF-ELSE ---")  # Indentation is important!
score = 45

if score >= 50:   # Every if, elif, and else line MUST end with a colon.
    print("Pass")
else:   
    print("Fail")

# 3. 'if - elif - else' (Multiple conditions)

print("\n--- 3. IF-ELIF-ELSE ---")
temperature = 25

if temperature > 30:   # Every if, elif, and else line MUST end with a colon.
    print("It's hot outside.")
elif temperature >= 20:   
    print("It's a pleasant day.")
elif temperature >= 10:   
    print("It's a bit chilly.")
else:   
    print("It's cold.")

# 4. Nested 'if' statements

print("\n--- 4. NESTED IF ---")
user_has_ticket = True 
user_has_id = False

if user_has_ticket:
    print("Ticket verified.")
    if user_has_id:
        print("Welcome to the event!")
    else:
        print("Please show your ID to enter.")
else:
    print("No ticket, no entry.")

# 5. Shorthand 'if' (Ternary Operator)

print("\n--- 5. SHORTHAND ---")
number = 10
status = "Even" if number % 2 == 0 else "Odd"
print(f"The number {number} is {status}.")

# 📝 PRACTICE EXERCISES

"""
EXERCISE 1: Number Sign
Write a condition that checks if a number is positive, negative, or zero.
"""
num = 7
# Your code here...
if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print(f"{num} is Zero")


"""
EXERCISE 2: Grading System
Create a script that takes a marks variable (0-100) and prints:
- "A" for 90-100
- "B" for 80-89
- "C" for 70-79
- "Fail" for below 70
"""
marks = 85
# Your code here...
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: Fail")

print("\n--- Practice Completed! ---")
