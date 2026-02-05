# 📊 Feb 05: Matplotlib Basics

Matplotlib is the foundational plotting library in Python. It gives you complete control over every element of your visualizations.

## 1. Why Matplotlib?
- **Industry Standard**: Most widely used Python visualization library
- **Flexibility**: Complete control over every aspect of your plots
- **Foundation**: Many other libraries (like Seaborn) are built on top of Matplotlib
- **Publication Quality**: Create professional charts for reports and presentations

## 2. Basic Plotting Workflow
```python
import matplotlib.pyplot as plt

# 1. Prepare your data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 2. Create the plot
plt.plot(x, y)

# 3. Add labels and title
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('My First Plot')

# 4. Display the plot
plt.show()
```

## 3. Figure and Axes
Understanding the anatomy of a Matplotlib plot:
- **Figure**: The entire window or page
- **Axes**: The actual plot area where data is displayed

```python
# Create figure and axes explicitly
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title('Using Axes Object')
plt.show()
```

## 4. Customization Options

### Colors
```python
plt.plot(x, y, color='red')        # Named color
plt.plot(x, y, color='#FF5733')    # Hex code
plt.plot(x, y, color=(0.1, 0.2, 0.5))  # RGB tuple
```

### Line Styles
```python
plt.plot(x, y, linestyle='--')     # Dashed
plt.plot(x, y, linestyle='-.')     # Dash-dot
plt.plot(x, y, linestyle=':')      # Dotted
plt.plot(x, y, linewidth=3)        # Thicker line
```

### Markers
```python
plt.plot(x, y, marker='o')         # Circle markers
plt.plot(x, y, marker='s')         # Square markers
plt.plot(x, y, marker='^')         # Triangle markers
plt.plot(x, y, marker='*', markersize=10)  # Star with size
```

### Shorthand Notation
```python
plt.plot(x, y, 'ro--')  # Red circles with dashed line
# Format: [color][marker][line]
```

## 5. Multiple Plots on Same Figure
```python
plt.plot(x, y1, label='Series 1')
plt.plot(x, y2, label='Series 2')
plt.legend()  # Show legend
plt.show()
```

## 6. Subplots
Create multiple plots in one figure:
```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.plot(x, y1)
ax1.set_title('Plot 1')
ax2.plot(x, y2)
ax2.set_title('Plot 2')
plt.tight_layout()  # Prevent overlap
plt.show()
```

## 7. Saving Plots
```python
plt.plot(x, y)
plt.savefig('my_plot.png', dpi=300, bbox_inches='tight')
# Formats: .png, .jpg, .pdf, .svg
```

## 8. Common Customizations
```python
plt.grid(True)                    # Add grid
plt.xlim(0, 10)                   # Set x-axis limits
plt.ylim(0, 20)                   # Set y-axis limits
plt.xticks([0, 2, 4, 6, 8, 10])  # Custom tick marks
plt.style.use('seaborn-v0_8')     # Use a style theme
```

## Key Takeaways
✅ Matplotlib gives you complete control over visualizations  
✅ The basic workflow: data → plot → customize → show/save  
✅ Use `fig, ax = plt.subplots()` for more control  
✅ Customize colors, markers, and line styles to enhance clarity  
✅ Always add labels, titles, and legends for context  

Ready to practice? Open `Feb5_MatplotlibBasics.ipynb`!
