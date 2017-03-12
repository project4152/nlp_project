#!/bin/usr/python

class tweet():

    def __init__(self,tag,content):
        self.tag = tag
        self.content = content

    def getTag(self):
        return self.tag

    def getContent(self):
        return self.content
