# -*- coding: utf-8 -*-#

import pymongo
import emojilist as el 

client = pymongo.MongoClient()
db = client.test
tweets = db.tweettest3

# GET NUMBER OF RECORDS
# records = tweets.count()
# print records
# print tweets.find()[300]
# GET UNIQUE USERS

# users = []

# for i in tweets.find():
# 	if i.has_key("user"):
# 		users.append(i)

# users = set([i["user"]["screen_name"] for i in tweets.find() if i.has_key("user")])
# # users = set([i["user"]["screen_name"] for i in users])
# print len(users)

# GET UNIQUE GEOCODES
# longlats = [
# i["coordinates"]["coordinates"] for i in tweets.find() if i.has_key("coordinates") and i["coordinates"] 
# ]
# print longlats

# GET TEXTS
# texts = [i["text"] for i in tweets.find()]

for i in tweets.find():
	if i.has_key("text"):

		tweet = i["text"].encode("utf8")
		for j in el.emojilist:
			if j in tweet: 
				print j
				print tweet

