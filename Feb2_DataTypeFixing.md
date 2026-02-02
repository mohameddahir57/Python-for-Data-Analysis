# 🔢 Feb 02: Fixing Data Types

Data often arrives as the wrong type (e.g., numbers stored as strings, or dates as plain text). Pandas allows you to convert these to the correct types for proper analysis.

## 1. Checking Data Types
- `df.dtypes`: Returns the data type of each column.
- `df.info()`: Provides a detailed summary including types and non-null counts.

## 2. Converting Types with `astype()`
The `astype()` method is the most common way to convert columns.
```python
# Convert Age column to integer
df['Age'] = df['Age'].astype(int)

# Convert Price to float
df['Price'] = df['Price'].astype(float)
```

## 3. Handling Date & Time
Dates are often loaded as strings (`object`). Use `pd.to_datetime()` for conversion.
```python
df['Date'] = pd.to_datetime(df['Date'])
```
After conversion, you can extract parts of the date:
- `df['Date'].dt.year`
- `df['Date'].dt.month`
- `df['Date'].dt.day_name()`

## 4. Handling Errors during Conversion
Sometimes conversion fails due to dirty data (e.g., 'Not Available' in a numeric column).
- `errors='coerce'`: Replaces failing values with `NaN`.
- `errors='ignore'`: Keeps the original value if conversion fails.

```python
# Safely convert to numeric
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
```

## 5. Summary of Common Types
- `int64`: Integers.
- `float64`: Decimals.
- `bool`: True/False.
- `datetime64`: Dates and times.
- `object`: Strings or mixed types.
- `category`: Limited set of values (efficient for memory).
