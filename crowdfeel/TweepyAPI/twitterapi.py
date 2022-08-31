import tweepy
import configparser
import pandas as pd
from geopy.geocoders import Nominatim



def authenticate():
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

    return tweepy.API(auth)

#To determine the twitter geo ID, need to use reverse_geocode with lat lon in and find the place_id from the output.
# tweets = api.reverse_geocode(lat=52.132633,long=5.29126,max_results=100)
# tweets = api.search_geo(query='Amsterdam Netherlands')
# tweets = api.geo_id(place_id='99cdab25eddd6bce')

def geo_query(distance,location):
    '''Query to search for the first 1000 tweets with a given latitude and longitude (ex: 52.374649000000005,4.898072467936939,10km) "
    to use tweet_mode="extended", need to change tweet.text to tweet.full_text. '''
    n = 100
    api = authenticate()


    geolocator = Nominatim(user_agent="twitter")
    loc = geolocator.geocode(f" {location} ")
    dist=f"{distance}km"
    geolocation=str(loc.latitude)+","+str(loc.longitude)+","+str(dist)

    tweets = list(tweepy.Cursor(api.search_tweets, q='*', geocode=geolocation,lang='en').items(n))

    columns = ['Time', 'User', 'Tweet', 'Location']
    data = []

    for tweet in tweets:
        data.append([tweet.created_at, tweet.user.screen_name, tweet.text, tweet.geo])

    df = pd.DataFrame(data, columns=columns)

    df.to_csv('tweets_geoloc_1k.csv')

    print('✅saved to csv: tweets_geoloc_1k.csv')

    return df


def hashtag_query(hashtag):
    '''Query to search the first 100 tweets for a given hashtag'''
    n = 100
    api = authenticate()

    hashtags = f"#{hashtag} -filter:retweets"
    tweets = list(tweepy.Cursor(api.search_tweets, q=hashtags, lang='en').items(n))

    columns = ['Time', 'User', 'Tweet', 'Location']
    data = []

    for tweet in tweets:
        data.append([tweet.created_at, tweet.user.screen_name, tweet.text, tweet.geo])

    df = pd.DataFrame(data, columns=columns)

    df.to_csv('tweets_hashtags_1k.csv')

    print('✅saved to csv: tweets_hashtags_1k.csv')

    return df

def combo_query(free_text, hashtag, account):
    '''Query to search Tweets based on keyword, hashtags and username?'''
    n = 100
    api = authenticate()

    # combo = "tesla AND #crypto AND @elonmusk -filter:retweets"
    combo = f"{free_text} AND #{hashtag} AND @{account} -filter:retweets"
    tweets = list(tweepy.Cursor(api.search_tweets, q=combo, lang='en').items(n))

    columns = ['Time', 'User', 'Tweet', 'Location']
    data = []

    for tweet in tweets:
        data.append([tweet.created_at, tweet.user.screen_name, tweet.text, tweet.geo])

    df = pd.DataFrame(data, columns=columns)

    df.to_csv('tweets_combo_1k.csv')

    print('✅saved to csv: tweets_combo_1k.csv')

    return df


# Uncomment these queries in order to run
# geo_query(10,'amsterdam')
# hashtag_query('amsterdam')
# combo_query('tesla','crypto','elonmusk')
