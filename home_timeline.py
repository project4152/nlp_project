import tweepy

consumer_key = "ZYJqiESGvdVppThthhk6AvO9B"
consumer_secret = "C1uP3LRb9b1e385cakmyJ24j6MYDpjMsW6ytzsTM4pxBeNNzSp"
access_key = "705525464736133120-7F9ngjewM9t4aHTXbD2hCavyWgL6ycV"
access_secret = "mQgnwMk2R1GTIpxlnq2wPwMkt3SjBRcPXjrtx0APDsVsV"

def get_home_timeline():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print tweet.text
        
get_home_timeline()
