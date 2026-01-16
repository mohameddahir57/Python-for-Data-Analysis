# 🟦 Day 16: Python Lists

Lists are one of the most versatile and commonly used data structures in Python. They are ordered, mutable (changeable), and allow duplicate values.

## 1. Creating Lists
You can create a list by placing elements inside square brackets `[]`, separated by commas.

```python
# Empty list
my_list = []

# List with integers
numbers = [1, 2, 3, 4, 5]

# List with mixed data types
mixed = [1, "Hello", 3.14, True]

# List constructor
another_list = list((1, 2, 3))
```

## 2. Accessing Elements (Indexing)
Items are accessed by their index (position). Python uses **0-based indexing**.

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[-1]) # Last item (cherry)
```

## 3. Slicing Lists
You can extract a portion of a list using slicing: `list[start:stop:step]`

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])   # [2, 3, 4] (index 2 up to but not including 5)
print(numbers[:3])    # [0, 1, 2] (start to index 2)
print(numbers[5:])    # [5, 6, 7, 8, 9] (index 5 to end)
print(numbers[::2])   # [0, 2, 4, 6, 8] (every 2nd item)
print(numbers[::-1])  # [9, 8, ..., 0] (Reverse list)
```

## 4. Modifying Lists
Lists are **mutable**, meaning you can change their content.

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits) # ['apple', 'blueberry', 'cherry']
```

## 5. Common List Methods

| Method | Description |
| :--- | :--- |
| `append(x)` | Adds an item `x` to the end of the list. |
| `insert(i, x)` | Inserts item `x` at index `i`. |
| `extend(iterable)`| Extends the list by appending elements from another list/iterable. |
| `remove(x)` | Removes the first occurrence of item `x`. |
| `pop(i)` | Removes and returns the item at index `i` (default is last). |
| `clear()` | Removes all elements from the list. |
| `index(x)` | Returns the index of the first occurrence of `x`. |
| `count(x)` | Returns the number of times `x` appears in the list. |
| `sort()` | Sorts the list items in ascending order (modifies original). |
| `reverse()` | Reverses the order of the list (modifies original). |
| `copy()` | Returns a copy of the list. |

```python
colors = ["red", "green", "blue"]

colors.append("yellow")   # ['red', 'green', 'blue', 'yellow']
colors.insert(1, "orange")# ['red', 'orange', 'green', 'blue', 'yellow']
item = colors.pop()       # Removes 'yellow'
colors.remove("green")    # Removes 'green'
```

## 6. List Comprehensions
A concise way to create lists based on existing lists.

**Syntax**: `[expression for item in iterable if condition]`

```python
numbers = [1, 2, 3, 4, 5]

# Create a list of squares
squares = [x**2 for x in numbers] # [1, 4, 9, 16, 25]

# Get even numbers only
evens = [x for x in numbers if x % 2 == 0] # [2, 4]
```

## 📝 Practice Exercises

### Exercise 1: Basic Operations
1. Create a list of 5 favorite movies.
2. Print the second movie.
3. Change the last movie to something else.
4. Add a new movie to the end.
5. Print the length of the list.

### Exercise 2: Numbers & Slicing
1. Create a list of numbers from 0 to 10 (use `range` and `list`).
2. Print the first 3 numbers.
3. Print the last 3 numbers using negative indexing.
4. Print the numbers in reverse order.

### Exercise 3: Methods
1. Create an empty list called `shopping_cart`.
2. Add "Milk", "Eggs", and "Bread".
3. Insert "Butter" at index 1.
4. Remove "Eggs".
5. Check if "Milk" is in the cart.
