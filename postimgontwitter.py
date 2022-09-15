import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

CONSUMER_KEY=os.getenv('CONSUMER_KEY')
CONSUMER_KEY_SECRET=os.getenv('CONSUMER_KEY_SECRET')
ACCESS_TOKEN=os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET=os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
tweet = "Say hi to Dr Gigachad"
image="H:\Memes Persona\Dr. Chad.jpg"
api.update_status_with_media(tweet, image)
print ("Done!")