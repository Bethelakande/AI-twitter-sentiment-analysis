from dotenv.main import load_dotenv
import tweepy
import os
import numpy as np
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from scipy.special import softmax
from textblob import TextBlob
load_dotenv()

CUSTOMER_API_KEY = os.getenv("CUSTOMER_API_KEY")
CUSTOMER_API_KEY_SECRET = os.getenv("CUSTOMER_API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
def main(topic):
    auth = tweepy.OAuthHandler(CUSTOMER_API_KEY, CUSTOMER_API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=CUSTOMER_API_KEY, consumer_secret=CUSTOMER_API_KEY_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

    public_tweets = api.search_recent_tweets(topic, max_results=10)
    print(public_tweets)
    for tweets in public_tweets:
        print(tweets.text)
        sentiment = TextBlob(tweets.text)
        print(sentiment.sentiment)

def get_tweet_sentiment(tweet:str):
    tweet_words = []
    for words in tweet.split(' '):
        if words.startswith("@") and len(words) > 1:
            tweet_words.append('@user')
        elif words.startswith("http"):
            tweet_words.append('http')
        else:
            tweet_words.append(words)
    print(tweet_words)
    tweet_Processed = " ".join(tweet_words)
    print(tweet_Processed)
    #Load model

    roberta = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    model = AutoModelForSequenceClassification.from_pretrained(roberta)
    tokenizer = AutoTokenizer.from_pretrained(roberta)

    labels = ['Negative', 'Neutral', 'Positive']

    #sentiment Analysis
    encoded_tweet = tokenizer(tweet_Processed, return_tensors="pt")
    output = model(**encoded_tweet)
    print('output', output)
    scores = output[0][0].detach().numpy()
    print('scores', scores)
    scores = softmax(scores)
    print('Softmax scores', scores)
    print('The shape o the array is:', scores.shape)
    print('The index of the maximum value is:', scores.argmax())
    for i in range(len(scores)):
        print(f'{labels[i]}: {scores[i]}')

    
    if scores[0] == scores.max():
        print('Negative')
        print('The tweet is Negative', labels[scores.argmax()])
    elif scores[1] == scores.max():
        print('Neutral')
        print('The tweet is Neutral', labels[scores.argmax()])
    else:
        print('Positive')
        print('The tweet is Positive', labels[scores.argmax()])
    
    

    

if __name__ == "__main__":
    print("Enter the topic you want to search for")
    print("-------------------")
    """topic = input()
    while topic == "":
        print("Please enter a topic")
        topic = input()
    main(topic)"""

