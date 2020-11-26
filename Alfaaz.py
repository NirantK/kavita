import os
import random
import re
import time
import webbrowser

import streamlit as st
import tweepy
from dotenv import load_dotenv

from sentiment_detection import HinglishSentiment

load_dotenv()


# @st.cache(
#     suppress_st_warning=True,
#     show_spinner=False,
#     persist=True,
#     allow_output_mutation=True,
# )
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
    auth = tweepy.OAuthHandler(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])
    auth.set_access_token(os.environ["ACCESS_KEY"], os.environ["ACCESS_SECRET"])
    twitter_API = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    print("Authenticated twitter API")
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
        print(f"tweet_id : {tweet_id}")
        if tweet_id[-5:] == "?s=20":
            tweet_id = tweet_id[:-5]
        tweet = twitter_API.get_status(tweet_id[0]).text
        print(f"Tweet Recieved : {tweet}")
    except:
        st.error(
            "Sorry, bottie isn't able to fetch the tweet from the URL provided. Can you check your URL or try a different one?"
        )
        print("Tweepy Error")
        return
    return tweet


def verify_credentials(twitter_API):
    try:
        twitter_API.verify_credentials()
        print("Authentication Ok")
    except:
        print("Error during authentication")


@st.cache(
    suppress_st_warning=True,
    show_spinner=False,
    # persist=True,
    allow_output_mutation=True,
)
def load_model():
    """This loads the HinglishSentiment which is internally loading
    the huggingface Hinglish Models which are either locally loded in
    the server and if the models are missing they will be downloaded
    from huggingface model hub and then loaded.
    Returns:
        HinglishSentiment: higlish sentiment detector.
    """
    detector = HinglishSentiment()
    print("Loading Hinglish Detector")
    return detector


def main():
    # Running this from main because in future we can use fire to give
    # more commandline options to this
    # st.title("HinglishBot: Sentiment Analysis Tool")
    st.markdown("![img](https://raw.githubusercontent.com/NirantK/kavita/class/Hinglish-Bot-Image.png)")

    dummy_tweet = "enter a tweet url here, eg - https://twitter.com/Twitter/status/1320822556614676480"

    preview_count = 9
    warning_count = 10000
    api = get_twitter_api()
    verify_credentials(api)
    list_of_display_messages = [
        "Asking the crowds what they think",
        "The committee is making up it's mind",
        "The crew is coordinating with their captain",
    ]
    st.sidebar.markdown("## About this project : Hinglish Bottie")
    st.sidebar.markdown(
        "Hinglish, romanised Hindi, is commonly used informally \
        on social media a lot. This work uses the models we created for SemEval Task 9 2020 \
        to analyse tweets and their sentiment. All you need to do is simply enter \
        the URL of the tweet and it will return it's sentiment"
    )
    st.sidebar.markdown("## Want to read the paper?")
    st.sidebar.markdown(
        "[HinglishNLP: Fine-tuned Language Models for Hinglish Sentiment Detection](https://arxiv.org/abs/2008.09820)"
    )
    st.sidebar.markdown("## You can say hello to us on twitter")
    st.sidebar.markdown("[Meghana Bhange](https://twitter.com/meghanabhange)")
    st.sidebar.markdown("[Nirant Kasliwal](https://twitter.com/nirantk)")
    st.sidebar.markdown("[Radhika Sethi](https://twitter.com/breezybadgerr)")

    with st.spinner(random.choice(list_of_display_messages)):
        detector = load_model()
    st.markdown(
        "To get sentiment of a Tweet enter the tweet URL below. \
    This model works the best with Hinglish tweets and you might not get \
    desired results if it is in any other language"
    )
    tweet_url = st.text_input("Enter Tweet URL", dummy_tweet)
    pressed = st.button("Get tweet Sentiment")
    if not (tweet_url == dummy_tweet) and pressed:
        tweet = get_tweet(tweet_url, api)
        if tweet:
            st.write("Tweet: ", tweet)
            with st.spinner(random.choice(list_of_display_messages)):
                sentiment = detector.mood(tweet)
                st.write(sentiment)


if __name__ == "__main__":
    main()
