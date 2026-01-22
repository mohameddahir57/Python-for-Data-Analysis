# 📊 Jan 21 — NumPy Arrays

## 1. What is NumPy?
**NumPy** (Numerical Python) is the fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.

### Why use NumPy over Python Lists?
1.  **Speed:** NumPy arrays are significantly faster than Python lists for numerical operations because they are implemented in C and use contiguous memory.
2.  **Convenience:** NumPy provides easy-to-use functions for complex mathematical operations (linear algebra, statistics, etc.).
3.  **Memory Efficiency:** NumPy arrays consume less memory than Python lists.

## 2. Installation
If you don't have NumPy installed, you can install it using pip:
```bash
pip install numpy
```

## 3. Creating NumPy Arrays
The core object in NumPy is the `ndarray` (n-dimensional array).

### Importing NumPy
Standard convention is to alias numpy as `np`.
```python
import numpy as np
```

### Methods to Create Arrays
| Method | Description | Example |
| :--- | :--- | :--- |
| `np.array()` | Creates an array from a list or tuple. | `np.array([1, 2, 3])` |
| `np.zeros()` | Creates an array filled with zeros. | `np.zeros((3, 3))` |
| `np.ones()` | Creates an array filled with ones. | `np.ones((2, 4))` |
| `np.arange()` | Like Python's `range()`, but returns an array. | `np.arange(0, 10, 2)` |
| `np.linspace()` | Creates an array of evenly spaced values. | `np.linspace(0, 1, 5)` |
| `np.random.rand()` | Creates an array with random values (0 to 1). | `np.random.rand(3)` |

## 4. Array Attributes
Once you have an array, you can inspect its properties using these attributes:

-   **.ndim**: Number of dimensions (axes).
-   **.shape**: Tuple of integers indicating the size of the array in each dimension.
-   **.size**: Total number of elements in the array.
-   **.dtype**: Data type of the elements in the array (e.g., `int32`, `float64`).

---

## 📝 Practice
Open `Jan21_NumPyArrays.ipynb` and try creating different types of arrays and inspecting their attributes!
