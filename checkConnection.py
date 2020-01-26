import getpass
import pymongo

# un = input('Enter username: ')
# pw = getpass.getpass(prompt='Enter password: ') 

client = pymongo.MongoClient("mongodb+srv://ADMIN:admin@library-seat-tracker-fvhnk.azure.mongodb.net/gettingStarted?retryWrites=true&w=majority")
db = client.seatsAvailable
seats = db.seats

seats.remove({"seatNo": -1})

cursor = list(seats.find({}))[-50:-1]
for i in cursor:
    print(i)
