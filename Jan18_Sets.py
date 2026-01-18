# Jan 18 - Sets Practice

# 1. Create a set called 'fruits' with "apple", "banana", "cherry"
fruits = {"apple", "banana", "cherry"}
print(f"Original Set: {fruits}")

# 2. Add "orange" to the set
fruits.add("orange")
print(f"After adding orange: {fruits}")

# 3. Add multiple items: "mango", "grape"
more_fruits = ["mango", "grape"]
fruits.update(more_fruits)
print(f"After adding list: {fruits}")

# 4. Remove "banana"
fruits.remove("banana")
print(f"After removing banana: {fruits}")

# 5. Check if "apple" is in the set
print(f"Is 'apple' in fruits? {'apple' in fruits}")

print("-" * 20)

# 6. Set Operations
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

print(f"Set A: {set_A}")
print(f"Set B: {set_B}")

# Union
union_set = set_A | set_B
print(f"Union (A | B): {union_set}")

# Intersection
intersection_set = set_A & set_B
print(f"Intersection (A & B): {intersection_set}")

# Difference (A - B)
diff_A_B = set_A - set_B
print(f"Difference (A - B): {diff_A_B}")

# Difference (B - A)
diff_B_A = set_B - set_A
print(f"Difference (B - A): {diff_B_A}")

# Symmetric Difference
sym_diff = set_A ^ set_B
print(f"Symmetric Difference (A ^ B): {sym_diff}")
