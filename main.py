from preprocess import *
from datacollection import read_json_example
from datacollection import translate_geo
from datacollection import search_geo
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
    province_city_map = translate_geo.translate("datacollection/province_city.txt")
    city_tweets_map = dict()
    city_tweets_tfidf_map = dict()
    for (province, city) in province_city_map.items():
        city_tweets_map[city] = search_geo.get_screen_name(city)
    (vectorizer, svm_model) = svm_data_transform.train_svm_model(file)
    # raw_tweets = read_json_example.tweets_collection("datacollection/tweets_json.txt")
    for (city, raw_tweets) in city_tweets_tfidf_map.items():
        tfidf_vector = vectorizer.transform(raw_tweets)
        city_tweets_tfidf_map[city] = tfidf_vector

    city_positive_emotion_predict_map = dict()
    for (city, tfidf_vector) in city_tweets_tfidf_map.items():
        city_positive_emotion_predict_map[city] = svm_model.predict(tfidf_vector)
        print city_positive_emotion_predict_map[city]


if __name__ == "__main__":
    main("Data.txt")
