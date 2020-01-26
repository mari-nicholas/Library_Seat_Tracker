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

inputDate = 31
inputTime = 14

dow = (inputDate + 3) % 7

if dow == 0:
    assert(12 <= inputTime <= 22)
elif dow == 5:
    assert(8 <= inputTime <= 17)
elif dow == 6:
    assert(10 <= inputTime <= 17)
else:
    assert(8 <= inputTime <= 22)

X_TEST = [[inputDate, dow, inputTime]]

for i in dataset:
    if i["dayOfWeek"] == dow and abs(i["hour"] - inputTime) < 2:
        print(i)

predictor = joblib.load('finalized_model.sav')
outcome = predictor.predict(X=X_TEST)

print('\nOutcome: {0:5.2f}'.format(float(outcome[0])))
