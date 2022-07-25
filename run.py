# import modules
from TwitterDataMining.pushtweets import writeTweets
import constants as c
from OpenAI.openai import *
from TwitterDataMining.functions import * 
from pathlib import Path  


# Triggering the entire project
# Do this by python run.py

def run():
    
    search_term = "satellites ?"

    # set variable to search
    tweetsmining = TweeterMining(search_term=search_term, tweets_amount=20)
    # get tweets
    tweetsmining.get_tweets()
    # cleaning tweets
    data = tweetsmining.cleaning()
      
    # getting answers from gpt3
    gpt = GPT3()
    replay = []

    for tweet in data['tweets']:
        temp = gpt.run(tweet)
        replay.append(temp)

    data["replay"] = replay
    data['replay'] = data['replay'].str.replace(r'\n', '', regex=True)

    # save file as csv
    filepath = Path('files/out.csv')  
    filepath.parent.mkdir(parents=True, exist_ok=True)  
    data.to_csv(filepath)  

    # pushing tweets
    pushtweets = writeTweets()
    pushtweets.run(data['id'], data['replay'])

    print(data)

# runs only if the file was executed directly
if __name__ == '__main__':
    run()   