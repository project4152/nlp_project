from preprocess import *
from datacollection import *
from svm import *
from svm import svm_data_transform


def main(file):
    """
    ideally, this file is treated as the main entry to this application
    1. it should read the training set and build a svm classifier
    2. it should retrieve the tweets for each user (user amount can be limited to 10000, 100000, and so on.
    3. it should organize users by districts
    4. it should classify the user tweets and summarize them
    5. it should draw the density graph.
    :param file:
    :return:
    """
    svm_data_transform.train_svm_model(file)


if __name__ == "__main__":
    main("Data.txt")
