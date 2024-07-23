import streamlit as st
import glob
import plotly.express as px
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pathlib import Path

nltk.download("vader_lexicon")
analyzer = SentimentIntensityAnalyzer()
filepaths = glob.glob("diary/*.txt")


filenames = []
positivity_scores = []
negativity_scores = []

# Extracting the filename from the filepaths and reading the content of the file for NLTK analysis
for filepath in filepaths:
    filename = Path(filepath).stem
    filenames.append(filename)

    with open(filepath, "r") as file:
        content = file.read()
    # Sentiment Analysis
    sentiment = analyzer.polarity_scores(content)

    positivity = sentiment["pos"]
    positivity_scores.append(positivity)
    negativity = sentiment["neg"]
    negativity_scores.append(negativity)

# Plotting the positivity scores
st.header("Positivity")
figure = px.line(x=filenames, y=positivity_scores, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure)


# Plotting the negativity scores
st.header("Negativity")
figure = px.line(x=filenames, y=negativity_scores, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure)

print(type(filenames))
print(type(positivity_scores))
print(type(negativity_scores))
