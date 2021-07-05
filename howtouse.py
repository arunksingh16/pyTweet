import os
import datetime
from tda.fetchtw import TdaClass

# Creating the authentication object

if __name__ == '__main__':
    consumer_key = "xxx"
    consumer_secret = "xxx"
    access_token = "xxx-xxxxxx"
    access_token_secret = "xxxxxx"
    x = datetime.datetime.now()
    print(f"Execution Started : {x}")
    #TdaClass.get_tw("nytimes",5,consumer_key,consumer_secret,access_token,access_token_secret)
    #TdaClass.tweet_home_tl(consumer_key,consumer_secret,access_token,access_token_secret)
    TdaClass.search_tw("hanuman",consumer_key,consumer_secret,access_token,access_token_secret)
