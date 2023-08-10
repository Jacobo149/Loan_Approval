import preprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import missingno as mso
import seaborn as sns
import warnings
import os
import scipy
from sklearn.ensemble import RandomForestClassifier



def train():
    df, X_train, y_train = preprocess.preproc()
    for i in range(2,25):
        RFclassifier = RandomForestClassifier(n_estimators = 1000, random_state = 1, max_leaf_nodes=i)
        RFclassifier.fit(X_train, y_train)

    return df, RFclassifier

def predict(df, rf, pred):
    return rf.predict([pred])

#pred = [76,0,12,360,1,1,0,1,0,0,0,1,0,0,0,1]
#df, rf = train()
#print(predict(df, rf, pred))