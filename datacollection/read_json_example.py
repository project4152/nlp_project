import json

def readIn(filename):
    filePath = filename
    buffer = ''
    buffer += open(filePath, 'rU').read()
    return buffer


buffer = readIn("tweets_json.txt")

data = json.loads(buffer)

for key, value in data[0].iteritems() :
    print "screen_name:",key,"tweets_array:", value
    print "\n"
