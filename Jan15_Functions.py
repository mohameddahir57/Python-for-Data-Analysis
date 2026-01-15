# 📅 Jan 15 — Day 15: Functions
# Topic: Reusable Code Blocks

"""
Functions are named blocks of code designed to do one specific job.
They help make our code cleaner, more organized, and reusable.
"""

# ---------------------------------------------------------
# 1. Defining and Calling a Function
# ---------------------------------------------------------
print("--- 1. DEFINING A FUNCTION ---")
def greet():
    """Simple function that prints a greeting."""
    print("Hello! Welcome to the Python Functions lesson.")

# Call the function
greet()

# ---------------------------------------------------------
# 2. Functions with Parameters
# ---------------------------------------------------------
print("\n--- 2. PARAMETERS AND ARGUMENTS ---")
def welcome_user(name):
    print(f"Welcome back, {name}!")

welcome_user("Mohamed")
welcome_user("Data Enthusiast")

# ---------------------------------------------------------
# 3. Returning Values
# ---------------------------------------------------------
print("\n--- 3. RETURN VALUES ---")
def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(15, 25)
print(f"The result of 15 + 25 is: {result}")

# ---------------------------------------------------------
# 4. Default Parameter Values
# ---------------------------------------------------------
print("\n--- 4. DEFAULT PARAMETERS ---")
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("Buddy")          # Uses default "dog"
describe_pet("Misty", "cat")    # Overrides default

# ---------------------------------------------------------
# 📝 PRACTICE EXERCISES
# ---------------------------------------------------------

"""
EXERCISE 1: Squared Number
Create a function 'square' that takes one number and returns its square.
"""
print("\nExercise 1: Squaring")
def square(n):
    return n * n

print(f"Square of 4 is: {square(4)}")

"""
EXERCISE 2: Data Analyzer
Create a function 'analyze_temp' that takes a temperature.
- If temp > 25, return "Hot"
- Else, return "Cool"
"""
print("\nExercise 2: Temp Analyzer")
def analyze_temp(t):
    if t > 25:
        return "Hot"
    else:
        return "Cool"

print(f"Temperature 30 is {analyze_temp(30)}")
print(f"Temperature 20 is {analyze_temp(20)}")
