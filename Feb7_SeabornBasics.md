# 📊 Feb 07: Seaborn Basics

Seaborn is a high-level visualization library built on top of Matplotlib. It makes creating beautiful, statistical graphics much easier with less code.

## 1. Why Seaborn?

### Advantages over Matplotlib
- **Beautiful by default**: Professional-looking plots with minimal code
- **Built-in themes**: Instantly improve aesthetics
- **Statistical functions**: Automatic calculation and display of statistics
- **Better defaults**: Sensible color palettes and styles
- **DataFrame integration**: Works seamlessly with Pandas

### When to Use Seaborn
✅ Statistical visualizations  
✅ Distribution analysis  
✅ Relationship exploration  
✅ Categorical data comparison  
✅ Quick, beautiful plots  

## 2. Getting Started

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Set the style
sns.set_style("whitegrid")
sns.set_palette("husl")
```

### Available Styles
- `whitegrid`: White background with grid
- `darkgrid`: Gray background with grid
- `white`: White background, no grid
- `dark`: Gray background, no grid
- `ticks`: White with ticks on axes

## 3. Distribution Plots

### Histogram with KDE
```python
sns.histplot(data=df, x='age', kde=True)
plt.title('Age Distribution')
plt.show()
```

### KDE Plot (Kernel Density Estimation)
Shows smooth distribution curve:
```python
sns.kdeplot(data=df, x='salary')
plt.title('Salary Distribution')
plt.show()
```

### Distribution Plot with Multiple Variables
```python
sns.histplot(data=df, x='score', hue='gender', kde=True)
plt.title('Score Distribution by Gender')
plt.show()
```

## 4. Categorical Plots

### Box Plot
Shows distribution quartiles and outliers:
```python
sns.boxplot(data=df, x='department', y='salary')
plt.title('Salary by Department')
plt.xticks(rotation=45)
plt.show()
```

### Violin Plot
Combines box plot with KDE:
```python
sns.violinplot(data=df, x='category', y='price')
plt.title('Price Distribution by Category')
plt.show()
```

### Bar Plot
Shows mean with confidence interval:
```python
sns.barplot(data=df, x='region', y='sales')
plt.title('Average Sales by Region')
plt.show()
```

### Count Plot
Shows frequency of categories:
```python
sns.countplot(data=df, x='product_type')
plt.title('Product Type Distribution')
plt.xticks(rotation=45)
plt.show()
```

## 5. Relationship Plots

### Scatter Plot
```python
sns.scatterplot(data=df, x='advertising', y='sales', hue='region')
plt.title('Advertising vs Sales by Region')
plt.show()
```

### Regression Plot
Adds a regression line:
```python
sns.regplot(data=df, x='experience', y='salary')
plt.title('Experience vs Salary with Trend Line')
plt.show()
```

### Line Plot
```python
sns.lineplot(data=df, x='month', y='revenue', hue='year')
plt.title('Monthly Revenue Trend')
plt.show()
```

## 6. Color Palettes

### Built-in Palettes
```python
# Qualitative (for categories)
sns.set_palette("Set2")
sns.set_palette("Pastel1")
sns.set_palette("husl")

# Sequential (for ordered data)
sns.set_palette("Blues")
sns.set_palette("YlOrRd")

# Diverging (for data with a midpoint)
sns.set_palette("RdBu")
sns.set_palette("coolwarm")
```

### Custom Palettes
```python
custom_colors = ["#3498db", "#e74c3c", "#2ecc71", "#f39c12"]
sns.set_palette(custom_colors)
```

## 7. Themes and Styling

### Context Settings
Control the scale of plot elements:
```python
sns.set_context("paper")    # Smallest
sns.set_context("notebook")  # Default
sns.set_context("talk")      # Larger
sns.set_context("poster")    # Largest
```

### Complete Theme Setup
```python
sns.set_theme(
    style="whitegrid",
    palette="husl",
    context="notebook",
    font_scale=1.2
)
```

## 8. Combining with Matplotlib

Seaborn works with Matplotlib for fine-tuning:
```python
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x='category', y='value', ax=ax)
ax.set_title('My Custom Title', fontsize=14, fontweight='bold')
ax.set_ylabel('Value ($)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

## 9. Common Plot Types Quick Reference

| Plot Type | Function | Best For |
|-----------|----------|----------|
| Histogram | `histplot()` | Distribution of single variable |
| KDE | `kdeplot()` | Smooth distribution curve |
| Box Plot | `boxplot()` | Distribution with quartiles |
| Violin Plot | `violinplot()` | Distribution shape comparison |
| Bar Plot | `barplot()` | Mean values with confidence |
| Count Plot | `countplot()` | Category frequencies |
| Scatter | `scatterplot()` | Relationship between variables |
| Regression | `regplot()` | Relationship with trend line |
| Line Plot | `lineplot()` | Trends over time |

## 10. Best Practices

### DO ✅
- Use Seaborn for statistical visualizations
- Set a theme at the beginning of your notebook
- Use `hue` parameter to add a third dimension
- Leverage built-in statistical calculations
- Combine with Matplotlib for fine control

### DON'T ❌
- Mix too many styles in one analysis
- Forget to set figure size for complex plots
- Ignore the `palette` parameter
- Use default colors when custom ones tell a better story

## Key Takeaways
✅ Seaborn makes beautiful plots with less code  
✅ Perfect for statistical and exploratory data analysis  
✅ Built-in themes and palettes save time  
✅ Works seamlessly with Pandas DataFrames  
✅ Use `hue` to add categorical dimensions  
✅ Combine with Matplotlib for full customization  

Ready to practice? Open `Feb7_SeabornBasics.ipynb`!
