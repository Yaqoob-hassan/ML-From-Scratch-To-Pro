import streamlit as st
import pandas as pd
import plotly.express as px

# For setting up title
st.title("US airline sentimental analysis.")

# A sidebar which displays about it
st.sidebar.title("US airline sentimental analysis.")

# Markdown
st.markdown("This data is about the US airlines.")
st.sidebar.markdown("This data is about the US airlines.")


@st.cache_resource
def load_data():
    data = pd.read_csv("Tweets.csv")
    data['tweet_created'] = pd.to_datetime(data['tweet_created'])
    return data


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


st.sidebar.markdown(" ### Number of tweets by sentiments.")
select = st.sidebar.selectbox("Visualization", ("Histogram", "Pie chart"), key="viz_select")

sentiments_count = df['airline_sentiment'].value_counts()
sentiments_count = pd.DataFrame({'sentiment': sentiments_count.index, 'Tweets': sentiments_count.values})

if not st.sidebar.checkbox("Hide", True, key="hide_checkbox"):
    st.markdown(" ### Number of Tweets by sentiments.")
    if select == 'Histogram':
        fig = px.bar(sentiments_count, x='sentiment', y='Tweets', color='Tweets', height=500)
        st.plotly_chart(fig)
    else:
        fig = px.pie(sentiments_count, values="Tweets", names='sentiment')
        st.plotly_chart(fig)


st.sidebar.markdown("When and where users are tweeting from?")

hour = st.sidebar.slider("Hours of the day", 0, 23, key="hour_slider")

if not st.sidebar.checkbox("close", True, key="close_checkbox"):
    modified_data = df[df["tweet_created"].dt.hour == hour]
    modified_data = modified_data.dropna(subset=['tweet_coord'])
    modified_data[['latitude', 'longitude']] = (
        modified_data['tweet_coord']
        .str.strip('[]')
        .str.split(',', expand=True)
        .astype(float)
    )

    st.markdown("Tweets location based on the day.")
    st.markdown("%i tweets between %i.00 and %i.00 " % (len(modified_data), hour, (hour + 1) % 24))
    st.map(modified_data)