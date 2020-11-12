import logging
import random
import re

import emoji
import streamlit as st
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

logger = logging.getLogger("hinglish")


class HinglishSentiment:
    def __init__(self):
        self.model_name = "Hinglish-Bert-Class"
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.classifier = pipeline(
            "sentiment-analysis", model=self.model, tokenizer=self.tokenizer
        )

    def clean(self, tweet):
        text = tweet
        text = re.sub(r"RT\s@\w+:", "Retweet", text)
        text = re.sub(r"@\w+", "mention", text)
        text = re.sub(r"#\w+", "hashtag", text)
        text = re.sub(r"http\S+", "", text)
        text = emoji.demojize(text)
        print(f"Cleaned Text : {text}")
        return text

    def mood(self, tweet: str, no_variation: bool = False) -> str:
        sentiment = self.classifier(self.clean(tweet))[0]["label"]
        print(f"Sentiment : {sentiment}")
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
