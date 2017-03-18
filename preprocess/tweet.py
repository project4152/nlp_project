#!/bin/usr/python
import array
import re, string, timeit
class tweet():

    def __init__(self,tag,content):
        self.tag = tag
        self.content = content
        self.document_terms is None

    def getTag(self):
        return self.tag

    def getContent(self):
        return self.content

    def document_terms(self,document_terms):
        self.document_terms = document_terms

    def get_document_vector(self):

        return self.document_terms

    def add_vector(self, words):

        self.document_terms = self.create_document_term_vector(words, self.content)

    def create_document_term_vector(self, words, tweet):
        length = len(words)
        words_array = tweet.split()
        vector_array = array.array('i', (0 for i in range(0, length)))

        for x in words_array:
            x = x.lower()
            if x in words:

                num = words.index(x)
                vector_array[num] += 1
        print vector_array
        return vector_array


