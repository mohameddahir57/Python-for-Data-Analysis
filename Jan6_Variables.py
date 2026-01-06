# Basics of Variables
# 1. Variable Assignment
name = "Mohamed"
age = 25
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Is Student: {is_student}")

# 2. Variable Naming Rules (PEP 8)
# - Use lowercase with underscores (snake_case)
# - Cannot start with a number
# - Case-sensitive (age, Age, and AGE are different)

user_name = "data_analyst"
# 1st_user = "invalid" # Error

# 3. Dynamic Typing
# You can change the type of a variable by assigning a new value
x = 10
print(type(x))
x = "Now I am a string"
print(type(x))

# --- Practice Exercises ---
# 1. Create a variable called 'city' and assign your city name to it.
# 2. Create a variable 'population' and assign a number.
# 3. Print a sentence using these variables: "The population of [city] is [population]."

# WRITE YOUR CODE BELOW

# 1. Create a variable called 'city'
city = "Mogadishu"

# 2. Create a variable 'population'
population = 2500000

# 3. Print a sentence using these variables
print(f"The population of {city} is {population}.")

