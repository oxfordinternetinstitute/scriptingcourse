#!/usr/bin/env python
# -*- coding: utf-8 -*-#
#
# Example capture of streaming data from Twitter
# CODE FROM: 
# http://answers.oreilly.com/topic/2605-how-to-capture-tweets-in-real-time-with-twitters-streaming-api/
#
# Modified by Bernie Hogan
# DSR Week 2. Twitter. 
import tweepy 
import sys
import twitterhelpers as th 
import codecs

auth = tweepy.OAuthHandler(th.CONSUMER_KEY, th.CONSUMER_SECRET)
auth.set_access_token(th.ACCESS_TOKEN, th.ACCESS_TOKEN_SECRET)

class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        
        # We'll simply print some values in a tab-delimited format
        # suitable for capturing to a flat file but you could opt 
        # store them elsewhere, retweet select statuses, etc.

        try:
            print "%s\t%s\t%s\t%s" % (status.author.screen_name, 
                                      status.created_at, 
                                      status.source,
                                      status.text)
        except Exception, e:
            print >> sys.stderr, 'Encountered Exception:', e
            pass

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

# Create a streaming API and set a timeout value of 60 seconds.



streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=60)

# Optionally filter the statuses you want to track by providing a list
# of users to "follow".

filter = ["grammys"]

print >> sys.stderr, 'Filtering the public timeline for "%s"' % (filter)

streaming_api.filter(follow=None, track=filter)