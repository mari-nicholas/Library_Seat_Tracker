import getpass
import pymongo

un = input('Enter username: ')
pw = getpass.getpass(prompt='Enter password: ') 

client = pymongo.MongoClient("mongodb+srv://"+un+":"+pw+"@library-seat-tracker-fvhnk.azure.mongodb.net/gettingStarted?retryWrites=true&w=majority")
db = client.seatsAvailable
seats = db.seats

# for i in cursor:
#     print(i)
