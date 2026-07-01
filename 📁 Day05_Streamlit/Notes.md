# Streamlit Notes — US Airline Sentiment Dashboard (Full Walkthrough)

**Dataset:** Twitter US Airline Sentiment (Kaggle) — `Tweets.csv`
**File covered:** `app_full_beginner.py`

This document explains every section and line of the code, in order, so it can be followed top to bottom while teaching.

---

## Running the App

```bash
streamlit run app_full_beginner.py
```

Streamlit re-runs this **entire script from top to bottom** every time a widget is interacted with (button clicked, slider moved, etc.). Keep this in mind — it explains why caching (Section 3) matters, and why widget state (Section 10) needs `st.session_state` to persist across reruns.

---

## Imports

```python
import time
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
```

- `streamlit as st` — the framework itself; every UI element is `st.something()`.
- `pandas as pd` — used to load and manipulate `Tweets.csv`.
- `matplotlib.pyplot as plt` — used later to build a histogram (Section 5).
- `altair as alt` — imported for chart building, though not used directly in this version of the file (kept available for future charts).
- `time` — imported for potential use with delays/progress bars (not used in this version, but commonly paired with `st.spinner`).

---

## 1. Core Display Helpers

```python
st.title("US Airline Sentiment Dashboard")
st.header("A Beginner's Tour of Streamlit Commands")
st.subheader("Built using the Twitter US Airline Sentiment dataset")
st.markdown("This app is **bold** proof that markdown works in Streamlit.")
st.write({"airline": "Delta", "sentiment": "positive"})
st.code("df['airline_sentiment'].value_counts()", language="python")
```

| Command | Purpose |
|---|---|
| `st.title()` | Largest heading on the page — used once, at the very top |
| `st.header()` | Section-level heading, smaller than title |
| `st.subheader()` | Sub-section heading, smaller than header |
| `st.markdown()` | Renders Markdown formatting — `**bold**` becomes bold text |
| `st.write()` | The most flexible display function — here it auto-renders a Python dict nicely |
| `st.code()` | Displays a syntax-highlighted, non-executed code block — good for teaching, since it shows code without running it |

**Why this order matters when teaching:** these are the "print statements" of Streamlit — the first thing any beginner needs before touching data or widgets.

---

## 2. Status / Info Messages

```python
st.info("Info: this dashboard analyzes tweets about US airlines.")
st.success("Success: dataset loaded without errors.")
st.warning("Warning: some tweets have missing location data.")
st.error("Error example: this is what a red error box looks like.")
```

Each of these renders a colored callout box:
- `st.info()` → blue — neutral information
- `st.success()` → green — confirms something worked
- `st.warning()` → yellow/orange — flags something to watch out for (used here honestly — the dataset *does* have missing `tweet_coord` values)
- `st.error()` → red — signals a problem

**Teaching tie-in:** these four boxes map naturally onto real dashboard states (data loaded fine / data has issues / something failed), not just cosmetic demo text.

---

## 3. Caching — Loading the Dataset

```python
@st.cache_data
def load_data():
    df = pd.read_csv("Tweets.csv")
    return df

df = load_data()
```

- `@st.cache_data` tells Streamlit: *"run this function once, store its result, and reuse that result on future reruns instead of recomputing it."*
- Without this decorator, `pd.read_csv("Tweets.csv")` — a ~14,600 row file — would reload from disk on **every single widget interaction**, which is slow and wasteful.
- `st.cache_data` is specifically for **data** (DataFrames, arrays, JSON). It returns a fresh copy each call, so later code can safely filter/modify `df` without corrupting the cached original.

**Path note:** this version uses a plain relative path `"Tweets.csv"`, so the script must be run from the same folder the CSV lives in, or you'll hit `FileNotFoundError`.

---

## 4. Data Display

```python
st.dataframe(df.head())
st.table(df.head(5))
st.json(df.iloc[0].to_dict())

positive_pct = (df["airline_sentiment"] == "positive").mean() * 100
st.metric(
    label="Positive Tweet %",
    value=f"{positive_pct:.1f}%",
    delta="vs overall average",
)
```

