# 🧹 Jan 31: Handling Missing Values

Handling missing data is one of the most critical steps in data cleaning. Real-world datasets often have empty fields, which can lead to errors or biased analysis if not handled correctly.

## 1. Detecting Missing Values
Pandas provides two main methods to detect missing values:
- `df.isna()`: Returns a DataFrame of booleans where `True` indicates a missing value.
- `df.info()`: Provides a summary of non-null counts.

To count missing values per column:
```python
df.isna().sum()
```

## 2. Handling Missing Values
There are three main strategies for dealing with missing data:

### A. Dropping Data (`dropna`)
Use this when the amount of missing data is small or the row/column is not useful.
- `df.dropna()`: Drops any row with at least one missing value.
- `df.dropna(axis=1)`: Drops columns with missing values.
- `df.dropna(subset=['ColumnName'])`: Drops rows only if a specific column has a missing value.

### B. Filling Data (`fillna`)
Replacing missing values with a specific value.
- `df.fillna(0)`: Fills all NaN with 0.
- `df['Column'].fillna('Unknown')`: Fills specific column.

### C. Imputation (Statistical Filling)
Using statistical measures to fill gaps:
- **Mean**: Average value (best for normally distributed numerical data).
- **Median**: Middle value (best if there are outliers).
- **Mode**: Most frequent value (best for categorical data).

```python
df['Age'] = df['Age'].fillna(df['Age'].mean())
```

## 3. Keywords to Remember
- `NaN`: Not a Number (Pandas default for missing values).
- `None`: Python's native null type.
- `inplace=True`: Modifies the original DataFrame instead of returning a new one.
