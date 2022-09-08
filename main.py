from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv()
import certifi

password=os.getenv("PSWD")


client =MongoClient(f"mongodb+srv://test:{password}@rm21.dgycuig.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())

db = client.test

dbs=client.list_database_names() 
print(dbs)

# view all items in the collection
for item in db.test.find():
    print(item)