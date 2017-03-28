class tweet_user():
    def __init__(self,userid,screen_name,decription,location):
        self.userid=userid
        self.screen_name = screen_name
        self.decription = decription
        self.location = location
        self.tweets_collection = []

    def add_tweets(self,tweets):
        self.tweets_collection.extend(tweets)

    def __str__(self):
        return self.userid,self.screen_name,self.decription,self.location,self.tweets_collection




