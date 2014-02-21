import tweepy 
import sys
import twitterhelpers as th 
import codecs
import json

auth = tweepy.OAuthHandler(th.CONSUMER_KEY, th.CONSUMER_SECRET)
auth.set_access_token(th.ACCESS_TOKEN, th.ACCESS_TOKEN_SECRET)

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        print tweet.text

    def on_error(self, status_code):
        print 'Error: ' + repr(status_code)
        return False

    def on_data(self, data):
        pass
        # print 'Ok! Inserting Data.'
        # from pymongo import MongoClient
        # client = MongoClient()
        # client = MongoClient('localhost', 27017)
        # db = client.test
        # test_id = db.twittertest.insert(json.loads(data))


streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener(), parser=MyModelParser(), timeout=60)
streaming_api.filter(follow=None, track=filter)


# l = StreamListener()

# streamer = tweepy.Stream(auth=auth, listener=l)

# streamer.sample()