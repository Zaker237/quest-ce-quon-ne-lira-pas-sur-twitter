import tweepy
import os

from TwitterStreamer import TwitterStream
from database import DateBaseManager
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
HASHTAG = os.environ.get("HASHTAG")

twitter_oauth = tweepy.OAuthHandler(API_KEY, API_SECRET)
twitter_oauth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)# instantiate tweepy api object using the authentication handler object
twitter_api = tweepy.API(twitter_oauth)# attempt credential verification. prints exception if something is wrong
try:
  print(twitter_api.verify_credentials())
  print("Successfully logged in")
except tweepy.TweepError as e:
  print(e)
except Exception as e:
  print(e)

tweets_listener = TwitterStream(twitter_api)# instantiate a tweepy.Stream object
tweet_stream = tweepy.Stream(twitter_api.auth, tweets_listener)#
tweet_stream.filter(track=[HASHTAG], languages=["en"])