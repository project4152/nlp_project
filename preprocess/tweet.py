#!/bin/usr/python
import array
import re, string, timeit
class tweet():

    def __init__(self,tag,content):
        self.tag = tag
        self.content = content
        self.document_terms_vector=[]

    def getTag(self):
        return self.tag

    def getContent(self):
        return self.content

    def document_terms(self,document_terms):
        self.document_terms_vector = document_terms

    def get_document_vector(self):

        return self.document_terms_vector

    def add_vector(self, words):

        self.document_terms_vector = self.create_document_term_vector(words, self.content)

    def create_document_term_vector(self, words, tweet):
        length = len(words)
        words_array = tweet.split()
        vector_array = [0]*length
        for x in words_array:
            x = x.lower()
            if x in words:
                num = words.index(x)
                vector_array[num] += 1

        return vector_array


    def __str__(self):
        return "tag: ",self.tag,"   vector",self.document_terms_vector


