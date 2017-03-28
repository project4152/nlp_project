import json

from twitter_user import tweet_user
from tool_utility import readIn
from datacollection.get_user_profile import get_profile


def generatetweetuser():
    buffer = readIn("../datacollection/tweets_json.txt")
    data = json.loads(buffer)
    users = []


    for key, value in data[0].iteritems():
        profile = get_profile(key)
        user = tweet_user(profile.id,profile.screen_name,profile.description,profile.location)
        user.add_tweets(value)
        users.append(user)
    return users


#sample useage
user = generatetweetuser()
print user[0].__str__()