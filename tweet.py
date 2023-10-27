import tweepy
import time
import pyjokes

# Define your Twitter API credentials
consumer_key = "1PZ6foLWh9GFvPqd69sja4ju6"
consumer_secret = "54WVkKgSPTqBciq34yYwEMN3GCISE4yQ336VuspLemPlXAzVHH"
access_token = "1717808070456381440-3un3LbTzfneVKn7cUXvwDYLZbT3OtZ"
access_token_secret = "s2wpWuvvrhK6r2q6KVQ7NnsfNHgcN4H3GddKtIOPVKNGc"

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
