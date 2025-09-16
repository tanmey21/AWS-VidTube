from pymongo import MongoClient,errors
from dotenv import load_dotenv
import os
import certifi


load_dotenv()

def connecting_to_mongodb():

    try:
        client = MongoClient(os.getenv('MONGODB_URI'),tlsCAFile=certifi.where())
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except errors.ServerSelectionTimeoutError as e:
        # Timeout specific error
        raise RuntimeError(f"MongoDB connection timed out: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"MongoDB connection error: {str(e)}")
