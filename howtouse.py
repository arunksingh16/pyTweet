import os
import datetime
from tda.fetchtw import tdaClass

# Creating the authentication object

if __name__ == '__main__':
    consumer_key = "xxx"
    consumer_secret = "xxx"
    access_token = "xxx-xxxxxx"
    access_token_secret = "xxxxxx"
    x = datetime.datetime.now()
    print(f"Execution Started : {x}")
    #tdaClass.get_tw("nytimes",5,consumer_key,consumer_secret,access_token,access_token_secret)
    #tdaClass.tweet_home_tl(consumer_key,consumer_secret,access_token,access_token_secret)
    tdaClass.search_tw("hanuman",consumer_key,consumer_secret,access_token,access_token_secret)
