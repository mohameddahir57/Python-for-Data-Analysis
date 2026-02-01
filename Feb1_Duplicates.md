# 👯 Feb 01: Handling Duplicates

Duplicate data can skew your analysis and lead to incorrect conclusions. Pandas offers efficient ways to find and remove these duplicates.

## 1. Finding Duplicates
- `df.duplicated()`: Returns a boolean Series where `True` indicates a row is a duplicate of a previous row.
- `df.duplicated().sum()`: Counts the total number of duplicate rows.
- `df[df.duplicated()]`: Shows the actual duplicate rows.

### Parameters for `duplicated()`:
- `subset`: Only check specific columns (e.g., `subset=['Email']`).
- `keep`: 
    - `'first'` (default): Mark all duplicates as `True` except for the first occurrence.
    - `'last'`: Mark all duplicates as `True` except for the last occurrence.
    - `False`: Mark all duplicates as `True`.

## 2. Removing Duplicates
- `df.drop_duplicates()`: Returns a DataFrame with duplicate rows removed.

### Parameters for `drop_duplicates()`:
- `subset`: Remove based on specific columns.
- `keep`: Which occurrence to keep (`'first'`, `'last'`, or `False` to drop all).
- `inplace=True`: Modifies the original DataFrame.

```python
# Keep the latest entry for each student ID
df.drop_duplicates(subset=['StudentID'], keep='last', inplace=True)
```

## 3. Best Practices
- Always check for duplicates after merging datasets.
- Be careful with `subset`; sometimes rows look like duplicates but have different timestamps or IDs.
- Use `inplace=True` only when you are sure you don't need the original state.
