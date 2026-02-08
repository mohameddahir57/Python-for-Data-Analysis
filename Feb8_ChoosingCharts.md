# 📊 Feb 08: Choosing the Right Chart

Choosing the right visualization is crucial for effectively communicating your data insights. This guide will help you select the perfect chart for your data story.

## 1. The Four Main Questions

Before creating any visualization, ask yourself:

1. **What am I trying to show?**
   - Comparison, distribution, composition, or relationship?

2. **How many variables do I have?**
   - One, two, three, or more?

3. **What type of data is it?**
   - Categorical, numerical, time-series?

4. **Who is my audience?**
   - Technical experts or general audience?

## 2. Chart Selection by Purpose

### 📊 Comparison Charts
**Goal**: Compare values across categories

| Chart Type | When to Use | Example |
|------------|-------------|---------|
| **Bar Chart** | Few categories (< 10) | Sales by product |
| **Grouped Bar** | Compare multiple series | Sales by product and year |
| **Horizontal Bar** | Long category names | Sales by country |
| **Line Chart** | Trends over time | Monthly revenue |
| **Radar Chart** | Multiple metrics per category | Product feature comparison |

```python
# Bar chart for comparison
sns.barplot(data=df, x='category', y='sales')
```

### 📈 Distribution Charts
**Goal**: Show how data is spread

| Chart Type | When to Use | Example |
|------------|-------------|---------|
| **Histogram** | Single variable distribution | Age distribution |
| **Box Plot** | Distribution with quartiles | Salary by department |
| **Violin Plot** | Distribution shape | Test scores by class |
| **KDE Plot** | Smooth distribution curve | Income distribution |
| **Strip Plot** | Individual data points | Survey responses |

```python
# Histogram for distribution
sns.histplot(data=df, x='age', bins=20, kde=True)
```

### 🥧 Composition Charts
**Goal**: Show parts of a whole

| Chart Type | When to Use | Example |
|------------|-------------|---------|
| **Pie Chart** | Few categories (< 6), simple percentages | Market share |
| **Stacked Bar** | Composition over categories | Revenue by channel per quarter |
| **Treemap** | Hierarchical data | Budget breakdown |
| **100% Stacked Bar** | Relative proportions | Customer segments by region |

```python
# Stacked bar for composition
plt.bar(x, online, label='Online')
plt.bar(x, store, bottom=online, label='Store')
```

### 🔗 Relationship Charts
**Goal**: Show correlation between variables

| Chart Type | When to Use | Example |
|------------|-------------|---------|
| **Scatter Plot** | Two continuous variables | Price vs demand |
| **Regression Plot** | Relationship with trend | Experience vs salary |
| **Heatmap** | Correlation matrix | Feature correlations |
| **Bubble Chart** | Three variables | Sales vs profit vs market size |
| **Pair Plot** | Multiple variable relationships | Dataset exploration |

```python
# Scatter plot for relationships
sns.scatterplot(data=df, x='advertising', y='sales')
```

## 3. Decision Tree

```
START: What do you want to show?
│
├─ COMPARISON
│  ├─ Over time? → Line Chart
│  ├─ Between categories? → Bar Chart
│  └─ Multiple series? → Grouped Bar Chart
│
├─ DISTRIBUTION
│  ├─ Single variable? → Histogram
│  ├─ By category? → Box Plot / Violin Plot
│  └─ Smooth curve? → KDE Plot
│
├─ COMPOSITION
│  ├─ Simple percentages? → Pie Chart
│  ├─ Over time/categories? → Stacked Bar Chart
│  └─ Hierarchical? → Treemap
│
└─ RELATIONSHIP
   ├─ Two variables? → Scatter Plot
   ├─ With trend? → Regression Plot
   └─ Many variables? → Heatmap / Pair Plot
```

## 4. Common Mistakes to Avoid

### ❌ DON'T Use Pie Charts When:
- You have more than 5-6 categories
- Differences between values are small
- Exact values matter more than proportions
- **Better alternative**: Bar chart

### ❌ DON'T Use 3D Charts
- They distort perception
- Hard to read exact values
- Look unprofessional
- **Better alternative**: 2D charts with good color coding

