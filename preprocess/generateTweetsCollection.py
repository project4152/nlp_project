#!/bin/usr/python

from generate_words_array import getAllWords
from preprocess.tool_utility import *
from tweet import tweet
from tweets_collection import tweets_collection


def generatorTweetsCollection(file):
    """
    :param file: input is the tweet data file
    :return: the tweets_collection object
    """
    data_array = getArrays(file)
    words = getAllWords(file)
    #create a Empty tweetCollection object
    tc = tweets_collection()

    for x in data_array:
        tw = createTweet(x,words)
        tc.addTweet(tw)


    return {
        "tweets_collection": tc,
        "features": words
    }

def createTweet(content,words):
    """
    :param content: first character is tag, followed is tweeet content, words:
    :return:  tweet object
    """
    temp = content[:1]

    if (isInt(temp)):
        tag = int(temp)
    else:
        tag = None

    #
    #need data preprocess in here
    #

    t = tweet(tag=tag,content=content[2:])
    t.add_vector(words)

    return t
#generatorTweetsCollection("Data.txt")

#example useage
# tweets = generatorTweetsCollection("Data.txt")
# print tweets.getAllTag()
# for x in tweets.getAllVector():
#     print x