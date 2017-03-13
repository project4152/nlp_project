#!/bin/usr/python

from tweet import tweet

class tweets_collection():
    def __init__(self):
        self.tweets = []

    def addTweet(self,tweet):
        self.tweets.append(tweet)

    def getAllTag(self):

        tags = []

        for x in self.tweets:
            tags.append(x.getTag())

        return tags


    def getAllContent(self):

        contents = []

        for x in self.tweets:
            contents.append(x.getContent())

        return contents

    def getAllContentInLowerCase(self):

        contents = []

        for x in self.tweets:
            contents.append(x.getContent().lower)

        return contents