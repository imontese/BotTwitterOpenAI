# import modules
import tweepy
from tweepy.streaming import Stream
import pandas as pd
import numpy as np
import re
import os

# env module
import dotenv
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file, override=True)

# # TWITTER AUTHENTICATER # #
class TwitterAuthenticator():
    '''
    Class for keys authentication
    '''

    def __init__(self) -> None:
        pass

    def authenticate(self):
        # set online authentication
        auth = tweepy.OAuth1UserHandler(
            os.getenv('consumer_key'), 
            os.getenv('consumer_secret'), 
            os.getenv('access_token'), 
            os.getenv('access_token_secret'))

        # calling the API
        api = tweepy.API(auth)

        return api


# # TWEETS RAW DATA # #
class TweeterMining:
    '''
    Processing tweets searched by term
    '''

    df = pd.DataFrame()

    def __init__(self, search_term = None, tweets_amount=5):
        self.search_term = search_term
        self.tweets_amount = tweets_amount
        self.twitter_authenticator = TwitterAuthenticator()


    def get_tweets(self):
        '''
        gets informatio from the tweets, txt, ids, likes, and time.
        '''
        # use lowercases for search term
        search_term = self.search_term
        tweet_amount = self.tweets_amount
        api = self.twitter_authenticator.authenticate()
        tweets_raw = []
        ids = []
        likes = []
        time = []


        # return most recent search word
        # search by topic
        data = tweepy.Cursor(api.search_tweets,
                            q = search_term,
                            lang='en',
                            tweet_mode='extended',
                            ).items(tweet_amount)



        # getting data into a lists
        for tweet in data:
            #print(tweet.text)
            tweets_raw.append(tweet.full_text)
            ids.append(tweet.id)
            likes.append(tweet.favorite_count)
            time.append(tweet.created_at)

        df = pd.DataFrame({'tweets':tweets_raw, 'id':ids,'likes':likes,'time':time})

        # # removing retweets (all the line)
        df = df[~df.tweets.str.contains("RT")]

        self.df = df
        
        return df

    
    def cleaning(self): 
        '''
        removes extra information from the tweets
        '''  
        # cleaning tweets, removing mentioned users (@)
        self.df['tweets'] = self.df['tweets'].str.replace('htt.*', '', regex=True)
        self.df['tweets'] = self.df['tweets'].str.replace(r'@.\w+', '', regex=True)
        self.df['tweets'] = self.df['tweets'].str.replace(r'#.\w+', '', regex=True)
        self.df['tweets'] = self.df['tweets'].str.replace(r'\n', '', regex=True)
        self.df['tweets'] = self.df['tweets'].str.replace(u'[\U0001F600-\U0001F975].+', '', regex=True)

        # reset index
        self.df = self.df.reset_index(drop=True)

        return self.df