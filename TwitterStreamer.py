import tweepy


class TwitterStream(tweepy.StreamListener):
  def __init__(self, api):
    self.api = api
    self.me = api.me()