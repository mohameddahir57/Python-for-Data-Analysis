# 🐍 Jan 08 — Type Conversion & Operations

Today we learn how to change data types (Casting) and perform basic math.

## 1. Type Conversion (Casting)
Sometimes you get data as a string (from a file) but you need it as a number for calculation.

-   `int()`: Converts to integer.
-   `float()`: Converts to decimal.
-   `str()`: Converts to text.

```python
score_str = "85"
score_int = int(score_str)  # Now it's a number
```

## 2. Basic Arithmetic Operations
Python is a powerful calculator!

-   `+` Addition
-   `-` Subtraction
-   `*` Multiplication
-   `/` Division (always returns a `float`)
-   `//` Floor Division (removes decimals)
-   `%` Modulo (returns the remainder)
-   `**` Exponent (Power)

```python
print(10 / 3)   # 3.333333333
print(10 // 3)  # 3
print(10 % 3)   # 1 (Remainder)
```

## 3. String Operations
You can use `+` to join strings (Concatenation) or `*` to repeat them.

```python
first = "Data"
second = "Analysis"
print(first + " " + second)  # Data Analysis
print("Hi! " * 3)            # Hi! Hi! Hi! 
```

## 📝 Practice Exercises

1.  Convert `price = "99.99"` to a float.
2.  Calculate the area of a circle with `radius = 7` (Area = 3.14 * r²).
3.  Given `items = 13` and `box_capacity = 4`, how many full boxes can you fill, and how many items are left over?

