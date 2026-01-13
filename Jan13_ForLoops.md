# 🐍 Python for Data Analysis: Day 13
## Topic: for Loops

### 1. Introduction
A `for` loop is used for **iterating over a sequence** (that is either a list, a tuple, a dictionary, a set, or a string). This is one of the most powerful tools for data analysis because it allows you to process large amounts of data one item at a time.

---

### 2. The `range()` Function
The `range()` function is often used with for loops to iterate a specific number of times.

- `range(5)`: Generates `0, 1, 2, 3, 4`
- `range(2, 8)`: Generates `2, 3, 4, 5, 6, 7`
- `range(1, 10, 2)`: Generates `1, 3, 5, 7, 9` (Uses a step of 2)

---

### 3. Syntax
```python
for item in sequence:
    # Code to execute for each item
```

**How it works:**
1. The loop starts with the first item in the sequence.
2. The code block inside the loop executes.
3. It moves to the next item and repeats until the end of the sequence is reached.

---

### 4. Why is this important for Data Analysis?
As a Data Analyst, you will use for loops to:
- **Clean data**: Loop through rows to fix formatting.
- **Calculate metrics**: Sum values across a dataset.
- **Automate tasks**: Run the same analysis on different files.

---

### 5. Loop Control: `break` and `continue`
- `break`: Stops the loop completely.
- `continue`: Skips the current iteration and moves to the next one.

```python
for i in range(10):
    if i == 5:
        break # Stops at 5
    print(i)
```

---

### 6. Practice Tips
- Always ensure your loop has an endpoint so it doesn't run forever.
- Use meaningful variable names (e.g., `for sales in sales_data:` instead of `for x in y:`).
- Remember the indentation!
