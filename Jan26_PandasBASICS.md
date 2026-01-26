# 🐼 Pandas Core: Series & DataFrames

Welcome to **Week 5**! Today we begin our journey with **Pandas**, the most popular library for data manipulation and analysis in Python.

## 1. What is Pandas?
Pandas is built on top of NumPy. While NumPy works with arrays, Pandas provides high-level data structures like **Series** and **DataFrames** that are designed to work with tabular data (like Excel or SQL tables).

## 2. Pandas Series
A **Series** is a one-dimensional labeled array. It can hold any data type.
- Think of it as a single column in a table.
- Each element has an **index** (label).

```python
import pandas as pd

# Creating a Series from a list
data = [10, 20, 30, 40]
s = pd.Series(data)
print(s)
```

## 3. Pandas DataFrames
A **DataFrame** is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure.
- Think of it as a whole table or spreadsheet.
- It has **rows** and **columns**.

```python
# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}
df = pd.DataFrame(data)
print(df)
```

## 4. Key Differences
| Feature | Series | DataFrame |
| :--- | :--- | :--- |
| Dimensions | 1D | 2D |
| Content | Single column | Multiple columns (Table) |
| Structure | Index + Data | Index + Columns + Data |

## Today's Goals:
* Understand the difference between Series and DataFrames.
* Create them from lists and dictionaries.
* Access basic attributes like `.shape`, `.columns`, and `.index`.
