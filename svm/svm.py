"""
Here uses the Support Vector Machine algorithm from python sklearn library
"""

from sklearn.svm import SVC

class svm_model:
    def __init__(self, penalty, kernel_type, cache_size, decision_function_shape):
        self.svm_model = SVC(C=penalty, kernel=kernel_type, cache_size=cache_size, decision_function_shape=decision_function_shape)
    def train_model(self, samples, classes):
        self.svm_model.fit(samples, classes)
    def predict(self, tests):
        return self.svm_model.predict(tests)