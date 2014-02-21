#!/usr/bin/env python
# -*- coding: utf-8 -*-#
#
import tweepy 
import sys
import twitterhelpers as th 
import json
from pymongo import MongoClient

auth = tweepy.OAuthHandler(th.CONSUMER_KEY, th.CONSUMER_SECRET)
auth.set_access_token(th.ACCESS_TOKEN, th.ACCESS_TOKEN_SECRET)

class CustomStreamListener(tweepy.StreamListener):

    
    # def on_status(self, status):
        
    #     # We'll simply print some values in a tab-delimited format
    #     # suitable for capturing to a flat file but you could opt 
    #     # store them elsewhere, retweet select statuses, etc.
    #     # print json.dumps(status, indent=1)
    #     try:
    #         print "%s\t%s\t%s\t%s" % (status.author.screen_name, 
    #                                   status.created_at, 
    #                                   status.source,
    #                                   status.text)
    #     except Exception, e:
    #         print >> sys.stderr, 'Encountered Exception:', e
    #         pass

    def __init__ (self):
        self.count = 0

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

    def on_data(self, data):
        self.count += 1

        client = MongoClient('localhost', 27017)
        db = client.test
        db.tweettest2.insert(json.loads(data))

        if self.count % 50 == 0:
            print self.count

        if self.count == 200: 
            print "got 1000 tweets, we're going home"
            sys.exit()

# Create a streaming API and set a timeout value of 60 seconds.
streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=60)

filter = ["justin"]

streaming_api.filter(follow=None, track=filter)