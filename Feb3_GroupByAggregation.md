# 📊 Feb 03: GroupBy & Aggregation

Aggregation is the process of summarizing data. Pandas uses the **Split-Apply-Combine** pattern to perform these operations.

## 1. The Split-Apply-Combine Pattern
1.  **Split**: Break the data into groups based on some criteria.
2.  **Apply**: Compute a statistic (sum, mean, count) for each group.
3.  **Combine**: Merge the results into a new DataFrame.

## 2. Basic Grouping
Use the `groupby()` method followed by an aggregation function.
```python
# Calculate average salary by department
df.groupby('Department')['Salary'].mean()

# Count number of employees in each city
df.groupby('City')['EmployeeID'].count()
```

## 3. Multiple Aggregations (`agg`)
You can apply multiple functions at once using the `agg()` method.
```python
# Get min, max, and mean age per department
df.groupby('Department')['Age'].agg(['min', 'max', 'mean'])
```

## 4. Custom Aggregations
You can also use custom dictionaries to apply different functions to different columns.
```python
summary = df.groupby('Department').agg({
    'Salary': 'mean',
    'Bonus': 'sum',
    'EmployeeID': 'count'
})
```

## 5. Grouping by Multiple Columns
```python
# Average price by category and region
df.groupby(['Category', 'Region'])['Price'].mean()
```

## 6. Pivot Tables
A more visual way to summarize data, similar to Excel.
```python
pivot = df.pivot_table(index='Region', columns='Category', values='Sales', aggfunc='sum')
```
