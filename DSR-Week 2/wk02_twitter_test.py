# -*- coding: utf-8 -*-#

"""
Basic Twitter Authentication

requirements: Python 2.5+ tweepy (easy_install tweepy | pip install tweepy)
"""

__author__ =  'Bernie Hogan'
__version__=  '1.0'

import string
import codecs
import os
import pickle
import copy
import sys
import json 
import webbrowser

import tweepy
from tweepy import Cursor
import twitterhelpers as th

def getFollowerCount(api, screen_name="BarackObama"):
	user = api.get_user(screen_name)
	
	return user.followers_count
	 

def getFollowingCount(api, screen_name="BarackObama"):
	user = api.get_user(screen_name)
	print user
	print dir(user)
	return user.friends_count


if __name__=='__main__':
	CONSUMER_KEY = th.CONSUMER_KEY
	CONSUMER_SECRET = th.CONSUMER_SECRET

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

	ACCESS_TOKEN_SECRET = th.ACCESS_TOKEN_SECRET
	ACCESS_TOKEN = th.ACCESS_TOKEN

	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

	api = tweepy.API(auth)

	print "Now you have received an access token."
	print "Or rather, your account has authorized this application to use the twitter api."
	print "You have this many hits to the API left this hour: " 
	# print json.dumps(api.rate_limit_status(), indent = 1) #['remaining_hits']

	print getFollowerCount(api, "blurky")
	print getFollowingCount(api, "blurky")

