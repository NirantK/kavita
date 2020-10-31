import os
import re
import time

import streamlit as st
import tweepy

from sentiment_detection import mood
from utils import get_tweet, get_twitter_api

# credentials = yaml.load(open('TestbaseRadhika/.github/workflows/secrets.yaml'))
auth = tweepy.OAuthHandler(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])
auth.set_access_token(os.environ["ACCESS_KEY"], os.environ["ACCESS_SECRET"])
st.title("HinglishBot: Sentiment Analysis Tool")

dummy_tweet = "enter a tweet url here, eg - https://twitter.com/Twitter/status/1320822556614676480"
preview_count = 9
warning_count = 10000
api = get_twitter_api(auth)
tweet_url = st.text_input("Enter Tweet URL", dummy_tweet)
if not (tweet_url == dummy_tweet):
    tweet = get_tweet(tweet_url, api)
    st.write("Tweet: ", tweet)
    sentiment = mood(tweet)
    st.write("Answer: ", sentiment)
