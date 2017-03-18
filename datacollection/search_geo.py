
import twitter
import csv


class searchUser_geo():
    def __init__(self,file):
        self.file = file
        #defulat value
        self.latitude = 44.64594101249177
        self.longitude = -63.595733642578125
        self.max_range = 1
        self.num_results = 1000
        self.outfile = file
        config = {}
        execfile("config.py", config)

        self.search = twitter.Api(access_token_key=config["access_key"], access_token_secret=config["access_secret"],
                        consumer_key=config["consumer_key"], consumer_secret=config["consumer_secret"])


    def search_geo(self,latitude,longitude,max_range,num_results):

        if (latitude is not None):
            self.latitude = latitude
            self.longitude = longitude
            self.max_range = max_range
            self.num_results = num_results

        cfile = file(self.file,"w")
        cswfile = csv.writer(cfile)

        row = ["user", "text", "latitude", "longitude"]
        cswfile.writerow(row)

        query = self.search.GetSearch(geocode="%f,%f,%dkm" % (self.latitude, self.longitude, self.max_range), count=1000)
        nameArray=[]
        for t in query:
            nameArray.append(t.user.screen_name)


        for t in query:
            print t.user.screen_name + ' (' + t.created_at + ')'
            # Add the .encode to force encoding
            print t.user.id
            print t.user.location
            print t.user.statuses_count
            print t.text.encode('utf-8')
            print ''

        return nameArray

def write_into_file_newline(array, filename):
    write_into_file(array,filename,'\n')

def write_into_file(array, filename, separate):
    f = open(filename,"w")

    for x in array:
        f.write(x)
        f.write(separate)

    f.close()

a= searchUser_geo("data.csv").search_geo(None,None,None,None)


write_into_file_newline(a,"name1.txt")