- `st.dataframe()` — interactive, scrollable grid. Safe for large data since it virtualizes rendering.
- `st.table()` — static HTML table. **Only ever call this on a small slice** (`.head(5)` here) — calling it on the full ~14,600-row DataFrame can freeze the browser tab.
- `st.json()` — pretty-prints a dictionary as collapsible JSON. Here it's used on a single tweet row (`df.iloc[0]`, converted with `.to_dict()`).
- `st.metric()` — a KPI-style number display, ideal for dashboards. `positive_pct` is calculated with boolean masking: `(df["airline_sentiment"] == "positive")` creates a True/False Series, `.mean()` on that gives the proportion of `True` values, multiplied by 100 for a percentage.

---

## 5. Charts & Plots

```python
sentiment_counts = df["airline_sentiment"].value_counts()

st.bar_chart(sentiment_counts)
st.area_chart(sentiment_counts)

fig, ax = plt.subplots()
ax.hist(df["airline_sentiment_confidence"], bins=20)
ax.set_xlabel("Sentiment Confidence")
ax.set_ylabel("Number of Tweets")
st.pyplot(fig)
```

- `df["airline_sentiment"].value_counts()` — counts how many tweets fall into each sentiment category (`positive`, `neutral`, `negative`). Returns a Series where the index is the category and the values are counts.
- `st.bar_chart()` — correct chart choice for this **categorical** data.
- `st.area_chart()` — same data, different visual style (filled area instead of bars). Shown here just to demonstrate the option exists, not because it's the ideal choice for categorical counts.
- The Matplotlib block builds a **true histogram** of `airline_sentiment_confidence`, which is continuous (0 to 1) — this is the correct use case for a histogram, unlike the categorical sentiment counts above. `st.pyplot(fig)` renders any Matplotlib figure object inside Streamlit.

**Key teaching point:** bar/area charts are for categories; histograms are for continuous numeric distributions. Mixing these up is one of the most common beginner mistakes.

---

## 6. Widgets (User Input)

```python
if st.button("Show 5 random tweets"):
    st.dataframe(df[["name", "text"]].sample(5))
```
- `st.button()` returns `True` only for the rerun immediately after it's clicked, then resets to `False`. Wrapping logic in `if st.button(...):` is the standard pattern.

```python
show_negative = st.checkbox("Show only negative tweets")
if show_negative:
    st.dataframe(df[df["airline_sentiment"] == "negative"][["name", "text"]].head())
```
- `st.checkbox()` returns `True`/`False` and stays in that state until unchecked — unlike a button, it persists across reruns while checked.

```python
sentiment_choice = st.radio("Filter by sentiment", ("positive", "negative", "neutral"))
st.dataframe(df[df["airline_sentiment"] == sentiment_choice][["name", "text"]].head())
```
- `st.radio()` lets the user pick exactly one option from a fixed set. The chosen value is used directly to filter the DataFrame.

```python
airline_choice = st.selectbox("Choose an airline", df["airline"].unique())
st.dataframe(df[df["airline"] == airline_choice][["name", "text"]].head())
```
- `st.selectbox()` — dropdown, single choice. `df["airline"].unique()` dynamically pulls the real list of airlines from the data instead of hardcoding them.

```python
airlines_choice = st.multiselect(
    "Pick multiple airlines", df["airline"].unique(), default=df["airline"].unique()[:2]
)
st.dataframe(df[df["airline"].isin(airlines_choice)][["airline", "text"]].head())
```
- `st.multiselect()` — like `selectbox` but allows multiple picks. `.isin(airlines_choice)` filters rows where the airline matches any of the selected values. `default=` pre-selects the first two airlines so the widget isn't empty on first load.

