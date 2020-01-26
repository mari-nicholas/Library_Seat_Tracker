import getpass
import pymongo

from random import randrange, randint

un = input('Enter username: ')
pw = getpass.getpass(prompt='Enter password: ') 

client = pymongo.MongoClient("mongodb+srv://"+un+":"+pw+"@library-seat-tracker-fvhnk.azure.mongodb.net/seatsAvailable?retryWrites=true&w=majority")
db = client.seatsAvailable
seats = db.seats

data = []

def makeSeat(i, y, mo, j, d, h, m, a):
    seat = {
        "seatNo" : i,
        "year" : y,
        "month" : mo,
        "day" : j,
        "dayOfWeek" : d,
        "hour" : h,
        "min" : m,
        "available" : a,
    }

    return seat

#for i in seatNos:
for i in range(100):
    dow = 3 #day of week
    for j in range(1, 26):
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
        data.append(makeSeat(i, 2020, 1, j, dow, st // 60, st % 60, a))
        while True:
            st += randrange(20, 91)
            if st < et:
                a += 1; a = a % 2
                data.append(makeSeat(i, 2020, 1, j, dow, st // 60, st % 60, a))
            else:
                break
        dow += 1
        dow = dow % 7

for i in data:
    print(i)
    # seats.insert_one(i)

# cursor = seats.find({})[0]
# print(cursor)
