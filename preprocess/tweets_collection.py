#!/bin/usr/python
import array
from tweet import tweet
import random
import copy

class tweets_collection:
    def __init__(self):
        self.tweets = dict()
        self.size = 0

    def addTweet(self,tweet):
        self.tweets[self.size] = tweet
        self.size += 1

    def getAllTag(self):
        return self.tweets.keys()

    def getAllVector(self):
        vectors = []
        for x in self.tweets.values():
            vectors.append(x.get_document_vector())
        return vectors

    def get_tweets(self):
        return self.tweets.values()

    def getAllContent(self):

        contents = []

        for x in self.tweets.values():
            contents.append(x.getContent())

        return contents

    def getAllContentInLowerCase(self):
        contents = []
        for x in self.tweets.values():
            contents.append(x.getContent().lower)

        return contents

    def getRandomizedTweets(self):
        tmp = copy.deepcopy(self.tweets.values())
        random.shuffle(tmp)
        return tmp

    def __str__(self):
        output=""
        for x in self.tweets.value:
            output.join(x)
            output.join('\n')

        return output


