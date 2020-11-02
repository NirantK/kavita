import unittest

from Alfaaz import get_tweet
from sentiment_detection import HinglishSentiment


class TestHinglishSentiement:
    def setUp(self):
        self.detector = HinglishSentiment()

    def test_positive(self):
        output = self.detector.mood(
            "Wow Kya voice hai Yar soooo sweet\
            :smiling_face_with_heart-eyes::smiling_face_with_heart-eyes:\
            :smiling_face_with_heart-eyes::smiling_face_with_heart-eyes:\
            I'm very very very very very very very excited guru sir can't \
            wait :hugging_face::hugging_face::hugging_face:",
            no_variation=True,
        )
        self.assertEqual(output, "POSITIVE")

        output = self.detector.mood(
            "Chhattisgarhiya sable badhiya! \
            Happy Chhattisgarh formation Day!",
            no_variation=True,
        )
        self.assertEqual(output, "POSITIVE")

    def test_negative(self):
        output = self.detector.mood(
            "Hum thaire puncture banane wale log\
            Humko kya isse fark padna h,\
            Fark to ab gaadi ke owners ko padna h.…",
            no_variation=True,
        )
        self.assertEqual(output, "NEGATIVE")

    def test_neutral(self):
        output = self.detector.mood(
            "mention :OK_hand:sir kya ap bta skte \
            h ki ye kb shoot hua tha :thinking_face:please \
            tell me sir please reply me… ",
            no_variation=True,
        )
        self.assertEqual(output, "NEUTRAL")


class TestUtilityFunctions:
    def test_get_tweet(self):
        output = get_tweet(
            "https://twitter.com/breezybadgerr/status/1322883382586437632?s=20"
        )
        self.assertEqual(output, "I'm just happy to see Vettel on #5. #ImolaGP")

        output = get_tweet(
            "https://twitter.com/breezybadgerr/status/1322883382586437632"
        )
        self.assertEqual(output, "I'm just happy to see Vettel on #5. #ImolaGP")
