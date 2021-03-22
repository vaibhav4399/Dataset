import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://User:50sotusoa@cluster0.7dzpl.mongodb.net/User?retryWrites=true&w=majority")

db = client.User
