import logging
import os
import random
import re
import time
import webbrowser

import streamlit as st
import tweepy
from dotenv import load_dotenv

from sentiment_detection import HinglishSentiment

logger = logging.getLogger("hinglish")
load_dotenv()

# @st.cache(allow_output_mutation=True) #DO NOT CHANGE THIS. Now I forgot why this line is really important. But it is. Don't remove.
def get_twitter_api():
    """Authenticates the twitter API from env variables.
    ENV variables that are required are CONSUMER_KEY
    CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET. Pass this
    using github secrets or directly in your app

    Do not push these keys to git.

    Known issue with this function is that it takes too
    log to autheticate and the authentication happens at
    every request. There is no way to just cache tweepy API.
    Thus this function is the speed bottleneck of this
    app.

    Returns:
        tweepy.API: Tweepy API which can be used to query
            and tweet tweets.
    """
    auth = tweepy.OAuthHandler(
        os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"]
    )
    auth.set_access_token(os.environ["ACCESS_KEY"], os.environ["ACCESS_SECRET"])
    twitter_API = tweepy.API(
        auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True
    )
    logger.info("Authenticated twitter API")
    return twitter_API


def get_tweet(tweet_url: str, twitter_API):
    """This gets tweets using tweepy API.
    Currently we are expecting tweets to come in two
    formats.

    It would be either https://twitter.com/verloopio/status/1326787675181944840
    which is copied directly from the url bar or
    https://twitter.com/verloopio/status/1326787675181944840?s=20
    Which is copied through share link option.

    We are using regex to get the tweetID and then using that to
    get the tweet from the URL


    Args:
        tweet_url (str): URL of the tweet whose sentiment you want to analyse
        twitter_API (tweepy.API): TweepyAPI

    Returns:
        str: the tweet from the URL
    """
    try:
        tweet_id = re.findall("(?<=status\/)(.*)", tweet_url)
        logger.info(f"tweet_id : {tweet_id}")
        if tweet_id[-5:] == "?s=20":
            tweet_id = tweet_id[:-5]
        tweet = twitter_API.get_status(tweet_id[0]).text
        logger.info(f"Tweet Recieved : {tweet}")
    except:
        st.error(
            "Sorry, bottie isn't able to fetch the tweet from the URL provided. Can you check your URL or try a different one?"
        )
        logger.exception("Tweepy Error")
        return
    return tweet


def verify_credentials(twitter_API):
    try:
        twitter_API.verify_credentials()
        print("Authentication Ok")
    except:
        print("Error during authentication")


def main():
auth = tweepy.OAuthHandler(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])
auth.set_access_token(os.environ["ACCESS_KEY"], os.environ["ACCESS_SECRET"])
st.title("HinglishBot: Sentiment Analysis Tool")

dummy_tweet = "enter a tweet url here, eg - https://twitter.com/Twitter/status/1320822556614676480"
preview_count = 9
warning_count = 10000
api = get_twitter_api(auth)
verify_credentials(api)
list_of_display_messages = [
    "Asking the crowds what they think",
    "The committee is making up it's mind",
    "The crew is coordinating with their captain",
]
tweet_url = st.text_input("Enter Tweet URL", dummy_tweet)
import random

