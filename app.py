import joblib
import streamlit as st
from utils import clean_text

# Load model
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

st.set_page_config(page_title="Fake News Detector", layout="centered")

st.title("📰 Fake News Detector")
st.write("Enter a news headline or article to check if it's fake or real.")

input_text = st.text_area("Enter News Text")

if st.button("Check"):
    if input_text.strip() == "":
        st.warning("Please enter some text")
    else:
        cleaned = clean_text(input_text)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)[0]

        if prediction == 1:
            st.error("🚨 This looks like FAKE news")
        else:
            st.success("✅ This looks like REAL news")
