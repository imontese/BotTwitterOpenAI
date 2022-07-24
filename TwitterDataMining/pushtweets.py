# import modules
import tweepy
import os

def writeTweets(dataframe):

    replay = []
    client = tweepy.Client(
        os.getenv('bearer_token'), 
        os.getenv('consumer_key'), 
        os.getenv('consumer_secret'), 
        os.getenv('access_token'), 
        os.getenv('access_token_secret'))

    for i in range(dataframe.shape[0]):
        client.create_tweet(in_reply_to_tweet_id=dataframe.loc[i][1],text= dataframe.loc[i][4])

    print("Tweets Replay Push")
