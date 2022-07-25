# import modules
import tweepy
import os

class writeTweets:

    client = ''

    def __init__(self):
        self.client = tweepy.Client(
            os.getenv('bearer_token'), 
            os.getenv('consumer_key'), 
            os.getenv('consumer_secret'), 
            os.getenv('access_token'), 
            os.getenv('access_token_secret'))
        

    def run(self, ids, msg):

        replay = []
        
        for i in range(ids.shape[0]):
            self.client.create_tweet(in_reply_to_tweet_id=ids[i],text= msg[i])

        print("Tweets Replay Push")
