# 📊 Feb 06: Line & Bar Charts

Line and bar charts are the workhorses of data visualization. Mastering these two chart types will cover 80% of your visualization needs.

## 1. When to Use Each Chart Type

### Line Charts
**Best for**: Showing trends over time or continuous data
- Stock prices over months
- Temperature changes throughout the day
- Website traffic over weeks
- Sales growth over years

### Bar Charts
**Best for**: Comparing discrete categories
- Sales by product category
- Revenue by region
- Survey responses by age group
- Performance metrics across teams

## 2. Line Charts in Detail

### Basic Line Chart
```python
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
revenue = [50000, 55000, 52000, 60000, 65000]

plt.plot(months, revenue)
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.title('Monthly Revenue Trend')
plt.show()
```

### Multiple Lines for Comparison
```python
plt.plot(months, revenue_2024, label='2024', marker='o')
plt.plot(months, revenue_2025, label='2025', marker='s')
plt.legend()
plt.show()
```

### Styling Line Charts
```python
plt.plot(months, revenue, 
         color='#3498db',           # Custom color
         linewidth=2.5,             # Thicker line
         marker='o',                # Add markers
         markersize=8,              # Marker size
         linestyle='--',            # Dashed line
         alpha=0.7)                 # Transparency
```

## 3. Bar Charts in Detail

### Vertical Bar Chart
```python
categories = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [45000, 38000, 52000, 41000]

plt.bar(categories, sales)
plt.xlabel('Product')
plt.ylabel('Sales ($)')
plt.title('Sales by Product')
plt.show()
```

### Horizontal Bar Chart
Useful when category names are long:
```python
plt.barh(categories, sales)
plt.xlabel('Sales ($)')
plt.ylabel('Product')
plt.title('Sales by Product')
plt.show()
```

### Customizing Bar Charts
```python
plt.bar(categories, sales,
        color='#2ecc71',           # Bar color
        edgecolor='black',         # Border color
        linewidth=1.5,             # Border width
        alpha=0.8,                 # Transparency
        width=0.6)                 # Bar width
```

## 4. Grouped Bar Charts
Compare multiple series side by side:
```python
import numpy as np

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots()
ax.bar(x - width/2, sales_2024, width, label='2024')
ax.bar(x + width/2, sales_2025, width, label='2025')

ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
plt.show()
```

## 5. Stacked Bar Charts
Show composition of totals:
```python
fig, ax = plt.subplots()
ax.bar(categories, online_sales, label='Online')
ax.bar(categories, store_sales, bottom=online_sales, label='In-Store')
ax.legend()
plt.show()
```

## 6. Best Practices

### For Line Charts
✅ **DO**:
- Use for time series data
- Add markers when you have few data points
- Use different colors/styles for multiple lines
- Include a legend when showing multiple series
- Start y-axis at zero (unless showing small variations)

❌ **DON'T**:
- Use too many lines (max 5-7)
- Use similar colors that are hard to distinguish
- Forget to label axes

### For Bar Charts
✅ **DO**:
- Always start y-axis at zero
- Sort bars by value (unless there's a natural order)
- Use horizontal bars for long category names
- Add value labels on bars when space allows
- Use consistent colors within a category

❌ **DON'T**:
- Use 3D effects (they distort perception)
- Make bars too wide or too narrow
- Use too many categories (consider grouping)

## 7. Adding Value Labels
```python
# On bar charts
bars = plt.bar(categories, sales)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'${height:,.0f}',
             ha='center', va='bottom')
```

## 8. Color Palettes
```python
# Professional color schemes
colors_professional = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
colors_pastel = ['#a8dadc', '#f1faee', '#e63946', '#457b9d']
colors_vibrant = ['#ff006e', '#fb5607', '#ffbe0b', '#8338ec']

plt.bar(categories, sales, color=colors_professional)
```

## Quick Reference

| Chart Type | Use Case | Key Function |
|------------|----------|--------------|
| Line Chart | Trends over time | `plt.plot()` |
| Vertical Bar | Category comparison | `plt.bar()` |
| Horizontal Bar | Long category names | `plt.barh()` |
| Grouped Bar | Multi-series comparison | Multiple `plt.bar()` with offset |
| Stacked Bar | Part-to-whole | `plt.bar()` with `bottom` parameter |

## Key Takeaways
✅ Line charts show trends, bar charts compare categories  
✅ Always label axes and add titles  
✅ Use colors strategically to highlight insights  
✅ Keep it simple - less is often more  
✅ Consider your audience when choosing chart complexity  

Ready to practice? Open `Feb6_LineBarCharts.ipynb`!
