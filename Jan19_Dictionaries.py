# Jan 19 - Dictionaries Practice

# 1. Create a dictionary representing a car
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2015,
    "color": "Silver"
}
print(f"Car Dictionary: {car}")

# 2. Access the value of "model"
print(f"Model: {car['model']}")
print(f"Model using get(): {car.get('model')}")

# 3. Change the "year" to 2018
car["year"] = 2018
print(f"Updated Year: {car['year']}")

# 4. Add a new key-value pair "price": 15000
car["price"] = 15000
print(f"After adding price: {car}")

# 5. Loop through both keys and values
print("\n--- Car Details ---")
for key, value in car.items():
    print(f"{key}: {value}")

print("-" * 20)

# 6. Nested Dictionary: Student Grades
students = {
    "Alice": {"Math": 85, "English": 90},
    "Bob": {"Math": 78, "English": 82},
    "Charlie": {"Math": 92, "English": 88}
}

# Print Bob's Math score
print(f"Bob's Math Score: {students['Bob']['Math']}")

# Calculate average score for Alice
alice_scores = students["Alice"].values()
alice_avg = sum(alice_scores) / len(alice_scores)
print(f"Alice's Average Score: {alice_avg}")
