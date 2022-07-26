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
        

    def run(self, ids=None, msg=None):

        replay = []
        
        if ids != None:
            for i in range(ids.shape[0]):
                try:
                    self.client.create_tweet(in_reply_to_tweet_id=ids[i],text= msg[i])
                except Exception as error:
                    print(error)

            print("Tweets Replay Push")

        else:
            try:
                self.client.create_tweet(text= msg)
                print("Tweet push!")
            except Exception as error:
                    print(error)
                