### ❌ DON'T Use Line Charts for:
- Categorical data (use bar charts)
- Unordered categories
- **Exception**: Time series data

### ❌ DON'T Truncate Y-Axis (Usually)
- Can mislead by exaggerating differences
- **Exception**: When showing small variations in large numbers

## 5. Best Practices by Data Type

### Time Series Data
✅ **Best**: Line chart  
✅ **Alternative**: Area chart for cumulative data  
✅ **For comparison**: Multiple lines or grouped bars  

### Categorical Data
✅ **Best**: Bar chart (vertical or horizontal)  
✅ **For counts**: Count plot  
✅ **For distributions**: Box plot or violin plot  

### Continuous Data
✅ **Distribution**: Histogram or KDE  
✅ **Relationship**: Scatter plot  
✅ **By category**: Box plot or violin plot  

### Hierarchical Data
✅ **Best**: Treemap  
✅ **Alternative**: Sunburst chart  
✅ **Simple**: Stacked bar chart  

## 6. Chart Complexity Guide

### Simple (General Audience)
- Bar charts
- Line charts
- Pie charts (< 5 categories)
- Simple scatter plots

### Moderate (Business Audience)
- Grouped bar charts
- Stacked bar charts
- Box plots
- Heatmaps

### Advanced (Technical Audience)
- Violin plots
- Pair plots
- Regression plots with confidence intervals
- Complex dashboards

## 7. Quick Reference Table

| Your Data | Your Goal | Use This Chart |
|-----------|-----------|----------------|
| Categories + Values | Compare | Bar Chart |
| Time + Values | Show trend | Line Chart |
| One continuous variable | Show distribution | Histogram |
| Category + Distribution | Compare distributions | Box Plot |
| Two continuous variables | Show relationship | Scatter Plot |
| Parts of whole | Show composition | Pie/Stacked Bar |
| Category + Multiple metrics | Compare profiles | Radar Chart |
| Many variables | Find correlations | Heatmap |

## 8. Real-World Scenarios

### Scenario 1: Sales Report
**Data**: Monthly sales for 3 products over 1 year  
**Goal**: Show trends and compare products  
**Best Choice**: Line chart with 3 lines  
**Why**: Shows both trends over time and allows comparison  

### Scenario 2: Customer Demographics
**Data**: Age distribution of 1000 customers  
**Goal**: Understand age spread  
**Best Choice**: Histogram with KDE  
**Why**: Shows distribution shape and density  

### Scenario 3: Regional Performance
**Data**: Sales figures for 5 regions  
**Goal**: Compare performance  
**Best Choice**: Horizontal bar chart (sorted)  
**Why**: Easy to compare, good for region names  

### Scenario 4: Budget Allocation
**Data**: Budget percentages across 4 departments  
**Goal**: Show how budget is divided  
**Best Choice**: Pie chart or stacked bar  
**Why**: Clearly shows parts of whole  

### Scenario 5: Price vs Quality
**Data**: Price and quality scores for 50 products  
**Goal**: Find relationship  
**Best Choice**: Scatter plot with regression line  
**Why**: Shows correlation and individual data points  

## 9. Combining Multiple Charts

For comprehensive analysis, use dashboards with:
- **Overview**: Key metrics (KPIs)
- **Trends**: Line charts
- **Comparisons**: Bar charts
- **Distributions**: Box plots or histograms
- **Relationships**: Scatter plots

## 10. The Golden Rules

1. **Simplicity First**: Start simple, add complexity only if needed
2. **One Message**: Each chart should tell one clear story
3. **Label Everything**: Axes, titles, legends, units
4. **Choose Colors Wisely**: Use color to highlight, not decorate
5. **Know Your Audience**: Technical depth should match audience
6. **Test Readability**: Can someone understand it in 5 seconds?
7. **Remove Clutter**: Every element should serve a purpose

## Key Takeaways
✅ Choose charts based on your data type and goal  
✅ Comparison → Bar/Line, Distribution → Histogram/Box, Relationship → Scatter  
✅ Keep it simple for general audiences  
✅ Avoid pie charts with many categories  
✅ Never use 3D charts  
✅ Label everything clearly  
✅ Test if your message is clear in 5 seconds  

Ready to practice? Open `Feb8_ChoosingCharts.ipynb`!
