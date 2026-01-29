# ✂️ Filtering & Sorting Data

Filtering and sorting are fundamental operations for narrowing down your analysis to specific data points.

## 1. Filtering Rows (Selection)
We use **Boolean Indexing** to select rows based on conditions.

```python
# Select rows where Price is greater than 100
expensive_products = df[df['Price'] > 100]

# Multiple conditions (AND: &, OR: |)
# Note: Use parentheses for each condition
filtered_df = df[(df['Price'] > 50) & (df['Product'] != 'Laptop')]
```

## 2. Filtering by specific values (`isin`)
```python
# Select rows where product is 'Mouse' or 'Keyboard'
selected_items = df[df['Product'].isin(['Mouse', 'Keyboard'])]
```

## 3. Sorting Data
* `df.sort_values(by='column_name')`: Sorts ascending (default).
* `df.sort_values(by='column_name', ascending=False)`: Sorts descending.
* `df.sort_values(by=['col1', 'col2'])`: Sorts by multiple columns.

## 4. Resetting Index
After filtering or sorting, the index might become disorganized.
* `df.reset_index(drop=True)`: Re-indexes the dataframe starting from 0.

## Today's Goals:
* Extract specific subsets of data using conditions.
* Combine multiple filters using logical operators.
* Organize data by sorting numerical or alphabetical columns.
