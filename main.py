from preprocess import  *
from svm import *
from svm import svm_data_transform
from preprocess import generate_tweet_user

def main(file):

    svm_data_transform.train_svm_model(file)
    # for output it will print the user id, user's name, user's decription, user's loction, and user's tweets
    users = generate_tweet_user.generatetweetuser("datacollection/tweets_json.txt")
    print users[0].__str__()

if __name__ == "__main__":
    main("Data.txt")
