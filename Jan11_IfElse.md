# 🐍 Python for Data Analysis: Day 11
## Topic: if / else Statements (Control Flow)

### 1. Introduction
**Control Flow** refers to the order in which individual statements, instructions, or function calls are executed or evaluated. In Python, the `if`, `elif`, and `else` statements allow the program to make decisions and execute specific blocks of code based on whether a condition is **True** or **False**.

### 2. Syntax & Definitions

#### A. The `if` Statement
The simplest form of decision making. If the condition is True, the indented block of code runs.

```python
if condition:
    # Code to run if condition is True
```

#### B. The `else` Statement
Used after an `if` to provide an alternative block of code that runs ONLY if the `if` condition is False.

```python
if condition:
    # Code if True
else:
    # Code if False
```

#### C. The `elif` Statement (Short for "else if")
Allows you to check multiple conditions in sequence. Python checks them one by one and executes the first block where the condition is True.

```python
if condition1:
    # Block 1
elif condition2:
    # Block 2
else:
    # Block if none of the above are True
```

### 3. Key Concepts

#### 🔹 Indentation
Unlike many other languages that use curly braces `{}`, Python uses **indentation** (usually 4 spaces) to define blocks of code. If you forget to indent, you will get an `IndentationError`.

#### 🔹 The Colon `:`
Every `if`, `elif`, and `else` line MUST end with a colon. This tells Python that a code block follows.

#### 🔹 Nested Ifs
You can place an `if` statement inside another `if` statement for more complex logic.

```python
if x > 10:
    if y > 20:
        print("Both high")
```

#### 🔹 Shorthand If (Ternary Operator)
A way to write simple if-else logic in a single line.
`result = value_if_true if condition else value_if_false`

### 4. Code Examples

#### Example 1: Basic Decision
```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("Too young to vote.")
```

#### Example 2: Grading System (elif)
```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

### 5. Summary Table

| Statement | Purpose | When it runs |
| :--- | :--- | :--- |
| `if` | Primary check | If the condition is `True`. |
| `elif` | Secondary checks | If previous conditions were `False` and this one is `True`. |
| `else` | Fallback | If ALL previous conditions were `False`. |

### 6. Practice Exercises
1. **Even or Odd**: Write a script that checks if a number is even or odd using the `%` operator.
2. **Access Control**: Create a variable `is_logged_in` and `user_role`. Only print "Welcome Admin" if both are True (`is_logged_in == True` and `user_role == "Admin"`).

