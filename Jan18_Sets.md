# 18 Jan — Sets

## 1. What is a Set?
A set is a collection that is:
- **Unordered**: The items have no index.
- **Unchangeable**: You cannot change items after the set is created, but you can add/remove items.
- **Indexed**: No (you cannot access create items by index).
- **Unique**: No duplicate members allowed.

Sets are written with curly brackets `{}`.

## 2. Creating a Set
```python
# Creating a set
my_set = {"apple", "banana", "cherry"}
print(my_set)

# Duplicate values will be ignored
this_set = {"apple", "banana", "cherry", "apple"}
print(this_set) # {'banana', 'apple', 'cherry'} (order may vary)
```

## 3. Accessing Items
You cannot access items in a set by referring to an index or a key.
But you can loop through the set items using a `for` loop, or ask if a specified value is present in a set, by using the `in` keyword.

```python
this_set = {"apple", "banana", "cherry"}

for x in this_set:
  print(x)

print("banana" in this_set) # True
```

## 4. Add Items
To add one item to a set use the `add()` method.
```python
this_set = {"apple", "banana", "cherry"}
this_set.add("orange")
print(this_set)
```

To add items from another set into the current set, use the `update()` method.
```python
this_set = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
this_set.update(tropical)
print(this_set)
```

## 5. Remove Items
To remove an item in a set, use the `remove()`, or the `discard()` method.
```python
this_set = {"apple", "banana", "cherry"}
this_set.remove("banana")
print(this_set)

# If the item to remove does not exist, remove() will raise an error.
# discard() will NOT raise an error.
this_set.discard("banana") 
```

## 6. Set Operations (Math)
Sets are great for mathematical operations like union, intersection, difference, etc.

### Union ( | )
Returns a set containing all items from both sets.
```python
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
# OR
set3 = set1 | set2
print(set3)
```

### Intersection ( & )
Returns a set items that exist in both sets.
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
# OR
z = x & y
print(z) # {'apple'}
```

### Difference ( - )
Returns a set that contains items that only exist in set x, and not in set y.
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)
# OR
z = x - y
print(z) # {'banana', 'cherry'}
```

### Symmetric Difference ( ^ )
Returns a set that contains all items from both sets, except items that are present in both.
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
# OR
z = x ^ y
print(z) # {'google', 'banana', 'microsoft', 'cherry'}
```
