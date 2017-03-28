import twitter
import config

from tool_utility import getToken



class searchUser_geo():
    def __init__(self):

        config = {}
        execfile("config.py", config)

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



def get_screen_name(inputfile,outputfile):
    location = getToken(inputfile)
    length = len(location)
    count = 0
    name_list = []
    search = searchUser_geo()
    while count < length:
        screan_names= search.search_geo(float(location[count]),float(location[(count+1)]),1,1000)
        name_list.extend(screan_names)
        count = count + 2

    write_into_file_newline(set(name_list),outputfile)

get_screen_name("location.txt","name.txt")




