import tweepy
import time
import pyjokes
import configparser

# Read credentials from config
config = configparser.ConfigParser()
config.read("config.ini")
credentials = config["Credentials"]
consumer_key = credentials["consumer_key"]
consumer_secret = credentials["consumer_secret"]
access_token = credentials["access_token"]
access_token_secret = credentials["access_token_secret"]

# Initialize Tweepy with your API credentials
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# Function to generate humor content
def content():
    # Implement content generation logic here
    return pyjokes.get_joke()

def tweet():
    response = client.create_tweet(text=content())
    print(f"https://twitter.com/user/status/{response.data['id']}") 

tweet()
# End of the script
