import getpass
import datetime
import pymongo

un = input('Enter username: ')
pw = getpass.getpass(prompt='Enter password: ') 

client = pymongo.MongoClient("mongodb+srv://"+un+":"+pw+"@library-seat-tracker-fvhnk.azure.mongodb.net/gettingStarted?retryWrites=true&w=majority")
db = client.seatsAvailable
seats = db.seats


dt = datetime.datetime.today()
#print( dt.strftime("%X"))
seatDocument = {
	"seatNo" : 0,
	"available" : True,
	"date" : dt.strftime("%F"),
	"time" : dt.strftime("%X")
}

seats.insert_one(seatDocument)