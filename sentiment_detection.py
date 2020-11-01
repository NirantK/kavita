from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import random
class HinglishSentiment:
    def __init__(self):
        self.model_name = "meghanabhange/Hinglish-Bert-Class"
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.classifier = pipeline('sentiment-analysis', model=self.model, tokenizer=self.tokenizer)
        # self.classifier = pipeline('sentiment-analysis')

    def mood(self, tweet: str) -> str:
        sentiment = self.classifier(tweet)[0]["label"]
        variations = [
            f"Oh, your tweet is {sentiment}",
            f"I guess this tweet is {sentiment}",
            f"Guess what, this tweet is {sentiment}",
            f"It appears that your tweet is {sentiment}",
            f"I am just a bot, but I think this tweet is {sentiment}"
        ]
        return random.choice(variations)
