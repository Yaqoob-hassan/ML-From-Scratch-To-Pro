# Day 05 — Streamlit Full Command Walkthrough

**Project:** US Airline Sentiment Dashboard
**Dataset:** Twitter US Airline Sentiment (Kaggle)
**File:** `app_full_beginner.py`

## Topics Covered Today

1. **Core display helpers** — `st.title()`, `st.header()`, `st.subheader()`, `st.markdown()`, `st.write()`, `st.code()`
2. **Status / info messages** — `st.info()`, `st.success()`, `st.warning()`, `st.error()`
3. **Caching** — `@st.cache_data` for loading `Tweets.csv` efficiently
4. **Data display** — `st.dataframe()`, `st.table()`, `st.json()`, `st.metric()`
5. **Charts & plots** — `st.bar_chart()`, `st.area_chart()`, and a Matplotlib histogram with `st.pyplot()`
6. **Widgets (user input)** — `st.button()`, `st.checkbox()`, `st.radio()`, `st.selectbox()`, `st.multiselect()`, `st.slider()`, `st.select_slider()`, `st.text_input()`, `st.text_area()`, `st.number_input()`, `st.date_input()`, `st.time_input()`, `st.file_uploader()`, `st.color_picker()`
7. **Forms** — `st.form()` and `st.form_submit_button()` for grouped, single-submit input
8. **Layout & containers** — `st.sidebar`, `st.columns()`, `st.container()`, `st.expander()`, `st.empty()`
9. **File download** — `st.download_button()` for exporting filtered tweet data
10. **Session state & callbacks** — `st.session_state` and `on_click` callbacks to build a persistent tweet-viewer counter

## Key Takeaway

Every Streamlit command was mapped directly onto a real column or real question about the airline dataset (sentiment counts, confidence scores, negative reasons, airline names) rather than generic placeholder examples — so each widget or display function has an immediate, practical use case tied to the data.
