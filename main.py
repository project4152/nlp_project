from preprocess import  *
from svm import *
from svm import svm_data_transform

def main(file):
    svm_data_transform.train_svm_model(file)

if __name__ == "__main__":
    main("Data.txt")
