import twitter
import config
import get_tweets
from tool_utility import getToken
from sets import Set
import random
import time



class searchUser_geo():
    def __init__(self):

        config = {}
        execfile("datacollection/config.py", config)

        self.search = twitter.Api(access_token_key=config["access_key"], access_token_secret=config["access_secret"],
                        consumer_key=config["consumer_key"], consumer_secret=config["consumer_secret"])


    def search_geo(self,latitude,longitude,max_range,num_results):
        query = self.search.GetSearch(geocode="%f,%f,%dkm" % (latitude, longitude, max_range), count=num_results)
        nameArray=[]
        for t in query:
            nameArray.append(t.user.screen_name)

        return nameArray

def write_into_file_newline(array, filename):
    write_into_file(array,filename,'\n')

def write_into_file(array, filename, separate):
    f = open(filename,"w")

    for x in array:
        f.write(x)
        f.write(separate)

    f.close()

def get_screen_name(location):
    """
    return users searched within a given longitude and latitude
    :param location:
    :return:
    """
    # location = getToken(inputfile)
    # length = len(location)
    count = 0
    name_list = []
    search = searchUser_geo()
    tweets = []
    name_list = Set()
    longitude = location.longitude
    latitude = location.latitude
    while len(tweets) < 1000:
        try:
            screan_names = search.search_geo(float(longitude), float(latitude), 1, 1000)
            print  screan_names
            tmp = Set(screan_names)
            if len(name_list.difference(tmp)) != 0:
                name_list.update(tmp)
                diff_names = name_list.difference(tmp)
                for name in diff_names:
                    tweets.extend(get_tweets.get_timeline(name, 50))
                print tweets
            longitude += random.uniform(-1, 1)
            latitude += random.uniform(-1, 1)
        except twitter.error.TwitterError:
            print 1
            time.sleep(60 * 15)
            print 1

    write_into_file(tweets, "tweets" + "_" + location.address + ".txt", "\n")

    return tweets



    # while count < length:
    #     screan_names= search.search_geo(float(location[count]),float(location[(count+1)]),1,1000)
    #     name_list.extend(screan_names)
    #     count = count + 2

    # write_into_file_newline(set(name_list),outputfile)

# get_screen_name("location.txt","name.txt")




