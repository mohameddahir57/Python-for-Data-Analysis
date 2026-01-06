# 🐍 Jan 06 — Python Variables

Welcome to Day 1 of your Python for Data Analysis journey! Today, we are covering **Variables**—the building blocks of any program.

## 1. What is a Variable?
A variable is like a **labeled container** that stores data in your computer's memory. Instead of remembering the data itself, you give it a name so you can use it later.

```python
# 'age' is the variable name
# '25' is the value stored inside
age = 25
```

## 2. Variable Assignment
In Python, we use the `=` sign (assignment operator) to assign a value to a name.

- **Left side**: The name you choose (Variable).
- **Right side**: The value you want to store (Data).

```python
city = "Mogadishu"
temperature = 30.5
is_cloudy = False
```

## 3. Naming Rules (PEP 8)
To write clean, professional code (following Python's PEP 8 style guide), follow these rules:

1.  **Be Descriptive**: Use `user_age` instead of `a`.
2.  **Use snake_case**: Join multiple words with underscores (e.g., `total_sales_2024`).
3.  **No Numbers at the Start**: `player1` is okay, but `1player` is NOT.
4.  **Case Sensitive**: `Name` and `name` are two different variables.
5.  **No Spaces**: Use underscores instead of spaces.

## 4. Dynamic Typing
Python is **dynamically typed**, which means you don't have to declare the type of data (like Integer or String). You can even change the type of data a variable holds whenever you want!

```python
x = 10       # x is an integer
x = "Ten"    # Now x is a string
```

## 5. Working with Multiple Variables
You can assign values to multiple variables in one line:

```python
x, y, z = "Orange", "Banana", "Cherry"
```

## 📝 Practice Exercises (Try these in your Python file!)

1.  **Profile Creation**: Create three variables: `my_name`, `my_goal`, and `years_experience`. Assign relevant values to them.
2.  **Calculation**: Create a variable `price = 100` and `tax = 0.15`. Calculate the `total_price` and print it.
3.  **Swap**: If `a = 5` and `b = 10`, try to swap their values so `a` becomes 10 and `b` becomes 5.

### 💡 Tip for Data Analysts
As a Data Analyst, you will use variables to store **DataFrames** (tables of data). Instead of typing a whole Excel file path every time, you'll store it in a variable like `df` or `sales_data`.

**Next Topic (Jan 7):** Data Types (Integers, Strings, Floats, Booleans)


