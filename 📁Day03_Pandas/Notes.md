# Day 03 Notes — Pandas Basics: Loading & Cleaning Data

These are my detailed notes for everything covered today. I'm using the **IRIS dataset** as the working example throughout.

---

## 1. Installing Pandas

```python
pip install pandas
```

Pandas doesn't come built into Python by default, so this installs it via pip. This only needs to be run once per environment — not every time I write code.

---

## 2. Importing Pandas

```python
import pandas as pd
```

`pd` is the universal alias for pandas — almost every pandas codebase you'll ever read uses this exact convention, so I'm sticking with it from day one.

---

## 3. Checking Pandas Version

```python
pd.__version__
```

Useful to check because pandas behavior can change between major versions (for example, how missing values or string columns are handled differs across versions). Good habit to check this early in any new project or notebook.

---

## 4. Importing CSV Files

```python
df = pd.read_csv("IRIS.csv")
```

This reads the CSV file from disk and loads it into a **DataFrame** — pandas' core 2D table structure (rows + columns), which is what almost all pandas work is built around. I named the variable `df` since that's the standard short-form for "DataFrame" used everywhere in pandas code.

---

## 5. Checking the DataFrame

```python
df
```

Just typing `df` in a Jupyter cell displays the table. This is the quickest way to "look" at the data and confirm it loaded correctly.

---

## 6. Giving Custom Column Names While Reading

```python
df = pd.read_csv("IRIS.csv", names=['Length', 'height'])
df
```

The `names` parameter lets you assign your own column headers when reading the file — useful if the CSV doesn't already have headers, or if you want to rename them right at load time instead of doing it afterward. I left this commented out since the original IRIS dataset already has proper column names and didn't need this.

---

## 7. Checking for Null Values

```python
df.isnull()
```

This returns a DataFrame of the same shape, but filled with `True`/`False` — `True` means that cell is missing (NaN), `False` means it has a value. On its own this isn't very readable for a big dataset, so it's more useful combined with `.sum()` (next step).

---

## 8. Quick Way to Count Null Values

```python
df.isnull().sum()
```

This adds up the `True` values column by column, giving a single count of how many missing values exist per column. For the IRIS dataset, this came back as **zero for every column** — meaning the dataset is clean with no missing values, which is actually rare in real-world data and made this a good "ideal" first dataset to practice on.

---

## 9. Getting DataFrame Info

```python
df.info()
```

This is one of the most useful first commands to run on any new dataset. It tells me:
- The object's **class** (confirms it's a DataFrame)
- The **range of the index** (e.g., 0 to 149 → 150 total rows)
- The **non-null count** per column (cross-checks what `.isnull().sum()` showed)
- The **dtype** of each column (so I know what operations are valid — e.g., you can't take a mean of a text column)
- The **memory usage** of the whole DataFrame

---

## 10. Viewing the First 5 Rows

```python
print("First 5 rows: ")
df.head()
```

`.head()` shows the top 5 rows by default — a fast sanity check that the data loaded correctly and looks the way I expect. Passing a number changes how many rows are shown, e.g. `df.head(10)` for the first 10 rows.

---

## 11. Viewing the Last 5 Rows

```python
df.tail()
```

Same idea as `.head()`, but from the bottom of the dataset. Same rule applies — `df.tail(Your_Number)` controls how many rows are shown. Checking both ends of a dataset is a good habit, since sometimes the last rows have different formatting or extra blank/summary rows that the first rows don't show.

---

## 12. Checking Total Rows and Columns

```python
df.shape
```

Returns a tuple `(rows, columns)`. For IRIS this is `(150, 5)` — 150 flower samples, 5 columns of measurements/labels.

---

## 13. Quick Statistical Summary

```python
df.describe()
```

Generates count, mean, std deviation, min, max, and the 25/50/75 percentiles for every **numeric** column. This is the fastest way to get a feel for the scale and spread of the data — for example, spotting if a column has unexpectedly large max values that might be outliers.

---

## 14. Handling Missing Values

```python
df.dropna(inplace=True)          # drops ROWS containing any NaN
df.dropna(inplace=True, axis=1)  # drops COLUMNS containing any NaN
```

- `dropna()` removes incomplete data.
- `inplace=True` is important — without it, pandas returns a *new* DataFrame and leaves the original `df` unchanged. Using `inplace=True` updates `df` directly so I don't have to keep reassigning it.
- `axis=1` switches the operation from rows to columns — easy to forget, but critical to get right depending on whether the missing data is scattered (drop rows) or whole columns are unreliable (drop columns).

---

## 15. Dropping Rows Based on a Specific Column

```python
df.dropna(subset=['sepal_length'], inplace=True)
```

Instead of dropping a row for *any* missing value anywhere, `subset` restricts the check to one (or more) specific columns. This is more precise — useful when only certain columns actually matter for the analysis.

---

## 16. Filling Missing Values Instead of Dropping

```python
df.fillna(0)
```

An alternative to dropping data — replaces every NaN with a constant (here, `0`). Useful when you don't want to lose rows entirely, though `0` is a simple placeholder; in real projects this is often replaced with something more meaningful like the column's mean or median.

---

## 17. Handling Unusual or Outlier Values

```python
# df.loc[0, 'sepal_length'] = 5
# df

# for x in df.index:
#     if df.loc[x, 'sepal_length'] > 5:
#         df.loc[x, 'sepal_length'] = 5
```

This was a demonstration of how to manually correct values that look wrong or unrealistic:
- `df.loc[row, column] = value` directly edits one specific cell.
- The loop version scans **every row** and caps any `sepal_length` value greater than 5 down to 5 — a simple manual way to clip outliers.

I kept this commented out since the actual IRIS dataset doesn't have any bad values — this was purely to demonstrate the technique.

---

## 18. Checking for Duplicate Rows

```python
df.duplicated()
```

Returns `True`/`False` per row — `True` means that row is an exact duplicate of an earlier row in the dataset.

---

## 19. Counting Total Duplicates

```python
df.duplicated().sum()
```

Same logic as `isnull().sum()` — adds up how many duplicate rows exist in total, instead of having to scroll through True/False values manually.

---

## 20. Removing Duplicate Rows

```python
df.drop_duplicates(inplace=True)
df.duplicated().sum()  # confirms 0 duplicates remain after cleaning
```

`drop_duplicates()` removes the repeated rows, keeping only the first occurrence of each. Running `.duplicated().sum()` again afterward confirms the cleanup worked — it should return `0`.

---

## Key Takeaways From Today

- Always inspect a new dataset with `.head()`, `.shape`, `.info()`, and `.describe()` before doing anything else.
- Check for both **missing values** (`isnull`) and **duplicates** (`duplicated`) early — these are the two most common data quality issues.
- Always remember `inplace=True` when you want changes to persist on `df` directly, otherwise pandas returns a copy and your original DataFrame stays unchanged.
- `axis=0` (rows) vs `axis=1` (columns) is a small detail that completely changes what an operation does — worth double-checking every time.