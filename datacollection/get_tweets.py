import tweepy
import time
import sys




def get_timeline(screen_name, number):
    config = {}
    execfile("config.py", config)
    auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
    auth.set_access_token(config["access_key"], config["access_secret"])
    api = tweepy.API(auth)
    try:
        tweets = api.user_timeline(screen_name=screen_name, count=number)
        for n in tweets:
            print n.text
            print "\n"
    except:
        print "broken"
    return tweets


if (len(sys.argv) != 3):
    print 'Usage: timeline name number'
    print 'Such as python timeline cd_conrad 10'
    print 'print 10 timeline of cd_conrad'
else:
    tweets = get_timeline(sys.argv[1], sys.argv[2])

