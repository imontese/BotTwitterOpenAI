# import modules
from ctypes.wintypes import PINT
import os
import openai

class OpenAI_Auth:

    def __init__(self):
        # load API key from an enviroment variable
        openai.api_key = os.getenv("OPENAI_API_KEY")



class GPT3:

    def __init__(self):
        OpenAI_Auth()
       

    def run(self, msg):
        try:
            response = openai.Completion.create(
                model="text-davinci-002", 
                prompt=msg, 
                temperature=0.7,    # temperature 0-1 represent the risk that the algorithm is taking, 0 being the lowest 
                max_tokens=60,
                top_p=1)
        except:
            print("An exception occurred")

        #replay = response.choice[0].text
        #print(replay)
        return response.choices[0].text

