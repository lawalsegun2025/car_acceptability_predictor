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


# groupby with target (class) col
def get_dict(col_name):

    df = read_data()

    return dict(df.groupby([col_name])["class"].count())



# label encoding 
def label_encoding(df):

    encoder = LabelEncoder()
    data = df.copy()
    get_mappings = {}

    for col in list(data.columns):
        data[col] = encoder.fit_transform(data[col])

        # get the mappings of the encoded dataframe
        get_mappings[col] = dict(
            zip(encoder.classes_, encoder.transform(encoder.classes_))
        )

    return get_mappings, data




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
        algo = my_dict["algo"]

        value = my_dict['feature']

        values = ["Buying", "Maitainance", "Doors",
                  "Persons", "Luggage", "Safety"]
        keys = ['buying', 'maint', 'doors',
                'persons', 'lug_boot', 'safety', 'class']
        mapper = dict(zip(keys, values))

        value_count = get_dict(value)

        # Selection of Algorithm
        algo_mapper = {'rf': randomforest(data), 
                       'dt': dtree(data), 
                       'svc': svc(data)}
        
        class_mapper = {0: 'Accurate', 1: 'Good', 
                        2: 'Unaccurate', 3: 'VeryGood'}
        
        algorithm = algo_mapper[algo]
        accuracy, recall, precision, f1score, model = algorithm

        input_param = [[buy, maintain, doors, person, luggage, safety]]
        predict = model.predict(inpute_param)
        predicted_class = class_mapper[predict[0]]

        return render_template('index.html', predicted_class=predicted_class, display=True, accuracy=round(accuracy*100, 2), precision=precision, showtemplate=True, value_count=value_count, value=mapper[value], mapper=value_count)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

