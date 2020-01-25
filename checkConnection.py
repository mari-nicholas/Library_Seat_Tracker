import getpass
import pymongo

un = input('Enter username: ')
pw = getpass.getpass(prompt='Enter password: ') 

client = pymongo.MongoClient("mongodb+srv://"+un+":"+pw+"@library-seat-tracker-fvhnk.azure.mongodb.net/gettingStarted?retryWrites=true&w=majority")
db = client.gettingStarted

# cursor = db.people.find({})[0]
# print(cursor)