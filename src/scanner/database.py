from pymongo import MongoClient
from os import environ

client = MongoClient(host="mongodb",
                     port=int(environ['MONGO_PORT']),
                     username=environ['MONGO_USER'],
                     password=environ['MONGO_PASS'])
db = client[environ['MONGO_DB']]
attack_coll = db[environ['MONGO_COLL']]
