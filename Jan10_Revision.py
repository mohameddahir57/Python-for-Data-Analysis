# Jan 10 — Week 1 Challenge: Sales Calculator

# --- Requirements ---
# 1. Welcome message
# 2. Input: Customer Name
# 3. Input: 3 Item prices (floats)
# 4. Calculation: Subtotal, 10% Discount, Final Total
# 5. Output: Formatted Receipt

# WRITE YOUR CHALLENGE SOLUTION BELOW
print("--- Welcome to Somali Grocery Store ---")

customer = input("Enter customer name: ")

item1 = float(input("Enter price for Item 1 (Apples): "))
item2 = float(input("Enter price for Item 2 (Bananas): "))
item3 = float(input("Enter price for Item 3 (Bread): "))

subtotal = item1 + item2 + item3
discount = subtotal * 0.10
final_total = subtotal - discount

print("\n--- RECEIPT ---")
print(f"Customer: {customer}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount (10%): -${discount:.2f}")
print(f"FINAL TOTAL: ${final_total:.2f}")
print("----------------")
print("Thank you for shopping!")
