import streamlit as st 
import pandas as pd
import numpy as np
st.title("US airline sentimental analysis.")
st.sidebar.title("US airline sentimental analysis.")

st.markdown("This data is about the US airlines.")
st.sidebar.markdown("This data is about the US airlines.")

df = pd.read_csv("Tweets.csv")

@st.cache_resource


def load_data():
    df['tweet_created'] = pd.to_datetime(df['tweet_created'])
    return df


df = load_data()
st.sidebar.subheader("Random Tweets.")

random_tweet = st.sidebar.radio("Sentimenal Analysis", ('positive', 'negative', 'neutral'))

tweet = (
    df.query("airline_sentiment == @random_tweet")["text"]
      .sample(1)
      .iloc[0]
)


st.write(df["airline_sentiment"].unique())

st.sidebar.markdown(tweet)

