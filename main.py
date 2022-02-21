import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

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

import tweepy# create new class "StreamListener" 
# takes in tweepy.StreamListener as a parameter
class StreamListener(tweepy.StreamListener):
  def __init__(self, api):
    self.api = api
    self.me = api.me()

Next, we’re going to definte two functions: on_status and on_error. The on_status function will contain the logic behind what we do with each tweet we receive from the stream listener. The on_error function will contain the logic behind what happens if something goes wrong.

in streamlistener.py# import dependencies
import tweepy# create new class "StreamListener" 
# takes in tweepy.StreamListener as a parameter
class StreamListener(tweepy.StreamListener):
  def __init__(self, api):
    self.api = api
    self.me = api.me()
  
  # the function containing the logic on what to do for each tweet
  def on_status(self, tweet):
    # We only want the bot to retweet original tweets, not replies.
    # We also don't want the bot to retweet itself
    if tweet.in_reply_to_status_id is not None or \
      tweet.use.id == self.me.id:
      return    # If we haven't retweeted this tweet yet, retweet it   
    if not tweet.retweeted:
      try: 
        tweet.retweet()
        print("Tweet retweeted successfully")
      except Exception as e:
        print(e)  # the function containing the logic in case there is an error  
  def on_error(self, status):
    print(f"Error while retweeting: {status}")

In the on_status function, we want to ignore any tweets that are replies to other tweets, and we want the bot to ignore it’s own retweets. To do this, we just check for those conditions and simply “return” if they are true. After this, we check if we have already retweeted that tweet and if not, we use the retweet() method that is available to the tweet object to retweet that tweet.

    As a side note, some bots also favorite the tweet when they retweet it. If you also want this functionality, you just check to see if you have favorited the tweet already in the same way you check for retweets, and then you use the favorite() method available to the tweet object.

  # the function containing the logic on what to do for each tweet
  def on_status(self, tweet):
    # We only want the bot to retweet original tweets, not replies.
    # We also don't want the bot to retweet itself
    if tweet.in_reply_to_status_id is not None or \
      tweet.use.id == self.me.id:
      return    # If we haven't retweeted this tweet yet, retweet it   
    if not tweet.retweeted:
      try: 
        tweet.retweet()
        print("Tweet retweeted successfully")
      except Exception as e:
        print(e)    # If we haven't favorited this tweet yet, favorite it
    if not tweet.favorited:
      try:
        tweet.favorite()
        print("Tweet favorited successfully")
      except Exception as e:
        print(e)

Now that we’ve completed this file, we can now use it in our bot.py file. Import the StreamListener class and instantiate a new StreamListener object. Pass in the Twitter API object as a parameter. After this, we’re going to instantiate a tweepy.Stream object, passing in our Twitter API’s auth parameter and the new StreamListener object.

After this, we use the filter() method available to the tweepy.Stream class, passing in ‘track=[“#100DaysOfCode”, “#AnotherHashtagWeMightWannaTrack”]’ to signal that we want to track these specific hashtags/search results and ‘languages=[“en”, “MaybeSomeOtherLanguage”]’ to signal that we only want tweets in English and maybe another specific language. Your bot.py should now look something like:

in bot.py# import dependencies
import tweepy
import os
from dotenv import load_dotenv
from streamlistener import StreamListener <-- Make sure to have this# load our .env file to make use of the environment variables
load_dotenv()# import and assign our environment variables
API_KEY = os.getenv('twitter_api_key')
API_SECRET = os.getenv('twitter_api_secret')
ACCESS_TOKEN = os.getenv('twitter_access_token')
TOKEN_SECRET = os.getenv('twitter_token_secret')# instantiate oauth handler and set access token
twitter_oauth = tweepy.OAuthHandler(API_KEY, API_SECRET)
twitter_oauth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)# instantiate tweepy api object using the authentication handler object
twitter_api = tweepy.API(twitter_oauth)# attempt credential verification. prints exception if something is wrong
try:
  print(twitter_api.verify_credentials())
  print("Successfully logged in")
except tweepy.TweepError as e:
  print(e)
except Exception as e:
  print(e)# instantiate a StreamListener object
tweets_listener = StreamListener(twitter_api)# instantiate a tweepy.Stream object
tweet_stream = tweepy.Stream(twitter_api.auth, tweets_listener)# Use the filter method
tweet_stream.filter(track=["#100DaysOfCode", "#30DaysOfCode"], languages=["en"])

