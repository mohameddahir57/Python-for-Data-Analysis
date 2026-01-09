# 🐍 Jan 09 — Input / Output

Today we interact with the user! We will learn how to take user input and display it beautifully.

---

## 1. Taking Input
The `input()` function allows the user to type something. **CRITICAL: `input()` always returns a string.**

```python
name = input("What is your name? ")
print("Hello, " + name)
```

If you need a number, you MUST convert it immediately:
```python
age = int(input("Enter your age: "))
```

---

## 2. Output Formatting (f-strings)
The modern way to print in Python is using **f-strings**. It's the most readable way.

```python
user = "Mohamed"
score = 95
print(f"User {user} scored {score}% in the test.")
```

---

## 3. Multiple Arguments in `print()`
The `print()` function can take multiple items separated by commas. It adds a space automatically.

```python
print("Total sales:", 5000, "USD")
```

---

## 📝 Practice Exercises

1.  Ask the user for their name and their favorite programming language. Print: "I am [Name] and I love [Language]."
2.  Ask the user for two numbers. Calculate their sum and print: "The total is [Result]." (Remember to convert to int!)
3.  Ask for the price of an item and quantity. Calculate total cost and print using an f-string.
