# 🐍 Python for Data Analysis: Day 15
## Topic: Functions

### 1. Introduction
A **Function** is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

Functions are the key to **DRY (Don't Repeat Yourself)** programming.

### 2. Syntax
```python
def function_name(parameters):
    # Docstring (optional but recommended)
    """Explanation of the function"""
    # Block of code
    return result # Optional
```

- `def`: The keyword used to define a function.
- `function_name`: Should be descriptive and lowercase (e.g., `calculate_mean`).
- `parameters`: Variables that act as placeholders for the data you pass in.
- `return`: Sends a value back to the caller.

### 3. Key Concepts

#### 🔹 Docstrings
A string literal that occurs as the first statement in a function. It is used to document what the function does.

#### 🔹 Positional vs Keyword Arguments
- **Positional**: Arguments assigned by their position.
- **Keyword**: Arguments assigned by their name (e.g., `greet(name="Ali")`).

#### 🔹 Scope
- **Local Scope**: Variables created inside a function only exist there.
- **Global Scope**: Variables created in the main body of the script.

### 4. Why use Functions in Data Analysis?
As a Data Analyst, you will use functions to:
- **Reuse logic**: Instead of writing the same cleaning steps for 10 files, create a `clean_data()` function.
- **Simplify code**: Break a complex analysis into smaller, manageable parts.
- **Improve readability**: A function name like `filter_outliers()` tells exactly what the code does.

### 5. Lambda Functions (Shortcuts)
For very simple, one-line functions, Python uses `lambda`:
`multiply = lambda x, y: x * y`
*Note: We will dive deeper into Lambda later in the journey.*

### 6. Practice Tips
- Use descriptive names for your functions.
- Keep functions small; each should do **one thing well**.
- Always include a docstring so others (or your future self) understand your code.

