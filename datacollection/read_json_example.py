import json

def readIn(filename):
    filePath = filename
    buffer = ''
    buffer += open(filePath, 'rU').read()
    return buffer

def tweets_collection(file):

    result = []

    buffer = readIn(file)

    data = json.loads(buffer)

    for key, value in data[0].iteritems() :
        result += value
        print "screen_name:",key,"tweets_array:", value
        print "\n"


    return result