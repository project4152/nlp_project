import tweepy


consumer_key = "ZYJqiESGvdVppThthhk6AvO9B"
consumer_secret = "C1uP3LRb9b1e385cakmyJ24j6MYDpjMsW6ytzsTM4pxBeNNzSp"
access_key = "705525464736133120-7F9ngjewM9t4aHTXbD2hCavyWgL6ycV"
access_secret = "mQgnwMk2R1GTIpxlnq2wPwMkt3SjBRcPXjrtx0APDsVsV"



def get_profile(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        user_profile = api.get_user(screen_name)
    except:
        user_profile = "broken"

    #print user_profile.id
    #print user_profile.screen_name
    #print user_profile.location
    #print user_profile.description
    return user_profile

get_profile("HalifaxVintage")