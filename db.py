import os
from pymongo import MongoClient
import gridfs
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db():
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    db_name = os.getenv("MONGO_DB", "video_db")

    client = MongoClient(mongo_uri)
    return client[db_name]

def get_fs():
    db = get_db()
    return gridfs.GridFS(db)
