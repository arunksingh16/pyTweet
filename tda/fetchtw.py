"""
A module is a file containing Python definitions and statements. 
The file name is the module name with the suffix .py appended. 
Within a module, the module’s name (as a string) is available as the value of the global variable __name__.
"""

import os
import tweepy as tw
import pandas as pd

# According to PEP8: Class names must follow CamelCase naming
class TdaClass():
    # slots provide a special mechanism to reduce the size of objects.It is a concept of memory optimisation on objects.
    
    __slots__ = ['query','actName','tweetCount','consumer_key','consumer_secret','access_token','access_token_secret']

    def __init__(self) -> None:
        pass

    def createAPIObj(consumer_key,consumer_secret,access_token,access_token_secret):
        auth = tw.OAuthHandler(consumer_key, consumer_secret)
        auth.secure = True
        auth.set_access_token(access_token, access_token_secret)
        api = tw.API(auth)
        return(api)
    
    def tweet_home_tl(consumer_key,consumer_secret,access_token,access_token_secret):
        api = TdaClass.createAPIObj(consumer_key,consumer_secret,access_token,access_token_secret)
        
        for tweet in api.home_timeline():
            tw_ = tweet.user.screen_name
            lo_ = tweet.user.location
            print(f"user name {tw_} and the loc is {lo_}")

    def get_tw(actName,tweetCount,consumer_key,consumer_secret,access_token,access_token_secret):
        api = TdaClass.createAPIObj(consumer_key,consumer_secret,access_token,access_token_secret)

        """"
            :param actName: Name of account for search
            :raise TypeError: If the given parser is not a ModelParser instance.
        """

        print(f"Account in use - {api.me().name}")
        results = api.user_timeline(id=actName, count=tweetCount)
        i = 0
        # foreach through all tweets pulled
        for tweet in results:
        # printing the text stored inside the tweet object
            print(f"Tweet {i} - {tweet.text}")
            i = i + 1

    def search_tw(query,consumer_key,consumer_secret,access_token,access_token_secret,language="en"):
        api = TdaClass.createAPIObj(consumer_key,consumer_secret,access_token,access_token_secret)

        """"
            :param actName: Name of account for search
            :raise TypeError: If the given parser is not a ModelParser instance.
        """

        print(f"Account in use - {api.me().name}")
        results = api.search(q=query, lang=language)
        for tweet in results:
            print(tweet.user.screen_name,"Tweeted:",tweet.text)
