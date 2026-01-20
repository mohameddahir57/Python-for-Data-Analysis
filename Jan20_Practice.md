# 20 Jan — Practice with Data Structures

## Overview
Today is about consolidating knowledge of the four built-in data structures in Python:
1. **List**: `[1, 2, 3]` (Ordered, mutable, allows duplicates)
2. **Tuple**: `(1, 2, 3)` (Ordered, immutable, allows duplicates)
3. **Set**: `{1, 2, 3}` (Unordered, immutable items, NO duplicates)
4. **Dictionary**: `{'a': 1, 'b': 2}` (Key-Value pairs, ordered, mutable, no duplicate keys)

## Practice Scenarios

### Challenge 1: The Grocery List
Managing a simple list of items to buy.
- Use a **List**.
- Add items, remove purchased items, sort them.

### Challenge 2: Unique Visitors
Tracking IP addresses of visitors to a website. We only care about unique visitors.
- Use a **Set**.
- Add IPs as they visit. Calculate total unique visitors.

### Challenge 3: Student Database
Storing student names and their corresponding grades.
- Use a **Dictionary**.
- Look up grades by name. Calculate class average.

### Challenge 4: Geographic Coordinates
Storing immutable (latitude, longitude) pairs for cities.
- Use a **Tuple**.
- Ensure they cannot be changed accidentally.

## Choosing the Right Structure
| Requirement | Recommended Structure |
| :--- | :--- |
| Need ordered sequence? | List or Tuple |
| Need to change items? | List or Dictionary |
| Need unique elements? | Set |
| Need key-value mapping? | Dictionary |
| Need immutability? | Tuple |