```python
n_tweets = st.slider("Number of tweets to preview", 1, 50, 10)
st.dataframe(df.head(n_tweets))
```
- `st.slider(label, min, max, default)` — numeric input. Used here to control how many rows of `df.head()` are shown.

```python
confidence_range = st.select_slider(
    "Minimum sentiment confidence", options=[0.0, 0.25, 0.5, 0.75, 1.0], value=0.5,
)
st.write(f"Tweets with confidence >= {confidence_range}:")
st.dataframe(df[df["airline_sentiment_confidence"] >= confidence_range].head())
```
- `st.select_slider()` — like a slider, but snaps to a fixed list of values instead of a continuous numeric range. Used here to filter tweets by minimum sentiment confidence.

```python
username_search = st.text_input("Search by username", value="")
if username_search:
    st.dataframe(df[df["name"].str.contains(username_search, case=False, na=False)])
```
- `st.text_input()` — free text entry. `.str.contains(..., case=False, na=False)` does a case-insensitive substring search, safely skipping rows where `name` is missing (`na=False` prevents an error on NaN values).

```python
feedback = st.text_area("Leave feedback about this dashboard")
```
- `st.text_area()` — like `text_input` but multi-line, good for longer free text.

```python
sample_size = st.number_input("Number of rows to sample", min_value=1, max_value=100, value=5)
st.dataframe(df.sample(int(sample_size)))
```
- `st.number_input()` — numeric entry with min/max bounds. `df.sample(n)` returns `n` random rows each time it's called.

```python
selected_date = st.date_input("Pick a date (demo only, not tied to data)")
selected_time = st.time_input("Pick a time (demo only, not tied to data)")
```
- `st.date_input()` / `st.time_input()` — calendar and clock pickers. Included here as a demo since the dataset's `tweet_created` column isn't filtered by these in this version.

```python
uploaded_file = st.file_uploader("Upload your own tweets CSV", type=["csv"])
if uploaded_file is not None:
    custom_df = pd.read_csv(uploaded_file)
    st.dataframe(custom_df.head())
```
- `st.file_uploader()` — lets a user upload their own file instead of relying only on the bundled `Tweets.csv`. Returns `None` until a file is actually uploaded, hence the `if uploaded_file is not None:` check.

```python
favorite_color = st.color_picker("Pick a theme color", "#1DA1F2")
```
- `st.color_picker()` — returns a hex color string. Default here is Twitter's brand blue, a nice thematic touch for this dataset.

---

## 7. Forms

```python
with st.form("tweet_filter_form"):
    form_airline = st.text_input("Airline name contains")
    form_min_confidence = st.number_input("Minimum confidence", 0.0, 1.0, 0.5)
    submitted = st.form_submit_button("Apply Filter")

if submitted:
    result = df[
        df["airline"].str.contains(form_airline, case=False, na=False)
        & (df["airline_sentiment_confidence"] >= form_min_confidence)
    ]
    st.write(f"Found {len(result)} matching tweets")
    st.dataframe(result[["airline", "text"]].head())
```

- `st.form()` groups multiple widgets so the app **doesn't rerun after every individual keystroke/change** — only when `st.form_submit_button()` is clicked. This is more efficient than the earlier widgets, which each trigger an immediate rerun.
- The filter logic combines two conditions with `&` (boolean AND): airline name matches the text input **and** confidence meets the minimum. Both conditions must be wrapped in parentheses since `&` has higher precedence than `==`/`>=` in Python.

---

## 8. Layout & Containers

```python
st.sidebar.header("Dashboard Filters")
sidebar_airline = st.sidebar.selectbox("Sidebar: choose airline", df["airline"].unique())
```
- Anything called as `st.sidebar.X()` instead of `st.X()` renders in the collapsible sidebar rather than the main page — ideal for filters that should stay visible while scrolling.

