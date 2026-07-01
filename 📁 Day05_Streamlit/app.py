"""
Streamlit Full Command Reference — Beginner Walkthrough
Dataset: Twitter US Airline Sentiment (Kaggle)

HOW TO RUN THIS FILE:
    streamlit run app_full_beginner.py
"""

import time
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



# 1. CORE DISPLAY HELPERS (text, markdown, code)

st.title("US Airline Sentiment Dashboard")          # large page title
st.header("A Beginner's Tour of Streamlit Commands")  # section header
st.subheader("Built using the Twitter US Airline Sentiment dataset")  # smaller header

st.markdown("This app is **bold** proof that markdown works in Streamlit.")

st.write({"airline": "Delta", "sentiment": "positive"})  # st.write is the "do anything" function

st.code(
    "df['airline_sentiment'].value_counts()",
    language="python",
)  # shows a code block, useful for teaching


# 2. STATUS / INFO MESSAGES

st.info("Info: this dashboard analyzes tweets about US airlines.")
st.success("Success: dataset loaded without errors.")
st.warning("Warning: some tweets have missing location data.")
st.error("Error example: this is what a red error box looks like.")




# 3. CACHING — LOAD THE DATASET

@st.cache_data  # caches the DataFrame so it isn't reloaded on every rerun
def load_data():
    df = pd.read_csv("Tweets.csv")
    return df


df = load_data()

# 4. DATA DISPLAY

st.subheader("Data Display")

st.dataframe(df.head())          # interactive, scrollable table
st.table(df.head(5))             # static table -- only use head(), never the full df here
st.json(df.iloc[0].to_dict())    # formatted JSON of a single tweet row

positive_pct = (df["airline_sentiment"] == "positive").mean() * 100
st.metric(
    label="Positive Tweet %",
    value=f"{positive_pct:.1f}%",
    delta="vs overall average",
)



# 5. CHARTS & PLOTS

st.subheader("Charts & Plots")

sentiment_counts = df["airline_sentiment"].value_counts()

# Categorical data -> bar chart is the correct choice
st.bar_chart(sentiment_counts)

# area_chart works the same way as bar_chart / line_chart -- just a different visual style
st.area_chart(sentiment_counts)

# Matplotlib figure
fig, ax = plt.subplots()
ax.hist(df["airline_sentiment_confidence"], bins=20)
ax.set_xlabel("Sentiment Confidence")
ax.set_ylabel("Number of Tweets")
st.pyplot(fig)


# 6. WIDGETS (USER INPUT)

st.subheader("Widgets")

if st.button("Show 5 random tweets"):
    st.dataframe(df[["name", "text"]].sample(5))

show_negative = st.checkbox("Show only negative tweets")
if show_negative:
    st.dataframe(df[df["airline_sentiment"] == "negative"][["name", "text"]].head())

sentiment_choice = st.radio(
    "Filter by sentiment", ("positive", "negative", "neutral")
)
st.dataframe(df[df["airline_sentiment"] == sentiment_choice][["name", "text"]].head())

airline_choice = st.selectbox("Choose an airline", df["airline"].unique())
st.dataframe(df[df["airline"] == airline_choice][["name", "text"]].head())

airlines_choice = st.multiselect(
    "Pick multiple airlines", df["airline"].unique(), default=df["airline"].unique()[:2]
)
st.dataframe(df[df["airline"].isin(airlines_choice)][["airline", "text"]].head())

n_tweets = st.slider("Number of tweets to preview", 1, 50, 10)
st.dataframe(df.head(n_tweets))

confidence_range = st.select_slider(
    "Minimum sentiment confidence",
    options=[0.0, 0.25, 0.5, 0.75, 1.0],
    value=0.5,
)
st.write(f"Tweets with confidence >= {confidence_range}:")
st.dataframe(df[df["airline_sentiment_confidence"] >= confidence_range].head())

username_search = st.text_input("Search by username", value="")
if username_search:
    st.dataframe(df[df["name"].str.contains(username_search, case=False, na=False)])

feedback = st.text_area("Leave feedback about this dashboard")

sample_size = st.number_input("Number of rows to sample", min_value=1, max_value=100, value=5)
st.dataframe(df.sample(int(sample_size)))

selected_date = st.date_input("Pick a date (demo only, not tied to data)")
selected_time = st.time_input("Pick a time (demo only, not tied to data)")

uploaded_file = st.file_uploader("Upload your own tweets CSV", type=["csv"])
if uploaded_file is not None:
    custom_df = pd.read_csv(uploaded_file)
    st.dataframe(custom_df.head())

favorite_color = st.color_picker("Pick a theme color", "#1DA1F2")  # Twitter blue as default


# 7. FORMS (grouped inputs + single submit)

st.subheader("Forms")

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



# 8. LAYOUT & CONTAINERS

st.subheader("Layout")

# Sidebar — put filters here in a real app
st.sidebar.header("Dashboard Filters")
sidebar_airline = st.sidebar.selectbox("Sidebar: choose airline", df["airline"].unique())

# Columns
col1, col2 = st.columns(2)
with col1:
    st.write("Positive tweet count:")
    st.write(int((df["airline_sentiment"] == "positive").sum()))
with col2:
    st.write("Negative tweet count:")
    st.write(int((df["airline_sentiment"] == "negative").sum()))

# Container — groups elements together
with st.container():
    st.write("This block is inside a container.")
    st.write(sentiment_counts)

# Expander — collapsible section, good for optional detail
with st.expander("Click to see negative reasons breakdown"):
    st.dataframe(df["negativereason"].value_counts())

# Empty — a placeholder you can update later
placeholder = st.empty()
placeholder.write("This text can be replaced later using the same placeholder.")


# 9. FILE UPLOAD / DOWNLOAD

st.subheader("Download Filtered Data")

csv_data = df[df["airline_sentiment"] == sentiment_choice].to_csv(index=False)
st.download_button(
    "Download filtered tweets as CSV",
    data=csv_data,
    file_name=f"{sentiment_choice}_tweets.csv",
)



# 10. SESSION STATE & CALLBACKS

st.subheader("Session State — Tweet Viewer Counter")

if "view_count" not in st.session_state:
    st.session_state.view_count = 0


def increment_counter():
    st.session_state.view_count += 1


st.button("View next tweet", on_click=increment_counter)
st.write("Tweets viewed this session:", st.session_state.view_count)

idx = st.session_state.view_count % len(df)
st.write(df.iloc[idx][["name", "airline", "text"]])






