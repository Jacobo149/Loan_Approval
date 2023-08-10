import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import missingno as mso
import seaborn as sns
import warnings
import os
import scipy

from scipy import stats
from scipy.stats import pearsonr
from scipy.stats import ttest_ind
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import CategoricalNB
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

def preproc():

    df = pd.read_csv('../resources/train_u6lujuX_CVtuZ9i.csv')

    df = df.drop(['Loan_ID'], axis = 1)
    df['Gender'].fillna(df['Gender'].mode()[0],inplace=True)
    df['Married'].fillna(df['Married'].mode()[0],inplace=True)
    df['Dependents'].fillna(df['Dependents'].mode()[0],inplace=True)
    df['Self_Employed'].fillna(df['Self_Employed'].mode()[0],inplace=True)
    df['Credit_History'].fillna(df['Credit_History'].mode()[0],inplace=True)
    df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0],inplace=True)
    df['LoanAmount'].fillna(df['LoanAmount'].mean(),inplace=True)

    df = pd.get_dummies(df, dtype=int)

    # Drop columns
    df = df.drop(['Gender_Female', 'Married_No', 'Education_Not Graduate', 
                'Self_Employed_No', 'Loan_Status_N'], axis = 1)

    # Rename columns name
    new = {'Gender_Male': 'Gender', 'Married_Yes': 'Married', 
        'Education_Graduate': 'Education', 'Self_Employed_Yes': 'Self_Employed',
        'Loan_Status_Y': 'Loan_Status'}
        
    df.rename(columns=new, inplace=True)

    #Remove outliers
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1

    df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]

    # Square Root Transformation

    df.ApplicantIncome = np.sqrt(df.ApplicantIncome)
    df.CoapplicantIncome = np.sqrt(df.CoapplicantIncome)
    df.LoanAmount = np.sqrt(df.LoanAmount)

    X = df.drop(["Loan_Status"], axis=1)
    y = df["Loan_Status"]

    X, y = SMOTE().fit_resample(X, y)


    X = MinMaxScaler().fit_transform(X)


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

    return df, X_train, y_train






#Plotting Results
'''
plt.plot(range(2,25), scoreListRF)
plt.xticks(np.arange(2,25,1))
plt.xlabel("RF Value")
plt.ylabel("Score")
plt.show()
RFAcc = max(scoreListRF)
print("Random Forest Accuracy:  {:.2f}%".format(RFAcc*100))
'''

