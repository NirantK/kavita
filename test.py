import unittest

from Alfaaz import get_tweet, get_twitter_api
from sentiment_detection import HinglishSentiment


class TestHinglishSentiement(unittest.TestCase):
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

        output = self.detector.mood(
            "mention Ohho badhiya Sheetal ji \
            :beaming_face_with_smiling_eyes \
            :good night :blue_heart:",
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

        output = self.detector.mood(
            "I’m watching Scam 1992 right \
            now and Rajat Kapoor saying Mein \
            chutiya hoon kya lodu is the vitamin \
            I needed today",
            no_variation=True,
        )
        self.assertEqual(output, "NEGATIVE")

        output = self.detector.mood(
            "mention mention lol ye log pagal ho \
            chuke hai.. kahi bhi kuch bhi bol rahe \
            hai.. but its funny",
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

        output = self.detector.mood(
            "I am not gussa...but i am gussa",
            no_variation=True,
        )
        self.assertEqual(output, "NEUTRAL")

        output = self.detector.mood(
            "Arey Git. Chill out nah bro. Empty line hain.",
            no_variation=True,
        )
        self.assertEqual(output, "NEUTRAL")
        output = self.detector.mood(
            "Aur kuch kaam toh bacha hi nahi hai iss desh mein.",
            no_variation=True,
        )
        self.assertEqual(output,"NEUTRAL")
        output = self.detector.mood(
            "Aacha tweleb ko kya bolenge tooter pe", 
            no_variation=True,
        )
        self.assertEqual(output,"NEUTRAL")




class TestUtilityFunctions(unittest.TestCase):
    def setUp(self):
        self.api = get_twitter_api()

    def test_get_tweet(self):
        output = get_tweet(
            "https://twitter.com/breezybadgerr/status/1322883382586437632?s=20",
            self.api,
        )
        self.assertEqual(output, "I'm just happy to see Vettel on #5. \n#ImolaGP")

        output = get_tweet(
            "https://twitter.com/breezybadgerr/status/1322883382586437632", self.api
        )
        self.assertEqual(output, "I'm just happy to see Vettel on #5. \n#ImolaGP")

        output = get_tweet(
            "https://twitter.com/growoverr/status/1329842358725222400?s=20", self.api
        )
        self.assertEqual(output, "11:11 bina padhai kare college ki degree")

        output = get_tweet(
            "https://twitter.com/growoverr/status/1321342899896807424?s=20", self.api

        )
        self.assertEqual(output, "Sometimes I read my own texts and wonder KOI KESE BAAT KARTA MUJHSE ????? mera aapna guess the gibberish challenge chal raha hai waha :(((")

        output = get_tweet(
            "https://twitter.com/youngestadult1/status/1329462598157312000?s=20", self.api

        )
        self.assertEqual(output, "Iss virus Covoid kaise karein?")


