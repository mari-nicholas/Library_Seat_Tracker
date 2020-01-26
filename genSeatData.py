# seatTemplate = {
#     "seatNo" : 0 # num
#     "available" : #bool
#     "date" : #str
#     "time" : #str
# }

from random import randrange, randint

data = []

def makeSeat(i, a, j, d, t):
    seat = {
        "seatNo" : i, # num
        "available" : a,#bool
        "date" : j, #str
        "dayOfWeek" : d, #int
        "time" : t, #str
    }

    return seat

def makeTime(st, s):
    return str(st // 60).zfill(2) + ":" + str(st % 60).zfill(2) + ":" + str(s).zfill(2)

#for i in seatNos:
for i in range(100):
    dow = 3 #day of week
    for j in ["2020-01-" + str(i).zfill(2) for i in list(range(1, 26))]:
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
        a = 1
        data.append(makeSeat(i, a, j, dow, makeTime(st, 0)))
        while True:
            st += randrange(20, 91)
            if st < et:
                a += 1; a = a % 2
                t = makeTime(st, randint(0, 59))
                data.append(makeSeat(i, a, j, dow, t))
            else:
                break
        dow += 1
        dow = dow % 7

for i in data:
    print(i)
