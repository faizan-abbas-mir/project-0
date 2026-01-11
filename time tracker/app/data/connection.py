import pymongo
import os
from dotenv import load_dotenv
load_dotenv()
client=pymongo.MongoClient(os.getenv("MONGODB_URL"))
dbname=client["timetracker"]
print(client)
