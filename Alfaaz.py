import os
import re
import time

import streamlit as st
import tweepy

from sentiment_detection import mood


def get_twitter_api(auth):
    twitter_API = tweepy.API(
        auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True
    )
    return twitter_API


def get_tweet(tweet_url: str, twitter_API):
    try:
        tweet_id = re.findall("(?<=status\/)(.*)(?=\?s)", tweet_url)
        tweet = twitter_API.get_status(tweet_id[0]).text
    except:
        st.error("Invalid tweet, please try again")
    return tweet


# credentials = yaml.load(open('TestbaseRadhika/.github/workflows/secrets.yaml'))
auth = tweepy.OAuthHandler(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])
auth.set_access_token(os.environ["ACCESS_KEY"], os.environ["ACCESS_SECRET"])
st.title("HinglishBot: Sentiment Analysis Tool")

dummy_tweet = "enter a tweet url here, eg - https://twitter.com/Twitter/status/1320822556614676480"

preview_count = 9
warning_count = 10000
api = get_twitter_api(auth)
list_of_display_messages = [
    "Asking the crowds what they think",
    "The committee is making up it's mind",
    "The crew is coordinating with their captain",
]
tweet_url = st.text_input("Enter Tweet URL", dummy_tweet)
import random

if not (tweet_url == dummy_tweet):
    tweet = get_tweet(tweet_url, api)
    st.write("Tweet: ", tweet)
    with st.spinner(random.choice(list_of_display_messages)):
        sentiment = mood(tweet)
        st.write(sentiment)
