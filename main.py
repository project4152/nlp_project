from __future__ import division
from preprocess import *
# from datacollection import read_json_example
from datacollection import translate_geo
from datacollection import search_geo
from datacollection import read_json
from svm import *
from svm import svm_data_transform
from generate_graph import generate_map
import numpy


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

    # store tweets retrieved from tweets api categorized by province
    province_tweets_collection = read_json.read_formatted_tweets()


    # train model
    (vectorizer, svm_model) = svm_data_transform.train_svm_model(file)

    # intermediate stage as to store the transformed data by svm model
    province_tweets_tfidf_map = dict()
    for (province, tweets) in province_tweets_collection.items():
        tfidf_vector = vectorizer.transform(tweets)
        province_tweets_tfidf_map[province] = tfidf_vector

    # predict the positiveness and negativeness of the input tweets
    province_positive_emotion_predict_map = dict()
    for(province, tfidf_vector) in province_tweets_tfidf_map.items():
        prediction_vector = svm_model.predict(tfidf_vector)
        unique, counts = numpy.unique(prediction_vector, return_counts=True)
        unique_counts_map = dict(zip(unique, counts))
        province_positive_emotion_predict_map[province] = unique_counts_map.get(1)/ len(prediction_vector)

    generate_map.draw_map(province_positive_emotion_predict_map)
if __name__ == "__main__":
    main("Data.txt")
