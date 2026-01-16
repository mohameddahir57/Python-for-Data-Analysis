# 🟦 Jan 16: Python Lists Practice

# 1. Creating and Accessing Lists
print("--- 1. Creating & Accessing ---")
my_list = [10, 20, 30, 40, 50]
print(f"Original List: {my_list}")
print(f"First element: {my_list[0]}")
print(f"Last element: {my_list[-1]}")

# 2. Slicing
print("\n--- 2. Slicing ---")
# Syntax: list[start:stop:step]
print(f"Index 1 to 3: {my_list[1:4]}")
print(f"First 3 items: {my_list[:3]}")
print(f"Reversed: {my_list[::-1]}")

# 3. Modifying & Methods
print("\n--- 3. Methods ---")
fruits = ["apple", "banana"]
print(f"Start: {fruits}")

# Append
fruits.append("cherry")
print(f"After append('cherry'): {fruits}")

# Insert
fruits.insert(1, "blueberry")
print(f"After insert(1, 'blueberry'): {fruits}")

# Remove
if "banana" in fruits:
    fruits.remove("banana")
    print(f"After remove('banana'): {fruits}")

# Pop
popped_item = fruits.pop()
print(f"Popped item: {popped_item}")
print(f"List after pop: {fruits}")

# 4. List Comprehension
print("\n--- 4. List Comprehensions ---")
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Original: {numbers}")
print(f"Squares: {squares}")

# ---------------------------------------------------------
# 📝 PRACTICE EXERCISES
# ---------------------------------------------------------

# Exercise 1: Create a list of 3 countries, add one more, then print the list.
print("\n--- Exercise 1 ---")
# Write your code here:


# Exercise 2: Create a list of numbers 1-10. Print only the even numbers using slicing or a loop.
print("\n--- Exercise 2 ---")
# Write your code here:


# Exercise 3: Use a list comprehension to create a list of even numbers from 0 to 20.
print("\n--- Exercise 3 ---")
# Write your code here:

