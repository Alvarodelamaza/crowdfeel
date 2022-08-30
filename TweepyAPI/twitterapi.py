from itertools import count
import tweepy
import configparser
import pandas as pd

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search_tweets(q='*', count=20, geocode="52.132633,5.29126,150km")

# https://www.gps-coordinates.net/

# create dataframe
columns = ['Time', 'User', 'Tweet', 'Location']
data = []
for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text, tweet.geo])

df = pd.DataFrame(data, columns=columns)

# df.to_csv('tweets.csv')

print(df)
