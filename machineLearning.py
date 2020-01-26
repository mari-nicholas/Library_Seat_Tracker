import getpass
import pymongo
import datetime

from random import randrange, randint
from pandas import read_csv, DataFrame
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# un = input('Enter username: ')
# pw = getpass.getpass(prompt='Enter password: ') 

client = pymongo.MongoClient("mongodb+srv://ADMIN:admin@library-seat-tracker-fvhnk.azure.mongodb.net/seatsAvailable?retryWrites=true&w=majority")
db = client.seatsAvailable
seats = db.seats

selection = list(seats.find( {} ))
# for i in selection:
#     print(i)

# dt = datetime.datetime.today()
# dow = int(dt.strftime("%w")) 

limit = len(selection)

data = []

dow = 3
for day in range(1, 26): # doesn't do today
    if dow == 0:
        st = 12 * 60
        et = 22 * 60 + 45
    elif dow == 5:
        st = 8 * 60
        et = 17 * 60 + 45
    elif dow == 6:
        st = 10 * 60 + 30
        et = 17 * 60 + 45
    else:
        st = 8 * 60
        et = 22 * 60 + 45
    
    data.append([])
    ind = 0
    if st % 60 == 0:
        firstTime = True
    else:
        firstTime = False
    data[day-1].append([])
    while st != et:
        if st % 60 == 0:
            if firstTime:
                firstTime = False
            else:
                data[day-1].append([])
                ind += 1
        seat, count = 0, 0
        for i in range(limit - 1):
            begin = selection[i]
            end = selection[i + 1]
            if begin["day"] == day and end["day"] == day:
                if begin["hour"] * 60 + begin["min"] <= st <= end["hour"] * 60 + end["min"]:
                    count += begin["available"]
        if count == 0:
            data[day-1][ind].append(100)
        else:
            data[day-1][ind].append(count)
        st += 15
    # print("Day " + str(day) + " done.")
    if dow == 6:
        dow = 0
    else:
        dow += 1
    for i in range(len(data[-1])):
        l = data[-1][i]
        data[-1][i] = round(sum(l) / len(l), 2)
    # print(data[-1])

dow = 3
dataset = []
for i in range(len(data)):
    if dow == 0:
        st = 12
    elif dow == 6:
        st = 10
    else:
        st = 8 
    for j in range(len(data[i])):
        
        point = {
            "day" : i + 1,
            "dayOfWeek" : dow,
            "hour" : st + j,
            "available" : data[i][j]
        }
        dataset.append(point)
    if dow == 6:
        dow = 0
    else:
        dow += 1

print(len(dataset))
for i in dataset:
    print(i)


dataTrain = DataFrame(dataset)

array = dataTrain.values
X = array[:,0:3]
# print(X)
y = array[:,3]
# print(y)
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=69)

print("Split and ready to train\n")

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=X, y=y)

X_TEST = [[29, 3, 8]]
outcome = predictor.predict(X=X_TEST)
coefficients = predictor.coef_

print('Outcome : {}\nCoefficients : {}'.format(outcome, coefficients))
