import logging
import random
import re

import emoji
import streamlit as st
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

logger = logging.getLogger("hinglish")


class HinglishSentiment:
    def __init__(self):
        try:
            self.classifier = pipeline(
                "sentiment-analysis", model="Hinglish-Bert-Class"
            )
        except:
            logger.info("Model not in RAM, downloading it now.")
            self.classifier = pipeline(
                "sentiment-analysis", model="meghanabhange/Hinglish-Bert-Class"
            )
        # self.classifier = pipeline('sentiment-analysis')

    def clean(self, tweet):
        text = tweet
        text = re.sub(r"RT\s@\w+:", "Retweet", text)
        text = re.sub(r"@\w+", "mention", text)
        text = re.sub(r"#\w+", "hashtag", text)
        text = re.sub(r"http\S+", "", text)
        text = emoji.demojize(text)
        logger.info(f"Cleaned Text : {text}")
        return text

    def mood(self, tweet: str, no_variation: bool = False) -> str:
        sentiment = self.classifier(self.clean(tweet))[0]["label"]
        logger.info(f"Sentiment : {sentiment}")
        if no_variation:
            return sentiment
        variations = [
            f"Oh, your tweet is {sentiment}",
            f"I guess this tweet is {sentiment}",
            f"Guess what, this tweet is {sentiment}",
            f"It appears that your tweet is {sentiment}",
            f"I am just a bot, but I think this tweet is {sentiment}",
        ]
        return random.choice(variations)