```python
col1, col2 = st.columns(2)
with col1:
    st.write("Positive tweet count:")
    st.write(int((df["airline_sentiment"] == "positive").sum()))
with col2:
    st.write("Negative tweet count:")
    st.write(int((df["airline_sentiment"] == "negative").sum()))
```
- `st.columns(2)` splits the page into two side-by-side sections. `with col1:` / `with col2:` route content into each column. `.sum()` on a boolean Series counts how many `True` values there are (i.e., how many rows match the condition).

```python
with st.container():
    st.write("This block is inside a container.")
    st.write(sentiment_counts)
```
- `st.container()` groups elements together logically without adding any visual columns or borders — mainly useful for organizing code or controlling render order.

```python
with st.expander("Click to see negative reasons breakdown"):
    st.dataframe(df["negativereason"].value_counts())
```
- `st.expander()` creates a collapsible section — content stays hidden until the user clicks to expand it. Good for optional detail (here, the breakdown of *why* tweets were negative) that not every viewer needs immediately.

```python
placeholder = st.empty()
placeholder.write("This text can be replaced later using the same placeholder.")
```
- `st.empty()` reserves a spot on the page that can be **overwritten later** by calling `.write()`, `.dataframe()`, etc. on the same `placeholder` variable again elsewhere in the script — useful for live-updating content (e.g., progress bars, streaming text).

---

## 9. File Upload / Download

```python
csv_data = df[df["airline_sentiment"] == sentiment_choice].to_csv(index=False)
st.download_button(
    "Download filtered tweets as CSV",
    data=csv_data,
    file_name=f"{sentiment_choice}_tweets.csv",
)
```

- `.to_csv(index=False)` converts the filtered DataFrame into a CSV-formatted string (without writing to disk), excluding the pandas row index column.
- `st.download_button()` gives the user a real download link in the browser — `data=` is the file content, `file_name=` sets what it's saved as. Notice the filename dynamically includes `sentiment_choice` (from Section 6's radio button), so the downloaded file is named after whatever filter is currently active.

---

## 10. Session State & Callbacks

```python
if "view_count" not in st.session_state:
    st.session_state.view_count = 0

def increment_counter():
    st.session_state.view_count += 1

st.button("View next tweet", on_click=increment_counter)
st.write("Tweets viewed this session:", st.session_state.view_count)

idx = st.session_state.view_count % len(df)
st.write(df.iloc[idx][["name", "airline", "text"]])
```

- `st.session_state` is a dict-like object that **persists across reruns** for a given user session — unlike ordinary Python variables, which reset every time the script reruns.
- The `if "view_count" not in st.session_state:` check initializes the counter only once, the first time the app loads — subsequent reruns skip re-initializing it (which would otherwise reset it back to 0 every click).
- `on_click=increment_counter` — instead of checking `if st.button(...)`, this passes a **callback function** that runs automatically whenever the button is clicked, *before* the rest of the script reruns.
- `idx = st.session_state.view_count % len(df)` uses the modulo operator so the index always wraps back into a valid range (0 to `len(df)-1`), cycling through tweets one at a time each time the button is clicked, no matter how large the counter gets.

---

## Summary Table — All Commands Used

| Category | Commands |
|---|---|
| Display | `st.title`, `st.header`, `st.subheader`, `st.markdown`, `st.write`, `st.code` |
| Status | `st.info`, `st.success`, `st.warning`, `st.error` |
| Caching | `@st.cache_data` |
| Data display | `st.dataframe`, `st.table`, `st.json`, `st.metric` |
| Charts | `st.bar_chart`, `st.area_chart`, `st.pyplot` |
| Widgets | `st.button`, `st.checkbox`, `st.radio`, `st.selectbox`, `st.multiselect`, `st.slider`, `st.select_slider`, `st.text_input`, `st.text_area`, `st.number_input`, `st.date_input`, `st.time_input`, `st.file_uploader`, `st.color_picker` |
| Forms | `st.form`, `st.form_submit_button` |
| Layout | `st.sidebar`, `st.columns`, `st.container`, `st.expander`, `st.empty` |
| File I/O | `st.download_button` |
| State | `st.session_state`, callback functions (`on_click`) |