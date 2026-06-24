# Day 03 — Pandas Basics: Loading & Cleaning Data

Part of the **ML From Scratch to Pro** series.

---

## 📌 Topics Covered Today

- Installing and importing the Pandas library
- Checking the installed Pandas version
- Loading a dataset from a CSV file (`pd.read_csv`)
- Assigning custom column names while reading a file
- Inspecting a DataFrame (`head`, `tail`, `shape`, `info`, `describe`)
- Detecting missing values (`isnull`, `isnull().sum()`)
- Handling missing values — dropping (`dropna`) vs filling (`fillna`)
- Dropping missing values from specific columns using `subset`
- Identifying and manually correcting unusual/outlier values
- Detecting duplicate rows (`duplicated`)
- Removing duplicate rows (`drop_duplicates`)

**Dataset used:** IRIS.csv

---

## 🎯 By the End of This Day, You Will Learn

- How to install Pandas and import it correctly into a project
- How to load any CSV file into a DataFrame and do a first-look inspection of it
- How to quickly judge the size, structure, and statistical shape of a new dataset
- How to detect missing values in a dataset and decide between dropping or filling them
- How to drop missing data from specific columns instead of the whole row
- How to identify and manually fix unusual or out-of-range values in a column
- How to detect and remove duplicate rows to keep a dataset clean
- Why `inplace=True` matters when cleaning data, and the difference between `axis=0` (rows) and `axis=1` (columns)

---

## 📂 Files in This Folder

| File | Purpose |
|---|---|
| `Day03.ipynb` | Hands-on notebook with all code cells run on the IRIS dataset |
| `notes.md` | Detailed written explanation of every command covered today |
| `Day03.md` | This file — topics + learning outcomes overview |

---

➡️ **Next up (Day 04):** Understanding matplotlib and pandas combine 