from os import read 
from flask import Flask, request, render_template
from sklearn.preprocessing import LabelEncoder 
import pandas as pd 
from modelbuilding import logistic, dtree, randomforest, svc, knn


app = Flask(__name__)


# reading the data from csv file

def read_data():
    col_names = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]

    df = pd.read_csv("car_data.csv", names=col_names)

    return df









@ app.route("/", methods=["GET", "POST"])
def hello_world():

    get_mappings, data = label_encoding(read_data())

    if request.method == "POST":

        my_dict = request.form
        buy = my_dict["buy"]
        maintain = my_dict["maintain"]
        doors = my_dict["doors"]
        person = my_dict["person"]
        luggage = my_dict["luggage"]
        safety = my_dict["safety"]