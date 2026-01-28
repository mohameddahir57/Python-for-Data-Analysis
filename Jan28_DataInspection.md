# 🔍 Data Inspection

Once data is loaded, the first step is always to **explore** it to understand its structure, size, and potential issues (missing values, wrong types).

## 1. Viewing the Data
* `df.head(n)`: Shows the first `n` rows (default 5).
* `df.tail(n)`: Shows the last `n` rows.
* `df.sample(n)`: Shows random `n` rows.

## 2. Understanding Structure & Size
* `df.shape`: Returns (rows, columns).
* `df.columns`: Returns the list of column names.
* `df.info()`: Provides a concise summary (indices, data types, memory usage, non-null counts).
* `df.dtypes`: Shows only data types of each column.

## 3. Basic Statistics
* `df.describe()`: Generates descriptive statistics for numerical columns (mean, std, min, max, etc.).
* `df.describe(include='all')`: Includes statistics for categorical columns as well.

## 4. Checking Unique Values
* `df['column'].nunique()`: Number of unique values.
* `df['column'].unique()`: Array of unique values.
* `df['column'].value_counts()`: Count of each unique value.

## Today's Goals:
* Master the basic inspection commands.
* Identifying the number of rows and columns quickly.
* Checking for data types and missing value clues.
