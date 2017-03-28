import json

from get_tweets import get_timeline
from tool_utility import getToken,write_into_file_newline,write_into_file


def getTweets():
    name_array = getToken("name.txt")
    time_line_array = []
    tweetsArray = []
    lst = []
    d = {}
    for x in name_array:
        time_line_array = get_timeline(x,100)
        d[x] = time_line_array
        tweetsArray.extend(time_line_array)
    #write_into_file_newline(tweetsArray,"tweets.txt")
    lst.append(d)
    data = json.dumps(lst)
    write_into_file(data, "tweets_json.txt",'')

    #usage for read json file
    #data = json.loads(data)
    #for key, value in data[0].iteritems() :
    #print key, value

    return tweetsArray

getTweets()