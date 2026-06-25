# Day 04 — Matplotlib Full Notes

---

## 1. Importing Matplotlib & NumPy

Before drawing any plot, you need to import the two core libraries.

```python
import matplotlib.pyplot as plt
import numpy as np
```

- `matplotlib.pyplot` is the module that contains all plotting functions. It is aliased as `plt` by convention.
- `numpy` is used to create and manipulate numerical arrays. It is aliased as `np` by convention.

---

## 2. Basic Line Plot

The simplest thing you can do is pass two arrays — one for x values and one for y values — and call `plt.plot()`.

```python
x = np.array([1, 2, 4, 8, 16])
y = np.array([0, 4, 5, 7, 15])

plt.plot(x, y)
plt.show()
```

**How it works:**
- `np.array([...])` creates a NumPy array from a Python list.
- `plt.plot(x, y)` draws a line connecting each (x, y) pair in order.
- `plt.show()` renders and displays the figure on screen. Without it, nothing appears.

---

## 3. Understanding Figure & Axes

Matplotlib has two main building blocks: the **Figure** and the **Axes**.

- A **Figure** is the entire window or canvas.
- An **Axes** is an individual plot inside that figure (the area with x/y axis lines, ticks, data, etc.).

```python
fig = plt.figure()              # empty figure, no axes yet
fig, ax = plt.subplots()        # figure with one axes
fig, axs = plt.subplots(2, 2)   # figure with a 2×2 grid of 4 axes
```

You can also create custom layouts using `subplot_mosaic`:

```python
fig, axs = plt.subplot_mosaic([
    ['left', 'right_top'],
    ['left', 'right_bottom']
])
```

**How it works:**
- `plt.subplots()` returns a tuple: the figure and either one axes or an array of axes.
- `subplot_mosaic` accepts a 2D list of string labels; axes that share the same label span multiple cells (like a merged cell in a table).
- `axs` (with an "s") is used by convention when there are multiple axes.

---

## 4. Drawing a Plot with the Axes Object

Using the object-oriented approach (recommended for complex plots):

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [5, 6, 7, 8])
plt.show()
```

**How it works:**
- `fig, ax = plt.subplots()` gives you explicit control over the figure and its single axes.
- `ax.plot(...)` draws on that specific axes object — this is safer than `plt.plot()` when you have multiple subplots.

---

## 5. Adding Multiple Subplots

You can manually add subplots to a figure using `fig.add_subplot(rows, cols, index)`.

```python
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(2, 2, 1)   # top-left
ax2 = fig.add_subplot(2, 2, 2)   # top-right
ax3 = fig.add_subplot(2, 2, 3)   # bottom-left
```

**How it works:**
- `figsize=(10, 5)` sets the figure width to 10 inches and height to 5 inches.
- `add_subplot(2, 2, 1)` means: in a 2-row × 2-column grid, place this axes at position 1 (top-left). Positions are counted left-to-right, top-to-bottom.

---

## 6. Supertitle & Figure-level Labels

```python
data = np.arange(10)   # array [0, 1, 2, ..., 9]
plt.suptitle("Data", fontsize=15, weight='bold', color='blue')
plt.plot(data)
```

**How it works:**
- `np.arange(10)` creates an array from 0 to 9.
- `plt.suptitle()` adds a "super title" across the top of the entire figure (above all subplots).
- `fontsize`, `weight`, and `color` control the appearance of the title text.

> **Note:** `plt.Figure(...)` with a capital F is the class constructor and does not create a usable figure in a script — use `plt.figure(...)` (lowercase) instead. This was a minor bug in today's code.

---

## 7. Line Styling

You can change how the line looks using the `linestyle` argument.

```python
x = np.array([1, 2, 4, 8, 16])
y = np.array([0, 4, 5, 7, 15])

plt.plot(x, y, linestyle='dashed')   # -- -- -- line
plt.plot(x, y, linestyle='dotted')   # ......... line
```

**Common linestyle values:**

| Value | Appearance |
|---|---|
| `'solid'` (default) | Continuous line |
| `'dashed'` | Dashes |
| `'dotted'` | Dots |
| `'dashdot'` | Alternating dash and dot |

---

## 8. Labels & Font Properties

Good plots always have axis labels and a title so the reader knows what they are looking at.

```python
x = np.array([1, 2, 4, 8, 16])
y = np.array([0, 4, 5, 7, 15])

