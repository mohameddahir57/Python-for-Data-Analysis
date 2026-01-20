# Jan 20 - Data Structures Practice

# --- Challenge 1: Grocery List (List) ---
print("--- Challenge 1: Grocery List ---")
grocery_list = ["milk", "eggs", "bread", "cheese"]
grocery_list.append("apples") # Forgot apples!
grocery_list.remove("bread")  # Bought bread.
grocery_list.sort()
print(f"Final Grocery List: {grocery_list}")


# --- Challenge 2: Unique Visitors (Set) ---
print("\n--- Challenge 2: Unique Visitors ---")
visitors = {"192.168.1.1", "192.168.1.2", "192.168.1.1", "192.168.1.3"}
print(f"Unique IPs recorded: {len(visitors)}")
print(f"Visitor Set: {visitors}")


# --- Challenge 3: Student Database (Dictionary) ---
print("\n--- Challenge 3: Student Database ---")
students = {
    "John": 85,
    "Emma": 92,
    "Ryan": 78,
    "Sophia": 95
}

# Add a new student
students["Lucas"] = 88

# Check Emma's grade
print(f"Emma's Grade: {students['Emma']}")

# Class Average
avg_grade = sum(students.values()) / len(students)
print(f"Class Average: {avg_grade:.2f}")


# --- Challenge 4: Coordinates (Tuple) ---
print("\n--- Challenge 4: Coordinates ---")
# (Latitude, Longitude)
location_ny = (40.7128, -74.0060)
location_la = (34.0522, -118.2437)

print(f"New York Coordinates: {location_ny}")
# location_ny[0] = 41.000 # This would cause an Error! Tuples are immutable.


# --- Integrated Challenge: Inventory System ---
print("\n--- Integrated Challenge: Inventory System ---")
# A dictionary where keys are product names, and values are a dict with 'price' and 'stock'.
inventory = {
    "Laptop": {"price": 1000, "stock": 5},
    "Mouse": {"price": 20, "stock": 50},
    "Keyboard": {"price": 50, "stock": 20}
}

# Sell a Laptop
item_sold = "Laptop"
if inventory[item_sold]["stock"] > 0:
    inventory[item_sold]["stock"] -= 1
    print(f"Sold 1 {item_sold}. Remaining Stock: {inventory[item_sold]['stock']}")
else:
    print(f"Out of stock: {item_sold}")

print(f"Full Inventory: {inventory}")
