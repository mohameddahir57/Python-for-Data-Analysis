# 📄 Reading CSV & Excel Files

In data analysis, we rarely create dataframes manually from scratch. Most of the time, we load data from external files like **CSV** or **Excel**.

## 1. Reading CSV Files
CSV (Comma Separated Values) is the most common format for data science.
- Use `pd.read_csv('filename.csv')`

```python
import pandas as pd

# Load a CSV file
df = pd.read_csv('data.csv')

# Show the first few rows
print(df.head())
```

## 2. Reading Excel Files
Excel files (`.xlsx`) are also very common in business environments.
- Use `pd.read_excel('filename.xlsx')`
- *Note: You might need to install `openpyxl` using `pip install openpyxl`.*

```python
# Load an Excel file
df_excel = pd.read_excel('data.xlsx')
```

## 3. Common Parameters in `read_csv()`
* `sep`: Change the delimiter (e.g., `sep=';'`)
* `header`: Specify which row to use as the column names.
* `index_col`: Set a specific column as the index.
* `usecols`: Load only specific columns.

## Today's Goals:
* Learn how to load data from external files.
* Understand basic file reading parameters.
* Practice loading a sample dataset.
