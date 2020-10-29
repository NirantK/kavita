import tweepy 
import time
import os
import streamlit as st 
import re
from sentiment_detection import mood
#credentials = yaml.load(open('TestbaseRadhika/.github/workflows/secrets.yaml'))
auth = tweepy.OAuthHandler( os.environ['CONSUMER_KEY'] , os.environ['CONSUMER_SECRET'] )
auth.set_access_token( os.environ['ACCESS_KEY'] , os.environ['ACCESS_SECRET'] )

def get_twitter_api(auth):
    twitter_API = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return twitter_API

def get_tweet(tweet_url, twitter_API):
    try : 
        tweet_id = re.findall("(?<=status\/)(.*)(?=\?s)", tweet_url)
        tweet = twitter_API.get_status(tweet_id[0]).text
    except:
        raise ValueError("Invalid tweet, please try again")
    return tweet
    
st.title("HinglishBot: Sentiment Analysis Tool")
st.image(
    image="https://verloop.io/wp-content/uploads/2020/08/cropped-VP.io-Website-Grey@2x.png"
)

dummy_tweet = 'enter a tweet url here, eg - https://twitter.com/Twitter/status/1320822556614676480'
preview_count = 9
warning_count = 10000
api = get_twitter_api(auth)
tweet_url = st.text_input('Enter Tweet URL', dummy_tweet)
if not (tweet_url==dummy_tweet):
    tweet = get_tweet(tweet_url, api)
    st.write('Tweet: ', tweet)
    sentiment = mood(tweet)
    st.write('Answer: ', sentiment)