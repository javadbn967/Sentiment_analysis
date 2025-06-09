import streamlit as st
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😠"
    else:
        return "Neutral 😐"

st.title("Sentiment Analyzer Web")
text = st.text_area("This robot can analyze emotions within a sentence. Just write your text.")

if st.button("analyze"):
    if text.strip():
        result = analyze_sentiment(text)
        st.success(f"Results: {result}")
    else:
        st.warning("Be sure to write a text!")
