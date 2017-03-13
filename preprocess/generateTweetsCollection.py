#!/bin/usr/python

from tweet import tweet
from tweets_collection import tweets_collection
from tool_utility import *

def generatorTweetsCollection(file):
    """
    :return: tweetsCollection object
    """
    data_array = getArrays(file)

    length = len(data_array)

    #Empty tweetCollection object
    tc = tweets_collection()

    for x in data_array:
        tc.addTweet(createTweet(x))


    #print tc.getAllTag()
    return tc


def createTweet(content):
    """
    :param content: first character is tag, followed is tweeet content
    :return:  tweet object
    """
    temp = content[:1]

    if (isInt(temp)):
        tag = int(temp)
    else:
        tag = None

    t = tweet(tag=tag,content=content[2:])

    return t

#generatorTweetsCollection("Data.txt")