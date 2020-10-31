import re

import tweepy


def get_twitter_api(auth):
    twitter_API = tweepy.API(
        auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True
    )
    return twitter_API


def get_tweet(tweet_url, twitter_API):
    try:
        tweet_id = re.findall("(?<=status\/)(.*)(?=\?s)", tweet_url)
        tweet = twitter_API.get_status(tweet_id[0]).text
    except:
        raise ValueError("Invalid tweet, please try again")
    return tweet
