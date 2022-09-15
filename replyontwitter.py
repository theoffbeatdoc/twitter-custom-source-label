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
tweet = "text to reply"
api.update_status(tweet, in_reply_to_status_id = TWEET ID HERE)
print ("Done!")

#For example, in the below Twitter tweet URL, 1570470417416204290 is the tweet id.
#https://twitter.com/theoffbeatdoc/status/1570470417416204290