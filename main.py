from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())



import certifi

client =MongoClient("mongodb+srv://test:test@rm21.dgycuig.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db = client.test

dbs=client.list_database_names() 
print(dbs)

# view all items in the collection
# for item in db.test.find():
#     print(item)