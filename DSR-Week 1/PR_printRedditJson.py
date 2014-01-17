#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
DSR Week 1: Download and print json from reddit's main page. 

This file contains methods to download and parse Reddit.com's main page.
One could do this hourly to sample reddit activity, and plot it over some metric.
hmmm....

CHANGELOG
version 1.1. 	Fixed bug to send output to the wrong path. 
				Tweaked method attributes. 
				Pretty print is more obvious

version 1.2.    Set time to sleep 3 seconds. Gets around timeout bug. 	

version 1.3.    Reddit subreddit argument added.	
"""

__author__ =  'Bernie Hogan'
__version__=  '1.3'

import json
# import simplejson as json # alternate for < 2.6
import urllib2 
import string
import os
import time 

PATH = (os.getcwd())


def getRedditJson(count=0,after="",url = "http://www.reddit.com/.json",prettyPrint=False):
	'''getRedditJson will append an after and a count to a reddit.com url.
	It can also be used with subreddits/elsewhere, using the optional url'''
	
	if count > 0:
		url += 	"?count=%d&after=%s" % (count,after)
	
	redditfile = urllib2.urlopen(url)

	if prettyPrint:
		return downloadJsonToPretty(url,"reddit-json_%d_%s.json" % (count,after))
	else:
		return json.load( redditfile )


def addToTable(jsondata,fileoutpath,count,header=False):
	'''This method takes a json file and adds it to a table. 
	Notice the header is only added if the count is 0. 
	- Certainly, there\'s tidier way to do this?'''
	
	outstr = ""
	
	queries = ["rank","ups","downs"]
	
	if count == 0:
		fileout = open(fileoutpath,'w')
		outstr += "queries\tups\tdowns\tscore\tcomments\tsubmitter\n"
	else:
		fileout = open(fileoutpath,'a')
		
	for c,i in enumerate(jsondata):
		outlist = []
		outlist.append(str(c+count+1))
		outlist.append(i["data"]["ups"])
		outlist.append(i["data"]["downs"])
		outlist.append(i["data"]["score"])
		outlist.append(i["data"]["num_comments"])
		outlist.append(i["data"]["author"])
		outstr += string.join([unicode(x) for x in outlist],'\t') + "\n"
		fileout.write(outstr)
		outstr = ""
	fileout.close()


# Note: os.sep below was not in the earlier version, 
# causing file to be written in dir immediately above.
def getIteratedReddits(max=200,url="http://www.reddit.com/.json",subreddit=""):
	'''This is the main controller method. Notice _i_ is in a range stepping by 25.
	This is a user configurable setting, so if this code worked on a logged in user
	it would have to be changed. I look at 50 reddits per page, for example.'''
	
	after = ""
	step = 25
	
	if subreddit != "":
		url = "http://www.reddit.com/r/%s.json" % subreddit
	# Remember, we do not need an 'else' statement here, since the URL is already a default argument. 
	# How would you restructure the code to not have the URL as an argument? 
	
	for i in range(0,max,step):
		print "Downloading stories from %d to %d (after %s)" % (i,i+step,after)

		reddit = getRedditJson(i,after,url)		
		time.sleep(3)
		addToTable(reddit["data"]["children"],PATH+os.sep+"redditstats.txt",i)

		after = reddit["data"]["after"]
		print after

	print "Finished downloading. File available at %s" % PATH + os.sep+"redditstats.txt"

# This is an unused helper method. 
# Use it to have a cleaner look at json than is provided raw from the server.
def downloadJsonToPretty(url = "http://www.reddit.com/.json", name="prettyjson.txt"):

	fileout = open(PATH + os.sep + name, 'w') 

	jsonfile = json.load(urllib2.urlopen(url))
	
	fileout.write(json.dumps(jsonfile, indent = 4))
	fileout.close()

	return jsonfile


# This method calls the other two. 
# See method above for optional arguments. 
getIteratedReddits(150)

# To Download for a subreddit: 
# getIteratedReddits(150,subreddit="aww")

# This method will print the main page by default to prettyjson.txt. 
# downloadJsonToPretty()