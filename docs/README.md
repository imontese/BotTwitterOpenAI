# Project Title: Twitter Data Analysis and Response  
   
This project mines Twitter data for a specific search term, analyzes the data, and generates responses using OpenAI's GPT-3. The program can also post the generated responses on Twitter.  
   
## Dependencies  
   
- TwitterDataMining module  
- OpenAI module  
- constants module  
- functions module  
- pathlib  
   
## How to use  
   
1. Set up the necessary API keys and tokens for both Twitter and OpenAI.  
2. Install the required dependencies.  
3. Modify the `search_term` variable in the `run()` function with the desired term to search for on Twitter.  
4. Run the program by executing `python run.py` in the terminal.  
   
## Functionality  
   
The program performs the following tasks:  
   
1. Searches for tweets containing the specified search term.  
2. Retrieves and cleans the tweet data.  
3. Sorts the tweets by the number of likes.  
4. Generates a response for the most liked tweet using OpenAI's GPT-3.  
5. Saves the processed data to a CSV file.  
6. Posts the generated response on Twitter.  
   
## Code Structure  
   
- `run()`: The main function that executes the entire project.  
- `TweeterMining`: A class for mining tweets and cleaning the data.  
- `GPT3`: A class for generating responses using OpenAI's GPT-3.  
- `writeTweets`: A class for posting tweets on Twitter.  
   
When executed directly, the `run()` function is called to perform the entire project workflow.

This project uses the Twitter API to search for tweets containing a specified search term, retrieve the tweet data, and post generated responses on Twitter. Ensure that you have the appropriate API API keys and tokens for both Twitter and OpenAI access level and version for your specific use case.