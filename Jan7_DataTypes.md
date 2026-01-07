# 🐍 Jan 07 — Data Types

In Python, every value has a **Data Type**. Understanding these is crucial for data analysis because you need to know if you are working with numbers, text, or logic.

---

## 1. The Big Four Types

### 1.1 Integer (`int`)
Whole numbers without decimals.
```python
age = 25
count = -5
```

### 1.2 Float (`float`)
Numbers with decimal points.
```python
price = 19.99
pi = 3.14159
```

### 1.3 String (`str`)
Text wrapped in quotes (single `'` or double `"`).
```python
name = "Mohamed"
message = 'Hello Python'
```

### 1.4 Boolean (`bool`)
Logical values—either True or False.
```python
is_data_clean = True
is_missing = False
```

---

## 2. Checking Data Types
You can use the `type()` function to check what kind of data is stored in a variable.

```python
x = 10
print(type(x))  # <class 'int'>

y = "10"
print(type(y))  # <class 'str'>
```

---

## 3. Why it matters for Data Analysis?
If you try to add a string `"10"` and an integer `5`, Python will give you an error. Data cleaning often involves making sure all numbers in a column are actually `float` or `int`, not `str`.

---

## 📝 Practice Exercises

1.  Create variables of all 4 types and print their types using `type()`.
2.  Can you add a Boolean to an Integer? Try it! (Hint: True = 1, False = 0).
3.  Create a variable `rating = "4.5"`. Is it a float or a string? Check it.
