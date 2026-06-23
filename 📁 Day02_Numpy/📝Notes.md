📘 Day 2 Notes – NumPy Indexing & Filtering
🧠 Topics Covered
Indexing in 1D arrays
Accessing elements in 2D arrays
Accessing elements in 3D arrays
Array slicing (positive indexing)
Negative indexing
Boolean masking (filtering)
Manual filtering using loops
📌 1. 1D Array Indexing

I learned that NumPy indexing in a 1D array works the same as Python lists. Indexing starts from 0, so the first element is at position 0, the second at position 1, and so on.

📌 2. 2D Array Accessing

A 2D array is like a matrix with rows and columns.
I learned that the first index represents the row and the second index represents the column. This helps in selecting specific elements or entire rows from the array.

📌 3. 3D Array Accessing

A 3D array contains multiple 2D arrays.
I learned that access happens in three steps: first selecting the matrix, then the row, and finally the column. This allows precise selection of elements inside multi-dimensional data.

📌 4. Array Slicing (Positive Indexing)

I learned that slicing is used to select a range of elements from an array. It follows a structure of start, stop, and step.

Start defines where selection begins
Stop defines where it ends (not included)
Step defines how many elements to skip

I also learned that leaving values empty gives default behavior like starting from the beginning or going till the end.

📌 5. Negative Indexing

Negative indexing is used to access elements from the end of the array.

The last element is represented by -1
The second last by -2, and so on

I also learned that slicing with negative indices helps select elements from the end portion of an array.

📌 6. Boolean Masking (Filtering)

Boolean masking is a technique used to filter data using True and False values.
I learned that only elements with True values are selected from the array, while False values are ignored. This is useful for conditional filtering.

📌 7. Manual Filtering Using Loops

I learned how to manually filter arrays using loops by checking conditions one by one. Based on the condition, True or False values are stored in a list, which is then used to filter the original array.

📌 8. Even and Odd Filtering

I also practiced filtering even numbers using a condition inside a loop. Only numbers that satisfy the condition are selected, while others are ignored.

🧠 Final Summary

Today I learned how NumPy allows:

Easy element access in different dimensional arrays
Powerful slicing techniques for selecting data
Negative indexing for reverse access
Efficient filtering using boolean masking
Manual filtering using logical conditions
🚀 Key Takeaway

NumPy makes data selection and filtering extremely fast and simple compared to normal Python loops, especially when working with large datasets.