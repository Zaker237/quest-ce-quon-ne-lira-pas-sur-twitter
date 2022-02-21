import tweepy


class TwitterStream(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    # the function containing the logic on what to do for each tweet
    def on_status(self, tweet):
        # We only want the bot to like original the tweet.
        # We also to save the originale tweet in our dab
        if tweet.in_reply_to_status_id is not None or \
            tweet.use.id == self.me.id:
            return    # If we haven't retweeted this tweet yet, retweet it   
        if not tweet.favorited:
        try: 
            tweet.favorite()
            print("Tweet favorited successfully")
        except Exception as e:
            print(e)

    def on_error(self, status):
        print(f"Error while retweeting: {status}")