import datetime
from flask import Flask, redirect
from flask_cors import CORS
from sklearn.externals import joblib
from smlHelpers import *

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def home():
    return ("hi", 200)

@app.route('/api')
def function():
    with open('dataset.txt', 'r') as f: 
        l = f.readlines()

    dataset = []

    for line in l:
        line = line.split()
        dataset.append({
                "day" : int(line[0]),
                "dayOfWeek" : int(line[1]),
                "hour" : int(line[2]),
                "available" : float(line[3])
            })

    d = datetime.datetime.today()

    inputDate = int(d.strftime("%d"))
    dow = int(d.strftime("%w"))
    inputTime = int(d.strftime("%H"))

    if not thodeOpen(dow, inputTime):
        return "Thode is currently closed; it opens today at {}.".format(getOpenTime(dow))
    else:
        predictor = joblib.load('finalized_model.sav')
        s = "This hour, Thode is expected to be {0:5.2f} available.".format(float(predictor.predict(X=[[inputDate, dow, inputTime]])[0]))
        if thodeOpen(dow, inputTime + 1):
            s += "Next hour, Thode is expected to be {0:5.2f} available.".format(float(predictor.predict(X=[[inputDate, dow, inputTime + 1]])[0]))
        return s

if __name__ == "__main__":
    app.run(host="localhost", port="8888")

# for i in dataset:
#     if i["dayOfWeek"] == dow and abs(i["hour"] - inputTime) < 2:
#         print(i)

# predictor = joblib.load('finalized_model.sav')
# outcome = predictor.predict(X=[[inputDate, dow, inputTime]])

# print('\nOutcome: {0:5.2f}'.format(float(outcome[0])))
