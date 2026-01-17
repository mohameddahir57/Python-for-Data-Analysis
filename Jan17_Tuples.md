# 17 Jan: Tuples

## 🔹 What is a Tuple?
A **Tuple** is a collection used to store multiple items in a single variable.

A tuple is:
- **Ordered**: Items have a defined order, and that order will not change.
- **Immutable**: Tuples **cannot** be changed, added, or removed after the tuple is created.
- **Allow Duplicates**: Since tuples are indexed, they can have items with the same value.

Tuples are written with round brackets `()`.

```python
my_tuple = ("apple", "banana", "cherry")
```

---

## 🔹 Creating Tuples

### 1. Standard Tuple
```python
thistuple = ("apple", "banana", "cherry")
print(thistuple)
```

### 2. Tuple with One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
```python
thistuple = ("apple",) # Tuple
not_tuple = ("apple")  # String
```

### 3. Using the `tuple()` Constructor
```python
thistuple = tuple(("apple", "banana", "cherry"))
```

---

## 🔹 Accessing Items
Since tuples are ordered, you can access items by referring to the index number inside square brackets `[]`.

**Note:** The first item has index 0.

```python
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # Output: banana
```

### Negative Indexing
Negative indexing means start from the end. `-1` refers to the last item.
```python
print(thistuple[-1]) # Output: cherry
```

### Slicing (Range of Indexes)
You can specify a range of indexes by specifying where to start and where to end.
```python
print(thistuple[1:3]) # Returns items from index 1 to 2 (3 is not included)
```

---

## 🔹 Updating Tuples
Tuples are **immutable**, meaning you cannot change, add, or remove items once the tuple is created.

**Workaround:** You can convert the tuple into a list, change the list, and convert the list back into a tuple.

```python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) # ("apple", "kiwi", "cherry")
```

---

## 🔹 Unpacking Tuples
When we create a tuple, we normally assign values to it. This is called **packing**.
But, we can also extract the values back into variables. This is called **unpacking**.

```python
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)  # apple
print(yellow) # banana
print(red)    # cherry
```

### Using Asterisk `*`
If the number of variables is less than the number of values, you can add an `*` to the variable name and the values will be assigned to the variable as a list.

```python
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green) # apple
print(yellow) # banana
print(red) # ['cherry', 'strawberry', 'raspberry']
```

---

## 🔹 Join Tuples
To join two or more tuples you can use the `+` operator.

```python
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
```

---

## 🔹 Tuple Methods
Python has two built-in methods that you can use on tuples:

| Method | Description |
|:---|:---|
| `count()` | Returns the number of times a specified value occurs in a tuple |
| `index()` | Searches the tuple for a specified value and returns the position of where it was found |

```python
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)
print(x) # 2

y = thistuple.index(8)
print(y) # 3 (first occurrence)
```

---

## 🔹 List vs Tuple (When to use which?)

| Feature | List `[]` | Tuple `()` |
|:---|:---|:---|
| **Mutable?** | Yes (Can change items) | No (Cannot change items) |
| **Speed** | Slower | Faster |
| **Memory** | Consumes more memory | Consumes less memory |
| **Use Case** | When you have a collection of data that needs to change (e.g., user input, shopping cart) | When you have a collection of constants that should not change (e.g., coordinates, configurations, fixed choices) |
