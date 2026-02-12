#  Feb 12: Exploratory Data Analysis (EDA) Project

Welcome to Day 3 of Week 8! Today you'll dive deep into Exploratory Data Analysis (EDA), the process of performing initial investigations on data to discover patterns, spot anomalies, and check assumptions.

##  Project Overview

**Scenario**: You are a Data Analyst for "GlobalCorp," a multinational company. The HR department wants to understand the factors affecting employee satisfaction and turnover. 

**Your Mission**: Perform a comprehensive EDA on the employee dataset to uncover hidden patterns and provide meaningful insights to the HR team.

##  Dataset Description

The employee dataset contains:

- **EmployeeID**: Unique ID for each employee.
- **Age**: Age of the employee.
- **Gender**: Gender of the employee.
- **Department**: Sales, Engineering, Marketing, HR, Finance.
- **MonthlySalary**: Salary in USD.
- **YearsAtCompany**: Total years spent at the company.
- **SatisfactionScore**: 1 to 5 (1 = Low, 5 = High).
- **WorkLifeBalance**: 1 to 5 (1 = Poor, 5 = Excellent).
- **NumberProjects**: Number of projects completed in the last year.
- **LeftCompany**: Whether the employee left the company (Yes/No).

##  EDA Objectives

### 1. Univariate Analysis (Looking at one variable)
- What is the age distribution of employees?
- How is the salary distributed across the whole company?
- What are the most common satisfaction scores?

### 2. Bivariate Analysis (Looking at two variables)
- Relationship between Age and Salary.
- Relationship between Department and Satisfaction Score.
- Relationship between Years at Company and Turnover (LeftCompany).

### 3. Multivariate Analysis (Looking at more than two variables)
- Salary distribution by Department and Gender.
- Satisfaction Score vs. Work-Life Balance vs. Turnover.

### 4. Correlation Analysis
- Which factors are most strongly correlated with an employee leaving the company?
- Is there a correlation between number of projects and satisfaction?

##  Required Visualizations

- **Histogram**: Age and Salary distributions.
- **Box Plots**: Salary by Department; Satisfaction by Turnover status.
- **Heatmap**: Correlation matrix of numerical variables.
- **Count Plots**: Employee counts by Department and Gender.
- **Violin Plots**: Salary distribution by Gender across Departments.
- **Pair Plot**: Overview of relationships between main numeric variables.

##  Step-by-Step Guide

### Step 1: Initial Data Inspection
- Load the data and check for missing values or duplicates.
- View summary statistics (`df.describe()`).

### Step 2: Distribution Analysis (Univariate)
- Create histograms and KDE plots for numeric variables.
- Use count plots for categorical variables.

### Step 3: Categorical Comparisons (Bivariate)
- Use box plots and bar charts to compare departments.
- Look for disparities in salary or satisfaction.

### Step 4: Relationship Exploration (Multivariate)
- Use scatter plots with `hue` to see interactions.
- Use `sns.heatmap` for correlation analysis.

### Step 5: Insights & Reporting
- Summarize the "Profile" of an employee likely to leave.
- Identify the highest and lowest performing departments in terms of satisfaction.

##  Deliverables

1. **Jupyter Notebook (`Feb12_EDA.ipynb`)**
   - Professional visualizations.
   - Statistical summaries.
   - Clear markdown explanations for each finding.
2. **Key Insights Summary**
   - Top 5 takeaways from the analysis.
   - Actionable advice for the HR team.

Ready? Open `Feb12_EDA.ipynb` and start your investigation! 🕵️‍♂️