plt.plot(x, y, linestyle='dashed')
plt.suptitle("Plot", fontsize=15, weight='bold')
plt.xlabel("X side", fontsize=12)
plt.ylabel("Y side", fontsize=14)
plt.show()
```

**How it works:**
- `plt.suptitle()` — title at the top of the figure.
- `plt.xlabel()` — label for the horizontal axis.
- `plt.ylabel()` — label for the vertical axis.
- `fontsize` controls text size (in points).
- `weight='bold'` makes the title text bold.

---

## 9. Adding a Grid

A grid makes it easier to read values off the plot.

```python
plt.plot(x, y, linestyle='dashed')
plt.suptitle("Plot", fontsize=15, weight='bold')
plt.xlabel("X side", fontsize=12)
plt.ylabel("Y side", fontsize=14)
plt.grid(color='green', linestyle='--')
plt.show()
```

**How it works:**
- `plt.grid()` enables the background grid.
- `color='green'` sets the grid line color.
- `linestyle='--'` sets the grid line style.
- You can restrict the grid to one axis only: `plt.grid(axis='x')` shows only vertical lines, `plt.grid(axis='y')` shows only horizontal lines.

---

## 10. Advanced Subplot Types

You can put different chart types into different subplots.

```python
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

# Histogram — shows distribution of data
ax1.hist(np.random.standard_normal(100), bins=20, alpha=0.3, color='yellow')

# Scatter plot — shows relationship between two variables
ax2.scatter(np.arange(30), np.arange(30) * 3 + np.random.standard_normal(30))

# Line plot — shows trend over sequential data
ax3.plot(np.random.standard_normal(100), linestyle='dashed', color='black')
```

**How it works:**

| Chart | Method | What it shows |
|---|---|---|
| Histogram | `ax.hist()` | How frequently values fall into ranges (bins) |
| Scatter | `ax.scatter()` | Points at (x, y) pairs — shows correlation |
| Line | `ax.plot()` | A connected line through sequential values |

- `np.random.standard_normal(n)` generates `n` random numbers from a normal (bell curve) distribution.
- `bins=20` divides the data range into 20 equal-width bars.
- `alpha=0.3` sets the transparency (0 = invisible, 1 = fully opaque).
- `np.arange(30) * 3 + np.random.standard_normal(30)` creates a noisy linear pattern for the scatter plot.

---

## 11. Sample Graph Workflow — Putting It All Together

This is the clean, complete pattern you should follow for most plots.

```python
x = np.linspace(0, 2, 200)   # 200 evenly spaced points from 0 to 2

fig, ax = plt.subplots(figsize=(5, 2.7))

ax.plot(x, x,      label='linear')     # y = x
ax.plot(x, x**2,   label='quadratic')  # y = x²
ax.plot(x, x**3,   label='cubic')      # y = x³

plt.title('Simple Plot')
plt.xlabel('X label')
plt.ylabel('Y label')
plt.legend()
plt.show()
```

**How it works step by step:**

1. `np.linspace(0, 2, 200)` — creates 200 points evenly spread from 0 to 2. Better than `arange` when you want a fixed number of points.
2. `figsize=(5, 2.7)` — sets the width and height of the output figure in inches.
3. Three `ax.plot()` calls — each draws a different curve on the same axes. Matplotlib automatically assigns different colors.
4. `label='linear'` — assigns a name to each line. This name appears in the legend.
5. `plt.title()` — plot title (appears above the axes, inside the figure).
6. `plt.xlabel()` / `plt.ylabel()` — axis labels.
7. `plt.legend()` — draws the legend box using the `label` values from each `plot()` call.
8. `plt.show()` — displays everything.

---

## Quick Reference Summary

| Function | What it does |
|---|---|
| `plt.plot(x, y)` | Draw a line graph |
| `plt.show()` | Display the figure |
| `plt.figure(figsize=(...))` | Create a figure with custom size |
| `plt.subplots()` | Create figure + axes together |
| `fig.add_subplot(r, c, i)` | Add an axes at grid position i |
| `plt.suptitle()` | Figure-level title |
| `plt.title()` | Axes-level title |
| `plt.xlabel()` / `plt.ylabel()` | Axis labels |
| `plt.grid()` | Show background grid |
| `plt.legend()` | Show legend |
| `ax.hist()` | Histogram |
| `ax.scatter()` | Scatter plot |
| `np.linspace(a, b, n)` | n evenly spaced values from a to b |
| `np.arange(n)` | Integer array from 0 to n−1 |
| `np.random.standard_normal(n)` | n random values from normal distribution |