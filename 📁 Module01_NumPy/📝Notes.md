# Day 01 — NumPy Fundamentals

**Series:** ML from Scratch to Pro
**Topic:** Introduction to NumPy and Arrays
**Instructor:** Muhammad Yaqoob Hassan

---

# Introduction

NumPy (Numerical Python) is one of the most important libraries in Python for working with numerical data. It provides a powerful data structure called an **array**, which is faster and more memory-efficient than Python lists.

NumPy is widely used in:

* Machine Learning
* Data Science
* Artificial Intelligence
* Scientific Computing
* Data Analysis

Most Machine Learning libraries such as Scikit-Learn, TensorFlow, and PyTorch use NumPy arrays internally.

---

# Installing NumPy

Before using NumPy, it must be installed in your Python environment.

After installation, NumPy can be imported into a Python program and used through the alias `np`, which is the standard convention followed by developers worldwide.

---

# Checking NumPy Version

NumPy continuously receives updates and improvements.

Checking the installed version helps ensure compatibility with tutorials, libraries, and projects.

---

# Understanding Arrays

The core data structure in NumPy is the **array**.

An array is a collection of values stored together in a structured format.

Arrays are preferred over Python lists because they:

* Execute operations faster
* Use less memory
* Support mathematical computations directly
* Are optimized for large datasets

---

# One-Dimensional Arrays (1D)

A one-dimensional array contains data in a single row or sequence.

Examples:

* Student marks
* Daily temperatures
* Product prices

A 1D array has only one axis.

---

# Two-Dimensional Arrays (2D)

A two-dimensional array contains both rows and columns.

Examples:

* Tables
* Spreadsheets
* Machine Learning datasets

Most datasets used in Machine Learning are represented as two-dimensional arrays.

---

# Array Dimensions

NumPy allows us to determine how many dimensions an array has.

Understanding dimensions is important because Machine Learning models often expect data in a specific structure.

Examples:

* 1D Array → One dimension
* 2D Array → Two dimensions
* 3D Array → Three dimensions

---

# Useful Functions for Creating Arrays

NumPy provides several built-in functions for creating arrays quickly.

### Zeros Array

Creates an array where every element is zero.

Commonly used for:

* Initialization
* Placeholder values
* Matrix creation

---

### Ones Array

Creates an array where every element is one.

Useful for:

* Testing algorithms
* Creating default values
* Mathematical operations

---

### Full Array

Creates an array filled with a custom value.

Useful when all elements need to start with the same value.

---

### Identity Matrix

An identity matrix is a square matrix where:

* Diagonal elements are 1
* Remaining elements are 0

Identity matrices are frequently used in Linear Algebra, which forms the mathematical foundation of Machine Learning.

---

### Arange

Creates a sequence of numbers using:

* A starting value
* An ending value
* A step size

Useful for generating ranges and numerical sequences.

---

# Statistical Functions

NumPy provides built-in functions for basic statistical analysis.

### Mean

The mean represents the average value of a dataset.

It is calculated by adding all values together and dividing by the total number of values.

---

### Median

The median is the middle value when data is arranged in order.

It is useful because it is less affected by extreme values.

---

### Minimum Value

Returns the smallest value present in the dataset.

---

### Maximum Value

Returns the largest value present in the dataset.

---

# NumPy Properties

Every NumPy array contains useful information about itself.

---

## Shape

The shape tells us the structure of the array.

For two-dimensional arrays, shape represents:

* Number of rows
* Number of columns

Understanding shape is important because Machine Learning algorithms expect data in specific formats.

---

## Number of Dimensions

This property tells us how many dimensions an array contains.

Examples:

* 1D Array → 1 Dimension
* 2D Array → 2 Dimensions

---

## Size

The size represents the total number of elements stored in an array.

---

## Data Type

Every value in a NumPy array has a data type.

Common data types include:

* Integer
* Float
* Boolean

Knowing the data type helps optimize memory usage and calculations.

---

# Array Operations

One of NumPy's biggest advantages is performing operations directly on arrays.

Instead of writing loops, NumPy can apply operations to entire arrays at once.

Operations covered in this lesson include:

* Addition
* Subtraction
* Multiplication
* Division

This approach is known as **vectorized computation**, and it is much faster than traditional looping.

---

# Copying Arrays

A copy creates a completely independent array.

When changes are made to the copied array, the original array remains unchanged.

This is useful when we want to preserve the original data while experimenting with modifications.

---

# Viewing Arrays

A view creates another reference to the same data.

Both arrays share the same memory location.

As a result, changes made through the view can affect the original array.

Understanding the difference between copying and viewing arrays is essential for preventing unexpected bugs.

---

# Reshaping Arrays

Reshaping changes the structure of an array without changing its actual values.

It allows us to transform data into different row and column arrangements.

This is especially important in Machine Learning because many algorithms require data in a specific shape.

---

# Concatenating Arrays

Concatenation means joining multiple arrays together.

This technique is commonly used when:

* Combining datasets
* Merging features
* Expanding data

NumPy provides efficient tools for combining arrays into larger structures.

---

# Why NumPy Matters in Machine Learning

Almost every Machine Learning workflow involves:

1. Loading data
2. Storing data in arrays
3. Performing calculations
4. Transforming data structures
5. Preparing data for model training

NumPy provides the foundation for all of these tasks.

A strong understanding of NumPy is essential before moving on to Pandas, Data Visualization, Data Preprocessing, and Machine Learning algorithms.

---

# Summary

In this lesson, we learned:

* What NumPy is and why it is important
* How arrays are used in Machine Learning
* The difference between 1D and 2D arrays
* Various methods for creating arrays
* Basic statistical functions
* Important NumPy properties
* Array arithmetic operations
* The difference between copy and view
* How to reshape arrays
* How to concatenate arrays

These concepts form the foundation for working with data in Machine Learning.

---

# Next Lesson

In Day 02, we will explore:

* Indexing
* Slicing
* Selecting specific values
* Array filtering
* Boolean masking
* Fancy indexing

These techniques will allow us to access and manipulate data more efficiently.
