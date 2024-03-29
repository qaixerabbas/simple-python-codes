# pip install vaderSentiment
# https://pypi.org/project/text2emotion/ for more emotions
#  Happy, Angry, Sad, Surprise and Fear.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time


def sentiment_vader(sentence):

    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    sentiment_dict = sid_obj.polarity_scores(sentence)
    negative = sentiment_dict["neg"]
    neutral = sentiment_dict["neu"]
    positive = sentiment_dict["pos"]
    compound = sentiment_dict["compound"]

    if sentiment_dict["compound"] >= 0.05:
        overall_sentiment = "Positive"

    elif sentiment_dict["compound"] <= -0.05:
        overall_sentiment = "Negative"

    else:
        overall_sentiment = "Neutral"

    return negative, neutral, positive, compound, overall_sentiment


sentences = [
    "I hate chocolate",
    "My cat is adorable ❤️❤️",
    "I can't wait for Halloween!!!",  # neutral by vader and postive by openai
    "This sucks. I'm bored 😠",
    "I can't stand homework",  # neutral by vader and negative by openai
]

time_start = time.time()
for sentence in sentences:
    result = sentiment_vader(sentence)
    print("#################################")
    print(sentence)
    print(result)
    print("##################################")
time_end = time.time()

print(f"Time taken: {time_end - time_start} seconds")
