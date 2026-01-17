# ------------------------------------------------------------------------------------
# 🐍 Python Tuples Practice
#
# A Tuple is a collection which is ordered and unchangeable.
# Written with round brackets: (item1, item2, item3)
# ------------------------------------------------------------------------------------

print("\n--- 1. Creating Tuples ---")
my_tuple = ("apple", "banana", "cherry")
print(f"Tuple: {my_tuple}")
print(f"Type: {type(my_tuple)}")

# Single item tuple (Remember the comma!)
single_tuple = ("apple",)
print(f"Single Tuple: {single_tuple}, Type: {type(single_tuple)}")

not_tuple = ("apple")
print(f"Not a Tuple: {not_tuple}, Type: {type(not_tuple)}")


print("\n--- 2. Accessing Items ---")
print(f"First item: {my_tuple[0]}")
print(f"Last item: {my_tuple[-1]}")
print(f"Slicing [0:2]: {my_tuple[0:2]}")


print("\n--- 3. Updating Tuples (Workaround) ---")
# Tuples are immutable, so we convert to list -> change -> back to tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(f"Original was (apple, banana, cherry), Updated: {x}")


print("\n--- 4. Unpacking Tuples ---")
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(f"Green: {green}")
print(f"Yellow: {yellow}")
print(f"Red: {red}")

# Using Asterisk *
fruits_ex = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits_ex
print(f"Green: {green}")
print(f"Tropic (List): {tropic}")
print(f"Red: {red}")


print("\n--- 5. Looping Tuples ---")
for x in my_tuple:
    print(x)


print("\n--- 6. Tuple Methods ---")
numbers = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_5 = numbers.count(5)
index_8 = numbers.index(8)
print(f"Tuple: {numbers}")
print(f"Count of 5: {count_5}")
print(f"Index of first 8: {index_8}")

print("\n------------------------------------------------------------------------------------")
print("✅ Practice Complete!")
