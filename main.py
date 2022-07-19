import tweepy
import os

from TwitterStreamer import TwitterStream
from database import DataBaseManager
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
HASHTAG = os.environ.get("HASHTAG")

DATABASE_PATH = "db/database.db"

db = DataBaseManager(DATABASE_PATH)

def main(db):
    tweet_stream = TwitterStream(
        API_KEY,
        API_SECRET,
        ACCESS_TOKEN,
        TOKEN_SECRET,
        db
    )
    tweet_stream.filter(track=[HASHTAG])

if __name__ == "__main__":
    db.create_tables()
    main(db)