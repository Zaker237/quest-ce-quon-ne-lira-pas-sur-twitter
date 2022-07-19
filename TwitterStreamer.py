import json
import tweepy

class TwitterStream(tweepy.Stream):
    def __init__(self, api_key, api_key_secret, access_token, access_token_secret, db):
        super().__init__(api_key, api_key_secret, access_token, access_token_secret)
        self.db = db

    def on_data(self, data):
        tweet = json.loads(data)

        if not tweet["is_quote_status"]:
            print("it it no a retweet")
            return
        # If we liked retweeted this tweet yet, retweet it   
        #if not tweet["favorited"]:
        #    try: 
        #        tweet.favorite()
        #        print("Tweet favorited successfully")
        #    except Exception as e:
        #        print(e)
        try:
            tweet_id = tweet["quoted_status_id"]
            tweet_date = tweet["quoted_status"]["created_at"]
            content = tweet["quoted_status"]["text"]
            user_id = tweet["quoted_status"]["user"]["id"]
            print(f"tweet id: {tweet_id}\ntweet date: {tweet_date}\ncontent: {content}\nuser id: {user_id}")
            self.db.insert(tweet_id, user_id, content, tweet_date)
        except Exception as e:
            print(e)


    # the function containing the logic on what to do for each tweet
    # def on_status(self, tweet):
    #     #print(f"\n\n{tweet}\n\n")
    #     # We only want the bot to like original the tweet.
    #     # We also to save the originale tweet in our dab
    #     if not tweet.is_quote_status:
    #         print("it it no a retweet")
    #         return
    #     # If we liked retweeted this tweet yet, retweet it   
    #     if not tweet.favorited:
    #         try: 
    #             tweet.favorite()
    #             print("Tweet favorited successfully")
    #         except Exception as e:
    #             print(e)
    #     try:
    #         tweet_id = tweet.quoted_status_id
    #         tweet_date = tweet.quoted_status.created_at
    #         content = tweet.quoted_status.text
    #         user_id = tweet.quoted_status.user.id
    #         print(f"tweet id: {tweet_id}\ntweet date: {tweet_date}\ncontent: {content}\nuser id: {user_id}")
    #         self.db.inset(tweet_id, user_id, content, tweet_date)
    #     except Exception as e:
    #         print(e)

    def on_error(self, status):
        print(f"Error while retweeting: {status}")