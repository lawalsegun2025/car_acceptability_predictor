from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn import metrics
import pickle
import numpy as np

# split data into training and testing sets

def split_data(df):

    X = df[['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']]

    y = df['class']

    X_train, X_test, y_train, y_test = train_test_split(np.array(X), y, test_size=0.2)

    return X_train, X_test, y_train, y_test

# Logistic Regression

def logistic(df):

    X_train, X_test, y_train, y_test = split_data(df)
    lr = LogisticRegression()
    lr.fit(X_train, y_train)
    y_pred = lr.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred, average="macro")
    precision = metrics.precision_score(y_test, y_pred, average="macro")
    f1score = metrics.f1_score(y_test, y_pred, average="macro")
    
    return accuracy, recall, precision, f1score, lr