At this point, you should be able to run “python bot.py” in your terminal and it will log in and start retweeting and favoriting.
Success!
Conclusion

This is just the tip of the iceberg when it comes to what you can do with this bot. You can add additional logic to StreamListener’s on_status method to do things like filter out other bot users or determine based on someone’s profile whether or not you want to retweet their tweet (trying to implement a filter that tries to identify descriptions that belong to malicious users).

If you found this guide particularly helpful, please feel free to check out @LiquetBot on Twitter, Liquet Bot’s Github Repo, my Ko-Fi, or follow me on medium for more articles like this one. For more information on tweepy, feel free to check out the tutorial I used to make my own bot, or check out tweepy’s official site! Thank you for giving my article a read!

Get an email whenever Liquet publishes.
More from Python in Plain English
Follow

New Python content every day. Follow to join our +400k monthly readers.
Peter Grant

Peter Grant

·Apr 27, 2021
How to Quickly Write Temporary Functions in Python

Or what the heck is a lambda function? — Functions are an extremely common form of code organization, simplification, and clarification in Python. They provide several benefits such as: By creating a command that can be reused over and over you can write it once, then use it repeatedly in several places. …
Python

5 min read
How to Quickly Write Temporary Functions in Python

Share your ideas with millions of readers.
Write on Medium
Hugh Donnelly

Hugh Donnelly

·Apr 27, 2021
Introduction to Python Functions

Instruction, media content, examples, and links to resources that will help you build a foundation for Python competency. Jupyter Notebooks are available on Google Colab and Github. Web Resources Docs.python.org — Functions Docs.python.org — More on Functions What are Python Functions? A function is a block of organized, reusable code that is used to…
Coding

3 min read
An Introduction to Python Functions
Nandhabalan Marimuthu

Nandhabalan Marimuthu

·Apr 27, 2021
An Introduction to Pandas

Pandas is a software library written for the Python programming language. It is used for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series. Installation We can install pandas by entering the following line of code in our command prompt. We…
Python

5 min read
An Introduction to Pandas
Misha Sv

Misha Sv

·Apr 27, 2021
Calculate Factorial in Python (PyShark)

In this article, we will discuss how to calculate factorial in Python — Table of Contents Introduction Factorial formula Calculating factorial in Python Factorial functions in Python Conclusion Introduction Most often you would see factorials in combinatorics algebra and probability theory. Factorials are used in permutations (calculating the number of ways to arrange some objects) and combinations (calculating the number of ways a subset…
Python

3 min read
Calculate Factorial in Python (PyShark)
Adam Cyber

Adam Cyber

·Apr 27, 2021
Turn your Python Script into a ‘Real’ Program with Docker

No one cares if you can reverse a linked list — they want a one-click way to use your software on their machine. Docker makes that possible. Who Should Read This? Have you ever been handed a piece of code or software with a dependency tree that resembles a messy circuit board:
Python

6 min read
Turn your Python Script into a ‘Real’ Program with Docker
Read more from Python in Plain English
More from Medium
Nx Private Cloud is Available!
For teams who want full control of their data, Nx Private Cloud brings the benefits of distributed computation caching and workspace…
MPPKVVCL Call Letter Out for Post of Line Operators (Cintract)
Doctors hate my no-frills, 30-day new job winning strategy
Deploying various type of storage(s) inside Azure Storage account using ARM template
We’re ready to announce the Whitelist TruePNL & Anypad winners! 🔥
How Greenpeace rolled out an engagement platform globally
Deploy Containerized Azure Functions with Docker
Yet another AVaaS. This time with Azure Functions!

Sign In
Liquet
Liquet

I'm a software engineer that enjoys mixing my passions into my code. When I'm working you can usually find me coding Discord Bots.
Follow
Related
Solving the Filter Bubble using Machine Learning
How to Solve the BotClean Challenge from AI Hackerrank Challenges
Most Accurate Forecasting Model Recommender System as a Flask App
GPU vs CPU: Which One Do You Need If You Want to Learn Deep Learning

Help

Status

Writers

Blog

Careers

Privacy

Terms

About

Knowable
To make Medium work, we log user data. By using Medium, you agree to our Privacy Policy, including cookie policy.
