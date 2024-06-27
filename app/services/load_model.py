import joblib
import numpy as np
from sklearn.datasets import load_iris

def load_model():
    model_trained = joblib.load('app/services/iris_model.pkl')
    iris = load_iris()
    model_trained.target_names = iris.target_names
    return model_trained
    