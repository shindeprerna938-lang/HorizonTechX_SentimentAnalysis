from textblob import TextBlob
import streamlit as st

st.title("Sentiment Analysis")

text = st.text_area("Enter Review")

if st.button("Analyze"):

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        st.success("Positive")

    elif polarity < 0:
        st.error("Negative")

    else:
        st.warning("Neutral")

else:
    st.info("Please enter some text.")