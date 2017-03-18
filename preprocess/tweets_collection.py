#!/bin/usr/python
import array
from tweet import tweet

class tweets_collection:
    def __init__(self):
        self.tweets = []

    def addTweet(self,tweet):
        self.tweets.append(tweet)

    def getAllTag(self):

        tags = []

        for x in self.tweets:
            tags.append(x.getTag())

        return tags


    def get_tweets(self):
        return self.tweets

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




#print create_document_term_vector(["very","good"],"very good very")