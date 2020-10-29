import tweepy 
import time
import os
import streamlit as st 
#credentials = yaml.load(open('TestbaseRadhika/.github/workflows/secrets.yaml'))

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

followers = []
def mention_followers(followers: list) -> None:
    for follower in followers:
        print(follower," ")
        twitter_API.update_status('yes this is annoying, ugh @' + follower.screen_name)
        
    

def follower_count()->list:
    followers = twitter_API.followers()
    return (followers)

num = []
num = follower_count()
mention_followers(num)
    
    
