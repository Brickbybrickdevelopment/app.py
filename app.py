import streamlit as st
import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

st.title('Stock News Sentiment Analysis')
st.write('This app displays the sentiment of the latest news articles for a given stock ticker.')
