# 🐍 Python for Data Analysis: Day 12
## Topic: Comparison & Logical Operators

### 1. Introduction
Comparison and Logical operators are essential for creating conditional statements. They allow us to evaluate relationships between data points and combine multiple rules into a single decision.

---

### 2. Comparison Operators
Comparison operators are used to compare two values. The result is always a **Boolean** (`True` or `False`).

| Operator | Name | Example | Result (if x=10, y=5) |
| :--- | :--- | :--- | :--- |
| `==` | Equal | `x == y` | `False` |
| `!=` | Not Equal | `x != y` | `True` |
| `>` | Greater Than | `x > y` | `True` |
| `<` | Less Than | `x < y` | `False` |
| `>=` | Greater or Equal | `x >= 10` | `True` |
| `<=` | Less or Equal | `y <= 5` | `True` |

---

### 3. Logical Operators
Logical operators are used to combine multiple conditional statements.

| Operator | Description | Rule |
| :--- | :--- | :--- |
| `and` | Returns `True` if **both** statements are true. | `True and True` = `True` |
| `or` | Returns `True` if **at least one** statement is true. | `True or False` = `True` |
| `not` | Reverses the result (`True` becomes `False`). | `not(True)` = `False` |

---

### 4. Operator Precedence
When combining multiple operators, Python follows a specific order:
1. Arithmetic Operators (`+`, `-`, `*`, etc.)
2. Comparison Operators (`==`, `>`, etc.)
3. Logical Operators (`not` first, then `and`, then `or`)

**Pro-tip:** Use parentheses `()` to make your logic clear and ensure it runs in the order you want.
*Example:* `(x > 5 and y < 10) or z == 0`

---

### 5. Practice Tips
- Use `==` for comparison, not `=` (which is for assignment).
- Remember that `a < x < b` is a valid shorthand in Python to check if `x` is between `a` and `b`.
- Logical operators are written in lowercase: `and`, `or`, `not`.
