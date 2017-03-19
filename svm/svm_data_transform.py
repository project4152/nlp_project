"""
Transform the tweets data for training
"""

from preprocess.generateTweetsCollection import generatorTweetsCollection
from preprocess.generate_words_array import getAllWords
from sklearn.feature_extraction.text import TfidfTransformer
import svm
from sklearn import metrics
import numpy


def createTrainingDataset(data_input, features):
    training_dataset = data_input[:int(0.7 * len(data_input))]
    training_dataset_samples = [t.getContent() for t in training_dataset]
    training_dataset_classes = [t.getTag() for t in training_dataset]

    return {
        "training_samples": numpy.array([features, training_dataset_samples], nmin=2),
        "training_classes": training_dataset_classes
    }


def createTestDataset(data_input, features):
    test_dataset = data_input[int(0.7 * len(data_input)):]
    test_dataset_samples = [t.getContent() for t in test_dataset]
    test_dataset_classes = [t.getTag() for t in test_dataset]

    return {
        "test_samples": numpy.array([features, test_dataset_samples], nmin=2),
        "test_classes": test_dataset_classes
    }
def train_svm_model(file):

    tweets_collection_object = generatorTweetsCollection(file)
    tweets = tweets_collection_object['tweets_collection']
    features = tweets_collection_object['features']
    t_arr = tweets.getRandomizedTweets()

    #create training dataset to train svm models
    training_collection = createTrainingDataset(t_arr, features)
    training_dataset = training_collection["training_samples"]
    training_classes = training_collection["training_classes"]

    #create test dataset to test model predicting accuracy
    test_collection = createTestDataset(t_arr, features)
    test_dataset = test_collection["test_samples"]
    test_classes = test_collection["test_classes"]


    training_tfidf_transformer = TfidfTransformer(norm='l1', use_idf=True, smooth_idf=True, sublinear=False)
    training_dataset_transformed = training_tfidf_transformer.fit_transform(training_dataset)

    svm_model = svm(penalty=1.0, kernel_type="linear", cache_size=300, decision_function_shape="ovr")

    svm_model.train_model(training_dataset_transformed, training_classes)
    test_results = svm_model.predict(test_dataset)
    print "accuracy score: " + str(metrics.accuracy_score(test_classes, test_results)) + "\n"



