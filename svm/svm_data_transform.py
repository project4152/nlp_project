"""
Transform the tweets data for training
"""

from preprocess.generateTweetsCollection import generatorTweetsCollection
from preprocess.generate_words_array import getAllWords
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn import metrics
from svm import svm_model
from nltk.stem import WordNetLemmatizer
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
import numpy
import pprint


def createTrainingDataset(data_input, features):
    training_dataset = data_input[:int(0.7 * len(data_input))]
    training_dataset_samples = [t.getContent() for t in training_dataset]
    training_dataset_classes = [t.getTag() for t in training_dataset]

    return {
        "training_samples": training_dataset_samples,
        "training_classes": training_dataset_classes
    }


def createTestDataset(data_input, features):
    test_dataset = data_input[int(0.7 * len(data_input)):]
    test_dataset_samples = [t.getContent() for t in test_dataset]
    test_dataset_classes = [t.getTag() for t in test_dataset]

    return {
        "test_samples": test_dataset_samples,
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
    expected_test_classes = test_collection["test_classes"]

    wordnet_lemmatizer = WordNetLemmatizer()
    vect = TfidfVectorizer(tokenizer=word_tokenize, ngram_range=(1, 1), stop_words=stopwords.words('english'), preprocessor= wordnet_lemmatizer.lemmatize)
    training_tfidf = vect.fit_transform(training_dataset)
    test_tfidf = vect.transform(test_dataset)

    svm = svm_model(penalty=1.0, kernel_type="linear", cache_size=300, decision_function_shape="ovr")

    svm.train_model(training_tfidf, training_classes)
    test_results = svm.predict(test_tfidf)
    # print "accuracy score: " + str(metrics.accuracy_score(expected_test_classes, test_results)) + "\n"
    return (vect, svm)
    # pprint.pprint(test_results)



