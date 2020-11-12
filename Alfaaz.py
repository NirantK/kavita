import logging
import os
import random
import re
import time

import streamlit as st
import tweepy

from sentiment_detection import HinglishSentiment

logger = logging.getLogger("hinglish")


@st.cache(allow_output_mutation=True)
def get_twitter_api():
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
    try:
        tweet_id = re.findall("(?<=status\/)(.*)", tweet_url)
        logger.info(f"tweet_id : {tweet_id}")
        if tweet_id[-5:] == "?s=20":
            tweet_id = tweet_id[:-5]
        tweet = twitter_API.get_status(tweet_id[0]).text
        logger.info(f"Tweet Recieved : {tweet}")
    except:
        st.error("Sorry, bottie isn't able to fetch the tweet from the URL provided. Can you check your URL or try a different one?")
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
# credentials = yaml.load(open('TestbaseRadhika/.github/workflows/secrets.yaml'))
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

if __name__ == "__main__":
    main()
