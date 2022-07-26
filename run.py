# import modules
from TwitterDataMining.pushtweets import writeTweets
import constants as c
from OpenAI.openai import *
from TwitterDataMining.functions import * 
from pathlib import Path  


# Triggering the entire project
# Do this by python run.py

def run():
    
    search_term = "US recession"

    # set variable to search
    tweetsmining = TweeterMining(search_term=search_term, tweets_amount=200)
    # get tweets
    tweetsmining.get_tweets()
    # cleaning tweets
    data = tweetsmining.cleaning()
      
    '''
    Answer all questions on the DF

    # getting answers from gpt3
    gpt = GPT3()
    replay = []

    for tweet in data['tweets']:
        temp = gpt.run(tweet)
        replay.append(temp)

    data["replay"] = replay
    data['replay'] = data['replay'].str.replace(r'\n', '', regex=True)

    '''

    # get the most liked tweet
    data = data.sort_values('likes', ascending=False)

    gpt = GPT3()
    msg = data['tweets'][0]
    replay = gpt.run(msg=msg)

    # save file as csv
    filepath = Path('files/out.csv')  
    filepath.parent.mkdir(parents=True, exist_ok=True)  
    data.to_csv(filepath)  

    # pushing tweets
    pushtweets = writeTweets()
    #pushtweets.run(data['id'], data['replay'])


    # tweet
    search_tearm_joined = " #".join(search_term.split())
    msg =  replay + " #" + search_tearm_joined
    pushtweets.run(msg=msg)

    print(data['tweets'][0]) 
    print(replay)

# runs only if the file was executed directly
if __name__ == '__main__':
    run()   