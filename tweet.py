import os
import tweepy
import random
import configparser
import requests

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

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api =tweepy.API(auth)

def joke():
    joke= requests.get("https://v2.jokeapi.dev/joke/Any?type=single").json()["joke"]
    response = client.create_tweet(text=joke)
    print(f"Tweet posted: https://twitter.com/user/status/{response.data['id']}")

def meme():
    meme_api_url = "https://meme-api.com/gimme"
    response = requests.get(meme_api_url)
    if response.status_code == 200:
        url= response.json()["url"]
    else:
        return None
    
    #save the meme
    image = requests.get(url).content
    with open('meme_temp.jpg', 'wb') as handler:
        handler.write(image)
    
    #get media id
    media_id = api.media_upload(filename="meme_temp.jpg").media_id
    
    #tweet
    response = client.create_tweet(media_ids=[media_id])
    print(f"Tweet posted: https://twitter.com/user/status/{response.data['id']}")
    
    #get rid of meme file
    os.remove("meme_temp.jpg")
    
def main():
    tweet = random.choice([joke,meme])
    tweet()

if __name__ == '__main__':
    main()
# End of the script
