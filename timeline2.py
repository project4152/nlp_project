import tweepy
import time
import sys


consumer_key = "ZYJqiESGvdVppThthhk6AvO9B"
consumer_secret = "C1uP3LRb9b1e385cakmyJ24j6MYDpjMsW6ytzsTM4pxBeNNzSp"
access_key = "705525464736133120-7F9ngjewM9t4aHTXbD2hCavyWgL6ycV"
access_secret = "mQgnwMk2R1GTIpxlnq2wPwMkt3SjBRcPXjrtx0APDsVsV"



def get_timeline(screen_name,number):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        tweets = tweepy.Cursor(api.search,
                                   q="google",
                                   rpp=100,
                                   result_type="recent",
                                   include_entities=True,
                                   lang="en").items()
        for tweet in tweets:
            print tweet.created_at, tweet.text
    except:
        print "broken"
        return tweets
if ( len(sys.argv)!=3 ):
    print 'Usage: timeline name number'
    print 'Such as python timeline cd_conrad 10'
    print 'print 10 timeline of cd_conrad'
else:
    t = get_timeline(sys.argv[1],sys.argv[2])
