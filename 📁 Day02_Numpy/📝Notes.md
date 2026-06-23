# 📘 Day 2 Notes – NumPy Indexing & Filtering

## 🧠 Topics Covered

- Indexing in 1D arrays
- Accessing elements in 2D arrays
- Accessing elements in 3D arrays
- Array slicing (positive indexing)
- Negative indexing
- Boolean masking (filtering)
- Manual filtering using loops
- Even and odd filtering

---

## 📌 1. 1D Array Indexing

NumPy indexing in a 1D array works the same as Python lists.

- Indexing starts from `0`
- The first element is at position `0`, the second at position `1`, and so on

---

## 📌 2. 2D Array Accessing

A 2D array is like a matrix with rows and columns.

- The **first index** represents the **row**
- The **second index** represents the **column**

This helps in selecting specific elements or entire rows from the array.

---

## 📌 3. 3D Array Accessing

A 3D array contains multiple 2D arrays. Access happens in three steps:

1. Select the matrix
2. Select the row
3. Select the column

This allows precise selection of elements inside multi-dimensional data.

---

## 📌 4. Array Slicing (Positive Indexing)

Slicing is used to select a range of elements from an array. It follows the structure:

```
array[start : stop : step]
```

| Part    | Meaning                              |
|---------|---------------------------------------|
| `start` | Where selection begins                |
| `stop`  | Where it ends (**not included**)      |
| `step`  | How many elements to skip              |

> 💡 Leaving a value empty gives default behavior — e.g., starting from the beginning or going till the end.

---

## 📌 5. Negative Indexing

Negative indexing is used to access elements from the **end** of the array.

- `-1` → last element
- `-2` → second-last element, and so on

Slicing with negative indices also helps select elements from the end portion of an array.

---

## 📌 6. Boolean Masking (Filtering)

Boolean masking filters data using `True`/`False` values.

- Only elements with `True` values are selected
- `False` values are ignored

Useful for conditional filtering.

---

## 📌 7. Manual Filtering Using Loops

Arrays can be filtered manually using loops:

1. Check each condition one by one
2. Store `True`/`False` in a list based on the condition
3. Use that list to filter the original array

---

## 📌 8. Even and Odd Filtering

Practiced filtering even numbers using a condition inside a loop:

- Only numbers satisfying the condition are selected
- Others are ignored

---

## 🧠 Final Summary

Today I learned how NumPy allows:

- ✅ Easy element access in different dimensional arrays
- ✅ Powerful slicing techniques for selecting data
- ✅ Negative indexing for reverse access
- ✅ Efficient filtering using boolean masking
- ✅ Manual filtering using logical conditions

---

## 🚀 Key Takeaway

> NumPy makes data selection and filtering **extremely fast and simple** compared to normal Python loops — especially when working with large datasets.