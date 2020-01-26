import datetime
from sklearn.externals import joblib

with open('dataset.txt', 'r') as f: 
    l = f.readlines()

dataset = []

for line in l:
    line = line.split()
    dataset.append({
            "day" : int(line[0]),
            "dayOfWeek" : int(line[1]),
            "hour" : int(line[2]),
            "available" : int(line[3])
        })

d = datetime.datetime.today()

inputDate = int(d.strftime("%d"))
dow = int(d.strftime("%w"))
inputTime = int(d.strftime("%H"))

def thodeOpen(d, i):
    if d == 0:
        return(12 <= i < 22)
    elif d == 5:
        return(8 <= i < 17)
    elif d == 6:
        return(10 <= i < 17)
    else:
        return(8 <= i < 22)

def getOpenTime(dow):
    if dow == 0:
        return "12:00"       
    elif dow == 6:
        return "10:30"
    else:
        return "8:00"

if not thodeOpen(dow, inputTime):
    print("Thode is currently closed; it opens today at {}.".format(getOpenTime(dow)))
else:
    predictor = joblib.load('finalized_model.sav')
    print("This hour, Thode is expected to be {0:5.2f} available.".format(float(predictor.predict(X=[[inputDate, dow, inputTime]])[0])))
    if thodeOpen(dow, inputTime + 1):
        print("Next hour, Thode is expected to be {0:5.2f} available.".format(float(predictor.predict(X=[[inputDate, dow, inputTime + 1]])[0])))

# for i in dataset:
#     if i["dayOfWeek"] == dow and abs(i["hour"] - inputTime) < 2:
#         print(i)

# predictor = joblib.load('finalized_model.sav')
# outcome = predictor.predict(X=[[inputDate, dow, inputTime]])

# print('\nOutcome: {0:5.2f}'.format(float(outcome[0])))
