# mongodb+srv://tani68667s1_db_user:ZeQKKNh8qqu9S56O@cluster0.x33mqsp.mongodb.net/
from pymongo.mongo_client import MongoClient
import pandas as pd 
import json

# url
url = 'mongodb+srv://tani68667s1_db_user:ZeQKKNh8qqu9S56O@cluster0.x33mqsp.mongodb.net/'

# create a new client and connect to server
client = MongoClient(url)

# create database and collection name 
DATABASE_NAME = 'sensorfault'
COLLECTION_NAME = 'waferfault'

# converted to json
df = pd.read_csv('wafer_23012020_041211.csv')
df = df.drop('Unnamed: 0', axis = 1)
json_record = df.to_dict(orient="records")

# inserting to mongodb
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)