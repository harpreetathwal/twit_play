import os
import tweepy

API_KEY=os.environ.get('API_KEY')
API_KEY_SECRET=os.environ.get('API_KEY_SECRET')
BEARER_TOKEN=os.environ.get('BEARER_TOKEN')
ACCESS_TOKEN=os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET=os.environ.get('ACCESS_TOKEN_SECRET')


def init():
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)

if __name__ == "__main__":
    secrets = "".join([API_KEY,API_KEY_SECRET,BEARER_TOKEN,ACCESS_TOKEN,ACCESS_TOKEN_SECRET])
    print("Secrets seem present" if secrets else "Secrets missing")
    print("Starting Job: ")
    print(init())