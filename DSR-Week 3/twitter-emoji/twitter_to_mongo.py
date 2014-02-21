import sys
import twitter

import twitterhelpers as th

# print twitter.__version__
print twitter.__file__
print help(Twitter)
# sys.exit()
# print dir(twitter)
# sys.exit()
# print help(twitter.api)

t = Twitter(auth=OAuth(th.ACCESS_TOKEN, th.ACCESS_TOKEN_SECRET, th.CONSUMER_KEY, th.CONSUMER_SECRET))
t.statuses.home_timeline()


# t.VerifyCredentials()
# (consumer_key=th.CONSUMER_KEY,
#                       consumer_secret=th.CONSUMER_SECRET,
#                       access_token_key=th.ACCESS_TOKEN,
#                       access_token_secret=th.ACCESS_TOKEN_SECRET)


# print api.VerifyCredentials()


# def oauth_login():
#     auth = twitter.oauth.OAuth(,th.ACCESS_TOKEN_SECRET,th.CONSUMER_KEY,) 
#     twitter_api = twitter.Twitter(auth = auth)
#     return twitter_api
#     
# q = "grammys"
# 
# api = oauth_login()
# 
# print api.VerifyCredentials()
# sys.exit()
# 
# twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)
# 
# print dir(twitter_stream.statuses.filter)
# 
# stream = twitter_stream.statuses.filter(track=["justin"])
# for tweet in stream:
#     print tweet['text']
#     