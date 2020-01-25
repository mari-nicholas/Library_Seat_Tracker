import pymongo

client = pymongo.MongoClient("mongodb+srv://<username>:<password>@library-seat-tracker-fvhnk.azure.mongodb.net/test?retryWrites=true&w=majority")
db = client.test