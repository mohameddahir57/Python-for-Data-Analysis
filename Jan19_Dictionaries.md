# 19 Jan — Dictionaries

## 1. What is a Dictionary?
A dictionary is a collection of **key-value pairs**.
- **Ordered**: As of Python 3.7, dictionaries are ordered.
- **Changeable**: You can change, add or remove items.
- **No Duplicates**: Dictionaries cannot have two items with the same key.

Dictionaries are written with curly brackets `{}`, and have keys and values.

## 2. Creating a Dictionary
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
```

## 3. Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets `[]` or using `get()`.

```python
x = thisdict["model"]
y = thisdict.get("model")
```

## 4. Keys, Values, and Items
- `keys()`: Returns a list of all the keys.
- `values()`: Returns a list of all values.
- `items()`: Returns each item in a dictionary, as tuples in a list.

```python
print(thisdict.keys())   # dict_keys(['brand', 'model', 'year'])
print(thisdict.values()) # dict_values(['Ford', 'Mustang', 1964])
print(thisdict.items())  # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
```

## 5. Change and Add Items
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Change value
thisdict["year"] = 2018

# Add new pair
thisdict["color"] = "red"

# Update method
thisdict.update({"year": 2020})
```

## 6. Remove Items
- `pop()`: Removes the item with the specified key name.
- `popitem()`: Removes the last inserted item.
- `del`: Removes the item with the specified key name.
- `clear()`: Empties the dictionary.

```python
thisdict.pop("model")
del thisdict["brand"]
```

## 7. Loop Through a Dictionary
```python
# Loop through keys
for x in thisdict:
  print(x)

# Loop through values
for x in thisdict:
  print(thisdict[x])
  
# Better way for values
for x in thisdict.values():
  print(x)

# Loop through keys and values
for x, y in thisdict.items():
  print(x, y)
```

## 8. Nested Dictionaries
A dictionary can contain dictionaries.
```python
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
```
