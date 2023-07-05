from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn import metrics
import pickle

# split data into training and testing sets

def split_data(df):

    X = df[['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']]

    y = df['class']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)