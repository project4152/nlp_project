import json

from twitter_user import tweet_user
from tool_utility import readIn
from datacollection.get_user_profile import get_profile


def generatetweetuser(inputfile):

    if inputfile is None:
        inputfile = "../datacollection/tweets_json.txt"

    buffer = readIn(inputfile )
    data = json.loads(buffer)
    users = []


    for key, value in data[0].iteritems():
        profile = get_profile(key)
        user = tweet_user(profile.id,profile.screen_name,profile.description,profile.location)
        user.add_tweets(value)
        users.append(user)
    return users


#sample useage
user = generatetweetuser(None)
#for output it will print the user id, user's name, user's decription, user's loction, and user's tweets
print user[0].__str__()