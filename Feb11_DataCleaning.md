# 🧹 Feb 11: Data Cleaning Project

Welcome to Day 2 of Week 8! Today you'll tackle one of the most important skills in data analysis: **data cleaning**.

## 🎯 Project Overview

**Scenario**: You've received a customer database from a legacy system. The data is messy, incomplete, and inconsistent. Before any analysis can be done, you need to clean and standardize it.

**Your Mission**: Transform dirty, unreliable data into a clean, analysis-ready dataset.

## 📁 Dataset Description

The messy customer dataset contains:

- **CustomerID**: Unique identifier (may have duplicates)
- **Name**: Customer name (inconsistent formatting)
- **Email**: Email address (some invalid, some missing)
- **Phone**: Phone number (various formats)
- **Age**: Customer age (some outliers, some missing)
- **City**: City name (inconsistent capitalization)
- **State**: State code (some full names, some abbreviations)
- **SignupDate**: Registration date (various formats)
- **TotalSpent**: Total purchase amount (some negative values)
- **Status**: Account status (Active/Inactive, inconsistent)

## 🎯 Data Quality Issues

You'll encounter:

1. **Missing Values**: Various columns have missing data
2. **Duplicates**: Some customers appear multiple times
3. **Inconsistent Formatting**: Names, cities, states
4. **Invalid Data**: Negative amounts, impossible ages
5. **Data Type Issues**: Dates stored as strings
6. **Outliers**: Extreme values that need investigation
7. **Inconsistent Categories**: Different spellings of same values

## 📊 Cleaning Tasks

### Task 1: Initial Assessment (15 min)
- Load and inspect the data
- Identify data quality issues
- Document problems found
- Create a cleaning plan

### Task 2: Handle Missing Values (20 min)
- Identify missing value patterns
- Decide on strategy for each column
- Implement appropriate solutions:
  - Drop rows/columns
  - Fill with mean/median/mode
  - Forward/backward fill
  - Custom logic

### Task 3: Remove Duplicates (15 min)
- Identify duplicate records
- Determine which duplicates to keep
- Remove or merge duplicates
- Verify results

### Task 4: Fix Data Types (15 min)
- Convert dates to datetime
- Ensure numeric columns are numeric
- Standardize categorical data
- Handle special cases

### Task 5: Standardize Formatting (20 min)
- Standardize name capitalization
- Clean and format phone numbers
- Standardize city/state names
- Fix email formats

### Task 6: Handle Outliers (15 min)
- Identify outliers in age and spending
- Investigate suspicious values
- Decide on treatment (keep, cap, remove)
- Document decisions

### Task 7: Validate Data (15 min)
- Check data ranges
- Validate email formats
- Verify phone numbers
- Ensure consistency

### Task 8: Export Clean Data (10 min)
- Create final clean dataset
- Generate data quality report
- Document all changes made
- Export to CSV

## ✅ Deliverables

Your completed project should include:

1. **Data Quality Report**
   - Issues found
   - Cleaning steps taken
   - Records affected
   - Final data quality metrics

2. **Clean Dataset**
   - No missing values (or documented strategy)
   - No duplicates
   - Consistent formatting
   - Valid data types
   - Documented outlier treatment

3. **Cleaning Documentation**
   - Clear explanations of decisions
   - Before/after comparisons
   - Validation results

## 🔍 Data Cleaning Principles

### Missing Values
- **Drop** if > 50% missing
- **Fill** with appropriate values (mean, median, mode)
- **Flag** if missingness is informative
- **Impute** using advanced methods if needed

### Duplicates
- **Exact duplicates**: Keep first, remove rest
- **Partial duplicates**: Investigate and merge if appropriate
- **Document** all duplicate removal decisions

### Outliers
- **Investigate** before removing
- **Cap** at reasonable thresholds
- **Remove** only if clearly errors
- **Document** all decisions

### Formatting
- **Consistency** is key
- **Standardize** to one format
- **Document** transformation rules
- **Validate** results

## 💡 Tips for Success

### Investigation
✅ Always investigate before deleting  
✅ Look for patterns in missing data  
✅ Check if outliers are errors or real  
✅ Understand the business context  
✅ Document your reasoning  

### Cleaning
✅ Make one change at a time  
✅ Verify results after each step  
✅ Keep track of rows affected  
✅ Create backup before major changes  
✅ Use functions for repetitive tasks  

### Validation
✅ Check data ranges after cleaning  
✅ Verify totals and counts  
✅ Look for new issues created  
✅ Compare before/after statistics  
✅ Test with sample queries  

## 📈 Success Metrics

Your clean dataset should have:

- **0% duplicate records**
- **< 5% missing values** (or documented strategy)
- **100% valid data types**
- **100% consistent formatting**
- **0 invalid values** (negative ages, etc.)
- **Documented outlier treatment**

## 🌟 Bonus Challenges

If you finish early:

1. **Advanced Imputation**: Use KNN or regression to fill missing values
2. **Fuzzy Matching**: Find and merge similar names/cities
3. **Data Profiling**: Create comprehensive data quality dashboard
4. **Automated Pipeline**: Create reusable cleaning functions
5. **Quality Scoring**: Assign quality scores to each record

## 🚀 Getting Started

Open `Feb11_DataCleaning.ipynb` and start cleaning!

Remember:
- Data cleaning is 80% of data analysis work
- Take your time to understand the data
- Document everything you do
- Validate your results

Good luck! 🧹✨
