import tweepy 
import time
import os
import streamlit as st 
#credentials = yaml.load(open('TestbaseRadhika/.github/workflows/secrets.yaml'))

#CONSUMER_KEY = credentials['env']['CONSUMER_KEY']
#CONSUMER_SECRET = credentials['env']['CONSUME_SECRET']
#ACCESS_KEY = credentials['env']['ACCESS_KEY']
#ACCESS_SECRET = credentials['env']['ACCESS_SECRET']
#print(os.environ)
#print("Hello the key is this - ")
#print(os.environ['CONSUMER_KEY'])
st.title("HinglishBot: Sentiment Analysis Tool")
st.image(
    image="https://verloop.io/wp-content/uploads/2020/08/cropped-VP.io-Website-Grey@2x.png"
)

preview_count = 9
warning_count = 10000

auth = tweepy.OAuthHandler( os.environ['CONSUMER_KEY'] , os.environ['CONSUMER_SECRET'] )
auth.set_access_token( os.environ['ACCESS_KEY'] , os.environ['ACCESS_SECRET'] )

print('just a few more steps to finish this bot') 

twitter_API = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def mention_followers():
    followers = twitter_API.followers()
    for follower in followers:
        print(follower," ")
        twitter_API.update_status('hello yes this is a spam again wot can i do -_- @' + follower.screen_name)
while True:
    mention_followers()
    time.sleep(3600)

