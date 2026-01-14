# 🐍 Python for Data Analysis: Day 14
## Topic: while Loops

### 1. Introduction
A `while` loop is used to execute a block of code repeatedly as long as a specified condition is **True**. This is called "conditional iteration."

---

### 2. Syntax
```python
while condition:
    # Code to run
    # Update the condition variable
```

**Crucial Rule:** You must ensure that the condition eventually becomes **False**. If it stays True forever, you create an **Infinite Loop**, which can crash your program.

---

### 3. Key Concepts

#### 🔹 Increment/Decrement
To avoid infinite loops, you usually change a counter or a flag inside the loop.
*Example:* `count += 1` or `n -= 1`.

#### 🔹 The `break` Statement
Instantly exits the loop, regardless of the condition.
*Use Case:* Stop searching when you find the value you need.

#### 🔹 The `continue` Statement
Skips the rest of the current block and goes back to the condition check at the top.
*Use Case:* Skip specific items (like missing data or errors) while processing.

---

### 4. for vs while: When to use which?
| Feature | `for` Loop | `while` Loop |
| :--- | :--- | :--- |
| **Usage** | Iterating over a sequence (list, range). | When logic depends on a condition. |
| **Known Limits** | Used when you know how many times to run. | Used when you don't know the end point. |
| **Complexity** | Generally safer and easier to read. | Powerful but carries risk of infinite loops. |

---

### 5. Practice Tips
- Use `while True` only when you have a clear `break` statement inside.
- Test your condition logic carefully to avoid "off-by-one" errors.
- In Data Analysis, `while` loops are less common than `for` loops but essential for tasks like reading data until a file ends or waiting for a specific event.
